import json
import requests
import urllib3

urllib3.disable_warnings()


class vCloudDirector:
    VCD_HOST_URL = ""
    VCD_USERNAME = ""
    VCD_PASSWORD = ""
    VCD_TOKEN = ""
    REPORT_DATA = {}

    def __init__(self, vcd_url, vcd_username, vcd_password):
        self.VCD_HOST_URL = vcd_url
        self.VCD_USERNAME = vcd_username
        self.VCD_PASSWORD = vcd_password
        self.VCD_TOKEN = self.generateTokenForVCD()

    def generateTokenForVCD(self):
        url = f"{self.VCD_HOST_URL}/api/sessions"

        headers = {"Accept": "application/*+json;version=34.0"}
        proxies = {"http": None, "https": None}

        response = requests.request(
            "POST",
            url,
            auth=(self.VCD_USERNAME, self.VCD_PASSWORD),
            headers=headers,
            verify=False,
            proxies=proxies,
        )

        if response.status_code == 200:
            print("Request generateTokenForVCD Successful. Getting details from response...")
            token = response.headers.get("X-VMWARE-VCLOUD-ACCESS-TOKEN")

        else:
            raise Exception(f"Request generateTokenForVCD Failed. Reason : {response.json()}")

        return token


    def invokeRestApi(self, api_url, query_string, http_method, body):
        url = f"{api_url}{query_string}"

        headers = {
            "Accept": "application/*+json;version=34.0",
            "Authorization": f"Bearer {self.VCD_TOKEN}",
        }

        proxies = {"http": None, "https": None}

        response = requests.request(
            http_method,
            url,
            headers=headers,
            verify=False,
            proxies=proxies,
        )
        # print(response.status_code)

        if response.status_code == 200:
            print("Request invokeRestApi Successful. Getting details from response...")
        else:
            raise Exception(f"Request invokeRestApi Failed. Reason : {response.json()}")

        return response.json()


    def getVPCCustomers(self):
        vpc_customers = []
        url = self.VCD_HOST_URL
        qs = f"/api/query?type=adminOrgVdc&filter=metadata@SYSTEM:teluscloud.com/vdctype==STRING:vpc"

        result = self.invokeRestApi(url, qs, "GET", None)
        result = result['record']
        if len(result):
            print(f"Found {len(result)} VPC customer")
            vpc_customers = result
        else:
            print("No VPC customer found.")
            exit(0)

        return vpc_customers


    def getEdgeGateways(self, orgvdc_name):
        edge_gateways = []
        url = self.VCD_HOST_URL
        qs = f"/api/query?type=edgeGateway&filter=(orgVdcName=={orgvdc_name})"

        result = self.invokeRestApi(url, qs, "GET", None)
        result = result['record']
        if len(result):
            print(f"Found {len(result)} edgeGateys for {orgvdc_name}")
            # edge_gateways = result
            for ew in result:
                # print(ew.get("href"))
                url = ew.get("href")
                ew_result = self.invokeRestApi(url, "", "GET", None)
                edge_gateways.append(ew_result)
        else:
            print(f"No edgeGateways found for {orgvdc_name}.")

        return edge_gateways


    def getvdcStorageProfiles(self, vdc_name):
        vdcStorageProfiles = []
        url = self.VCD_HOST_URL
        qs = f"/api/query?type=adminOrgVdcStorageProfile&filter=(vdcName=={vdc_name})"

        result = self.invokeRestApi(url, qs, "GET", None)
        result = result['record']
        if len(result):
            print(f"Found {len(result)} adminOrgVdcStorageProfile for {vdc_name}")
            vdcStorageProfiles = result
            # for sp in result:
                # print(sp.get("href"))
                # url = ew.get("href")
                # ew_result = self.invokeRestApi(url, "", "GET", None)
                # vdcStorageProfiles.append(ew_result)
        else:
            print(f"No adminOrgVdcStorageProfile found for {vdc_name}.")

        return vdcStorageProfiles


    def getAllVMSinVDC(self, vdc):
        allVMS = []
        currentVdc = self.invokeRestApi(vdc['href'], '','GET', None)
        if  (not currentVdc):
            raise Exception("No vdc found.")

        if len(currentVdc['resourceEntities']['resourceEntity']):
            url = self.VCD_HOST_URL
            qs = f"/api/query?type=adminVM&filter=(vdc=={vdc.get('href')})"
            result = self.invokeRestApi(url, qs, "GET", None)
            if len(result["record"]):
                print(f"Found {len(result['record'])} vm for {vdc.get('name')}.")
                for vm in result["record"]:
                   vmResult = self.invokeRestApi(vm["href"],"","GET",None)
                   vmResult.__setitem__("status", vm["status"])
                   allVMS.append(vmResult)

        return allVMS


    def generateReportForVPCCustomers(self):
        VPC_CUSTOMERS = self.getVPCCustomers()
        for cust in VPC_CUSTOMERS:
            vdc_name = cust.get("name")
            print(f"Looking for vdc : {vdc_name}")
            ews = self.getEdgeGateways(vdc_name)
            cust.__setitem__("edgeGateways",ews)

            vdcSps = self.getvdcStorageProfiles(vdc_name)
            cust.__setitem__("storageProfile",vdcSps)

            vms = self.getAllVMSinVDC(cust)
            cust.__setitem__("vm",vms)

            self.REPORT_DATA.__setitem__("data", VPC_CUSTOMERS)

        return json.dumps(self.REPORT_DATA)



def handler(context, inputs):
    vcd_host = inputs["VCD_HOST"]
    vcd_username = inputs["USERNAME"]
    vcd_password = inputs["PASSWORD"]

    if (not vcd_host) or (not vcd_username) or (not vcd_password):
        raise Exception("NULL value provided for Inputs")
    
    obj = vCloudDirector(vcd_host, vcd_username, vcd_password)
    report_data = obj.generateReportForVPCCustomers()

    return report_data

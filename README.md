# vRO
###  vRO REST Authentication Methods

| Authentication Provider |	MiddleWare |	Access Scheme |	Encoding |
|-------------------------|-------------------------|------------------------------|-----------------------------|
| Active Directory	| LDAP |	HTTP Basic authentication	| base64-encoded user name and password |
| vSphere |	SSO |	Holder-of-key (HoK) token	| GZIP, base64-encoded string |
| vRA	| vIDM	| OAuth bearer access token	| Plain unreadable |

### vmwvro - A simple Python library to interface with VMware vRealize Orchestrator
https://pypi.org/project/vmwvro/

### vroParse - A Python library that parses scriptable tasks out of vRO Workflow XML, saves them as discrete files
https://pypi.org/project/vroParse/

### Ansible module for executing vRealize Orchestrator workflows
https://github.com/tonyskidmore/vmware_vro_workflow

============================================================================
# vRA

vRealize Automation API uses OpenAPI for all REST API service calls. How you access the API reference depends on the vRealize Automation version installed.

#### If vRealize Automation 7.6 or earlier is installed, go to https://$vRA/component-registry/services/docs, where $vRA denotes an instance of vRealize Automation.
#### If vRealize Automation 8.0 or later is installed, go to https://$vRA/automation-ui/api-docs, where $vRA is the hostname of your vRealize Automation appliance.

### vRA REST Methods <br>
https://github.com/vmware-archive/vra-api-samples-for-postman <br>
https://www.thehumblelab.com/vrealize-automation-api-with-python/ <br>
https://github.com/imtrinity94/postman-collections <br>


============================================================================
# vCD



| Revision Date	| Description	| Release Vehicle	| Status |
|----------------|----------------|------------------------|------------|
|9 Apr 2020	|API Version 34.0	|VMware Cloud Director 10.1	|supported|
|19 Sep 2019	|API Version 33.0	|vCloud Director 10.0	|supported|
|28 MAR 2019	|API Version 32.0	|vCloud Director 9.7	|supported|
|04 OCT 2018	|API Version 31.0	|vCloud Director 9.5	|supported|
|27 FEB 2018	|API Version 30.0	|vCloud Director 9.1	|supported|
|25 SEP 2017	|API Version 29.0	|vCloud Director 9.0	|deprecated|
|21 FEB 2017	|API Version 27.0	|vCloud Director 8.20	|deprecated|
|26 MAY 2016	|API Version 20.0	|vCloud Director 8.10	|not supported|
|N/A	|API Version 19.0 and earlier	|vCloud Air Compute Service	|not supported|

### pyvcloud - A Python SDK for VMware vCloud Director
https://pypi.org/project/pyvcloud/

X-VCLOUD-AUTHORIZATION: 08a321735de84f1d9ec80c3b3e18fa8b <br>
X-VMWARE-VCLOUD-ACCESS-TOKEN: eyJh...*long_text*....CX3iYWA <br>

The string after `X-VCLOUD-AUTHORIZATION:` is the old (deprecated) token <br>
The string after `X-VMWARE-VCLOUD-ACCESS-TOKEN` is the bearer token <br>


============================================================================
# vSphere

### pyVmomi - A Python SDK for the VMware vSphere API that allows you to manage ESX, ESXi, and vCenter.
https://pypi.org/project/pyvmomi/

### vmwc - Simplified VMWare API client for Python (based on pyVmomi)
https://pypi.org/project/vmwc/

## Use of Managed Object References by the vSphere Provider

Unlike the vSphere client, many resources in the vSphere take Managed Object IDs (or UUIDs when provided and practical) , which provides a stable interface for providing necessary data to downstream resources, in addition to minimizing the bugs that can arise from the flexibility in how an individual object's name or inventory path can be supplied.

There are several data sources (such as vsphere_datacenter, vsphere_host, vsphere_resource_pool, vsphere_datastore, and vsphere_network) that assist with searching for a specific resource.

### Locating Managed Object IDs
There are certain points in time that you may need to locate the managed object ID of a specific vSphere resource yourself. A couple of methods are documented below.

#### Via govc
govc is an vSphere CLI built on govmomi, the vSphere Go SDK. It has a robust inventory browser command that can also be used to list managed object IDs.

To get all the necessary data in a single output, use govc ls -l -i PATH. Sample output is below:

```go
$ govc ls -l -i /dc1/vm
VirtualMachine:vm-123 /dc1/vm/foobar
Folder:group-v234 /dc1/vm/subfolder
```
To do a reverse search, supply the -L switch:

```
$ govc ls -i -l -L VirtualMachine:vm-123
VirtualMachine:vm-123 /dc1/vm/foobar
```
For details on setting up govc, see the homepage.

#### Via the vSphere Managed Object Browser (MOB)
The Managed Object Browser (MOB) allows one to browse the entire vSphere inventory as it's presented to the API. It's normally accessed via [https://YOUR_VSPHERE_SERVER_FQDN_or_IP/mob](). For more information, see [here](https://code.vmware.com/doc/PG_Appx_Using_MOB.21.2.html#994699).

#### NOTE:
> The MOB also offers API method invocation capabilities, and for security reasons should be used sparingly. Modern vSphere installations may have the MOB disabled by default, at the very least on ESXi systems. For more information on current security best practices related to the MOB on ESXi, click [here](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.security.doc/GUID-0EF83EA7-277C-400B-B697-04BDC9173EA3.html).

============================================================================
# LogInsight

### pyloginsight - A Python SDK for LogInsight
https://pypi.org/project/pyloginsight/

============================================================================
# SRM

### SRM_client - A Python SDK for SRM
https://pypi.org/project/srm_client/

============================================================================
# Usage Meter

Usage Meter API uses Swagger UI for all REST API service calls. How you access the API reference depends on the Usage Meter version installed.

#### If Usage Meter 3.6 or earlier is installed, go to https://$um/um, where $um denotes an instance of Usage Meter.
#### If Usage Meter 4.2 or later is installed, go to https://$um/api/v1, where $um denotes an instance of Usage Meter.


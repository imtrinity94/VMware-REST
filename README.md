# vRO
###  vRO REST Authentication Methods

| Authentication Provider |	MiddleWare |	Access Scheme |	Encoding |
|-------------------------|-------------------------|------------------------------|-----------------------------|
| Active Directory	| LDAP |	HTTP Basic authentication	| base64-encoded user name and password |
| vSphere |	SSO |	Holder-of-key (HoK) token	| GZIP, base64-encoded string |
| vRA	| vIDM	| OAuth bearer access token	| Plain unreadable |

### vmwvro - A simple Python library to interface with VMware vRealize Orchestrator
https://pypi.org/project/vmwvro/

### vroParse - A Python library that parses scriptable tasks out of vRO Workflow XML, saves them as discrete files.
https://pypi.org/project/vroParse/

==============================================================================
# vRA

### vRA REST Methods <br>
https://github.com/vmware-archive/vra-api-samples-for-postman <br>
https://www.thehumblelab.com/vrealize-automation-api-with-python/ <br>
https://github.com/imtrinity94/postman-collections <br>


==============================================================================
#vCD

X-VCLOUD-AUTHORIZATION: 08a321735de84f1d9ec80c3b3e18fa8b <br>
X-VMWARE-VCLOUD-ACCESS-TOKEN: eyJh...*long_text*....CX3iYWA <br>

The string after `X-VCLOUD-AUTHORIZATION:` is the old (deprecated) token <br>
The string after `X-VMWARE-VCLOUD-ACCESS-TOKEN` is the bearer token <br>

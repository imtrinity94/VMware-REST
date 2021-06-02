vRO REST Authentication Methods

| Authentication Provider |	MiddleWare |	Access Scheme |	Encoding |
|-------------------------|-------------------------|------------------------------|-----------------------------|
| Active Directory	| LDAP |	HTTP Basic authentication	| base64-encoded user name and password |
| vSphere |	SSO |	Holder-of-key (HoK) token	| GZIP, base64-encoded string |
| vRA	| vIDM	| OAuth bearer access token	| Plain unreadable |



vRA REST Methods <br>
https://github.com/vmware-archive/vra-api-samples-for-postman
https://www.thehumblelab.com/vrealize-automation-api-with-python/

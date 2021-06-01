vRO REST Authentication Methods

| Authentication Provider |	MiddleWare |	Access Scheme |	Encoding |
|-------------------------|-------------------------|------------------------------|-----------------------------|
| Active Directory	| LDAP |	HTTP Basic authentication	| base64-encoded user name and password |
| vSphere |	SSO |	Holder-of-key (HoK) token	| GZIP, base64-encoded string |
| vRA	| vIDM	| OAuth bearer access token	| Plain unreadable |




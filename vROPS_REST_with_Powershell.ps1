<#Authentication
The most challenging part of working out how to use the API was how the authentication works. Essentially, you need to form the authentication URL, create a JSON formatted credential then obtain a session ID for the subsequent requests.

I have put all of this together in the below sample PowerShell code.

You’ll probably not want to store credentials in the script, so be sure to find an alternative way to obtain the password (via Read-Host or a call to your password database API
#>
## Global Variables
$vrops_server = ""
$vrops_username = ""
$vrops_password = ""

## Ignore SSL Certificates
add-type @"
    using System.Net;
    using System.Security.Cryptography.X509Certificates;
    public class TrustAllCertsPolicy : ICertificatePolicy {
        public bool CheckValidationResult(
            ServicePoint srvPoint, X509Certificate certificate,
            WebRequest request, int certificateProblem) {
            return true;
        }
    }
"@
[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy

## vROps API Strings
$rest_url_base = "https://" + $vrops_server + "/suite-api/api/"
$rest_url_authenticate = "https://" + $vrops_server + "/suite-api/api/auth/token/acquire"

## Create JSON for Authentication
$json_authentication =
"{
  ""username"": ""$vrops_username"",
  ""password"": ""$vrops_password""
}"

## Authenticate with vROPs REST API
Try {
    $rest_authenticate = Invoke-RestMethod -Method POST -Uri $rest_url_authenticate -Body $json_authentication -ContentType "application/json"
}
Catch {
    $_.Exception.ToString()
    $error[0] | Format-List -Force
    exit
}

## Get Session ID from response
$rest_authentication_session_xml = @{"Authorization"="vRealizeOpsToken "+$rest_authenticate.'auth-token'.token 
"Accept"="application/xml"}
Get Email Plugins
Once you have authenticated to the API, you can use the $rest_authentication_session_xml variable, containing the Session ID for subsequent requests.

The next code snippet will output all configured vROps email plugins

$rest_url_email_plugins = $rest_url_base+"alertplugins"
Try {
  $ResourcesXML = Invoke-RestMethod -Method GET -Uri $rest_url_email_plugins -Headers $rest_authentication_session_xml
  $plugins = $ResourcesXML.'notification-plugins'.'notification-plugin'


  Write-Host "Available Email Plugins:" -ForegroundColor Blue
  $plugin_id_array=@()
  foreach ($plugin in $plugins ) {
   
    if($plugin.pluginTypeId -ne "StandardEmailPlugin"){
      continue;
    }
   
    $plugin_id_array += $plugin.pluginId
    Write-Host "Plugin Name:" $plugin.name " | Plugin ID" $plugin.pluginId  -ForegroundColor White
  }
}
Catch {
  $_.Exception.ToString()
  Write-Host "Error getting email plugins. Exiting" -ForegroundColor Red
  exit
}
Get Remote Collectors
Next, you can amend the above code snippet to get all configured remote collectors

$rest_url_remote_collectors = $rest_url_base+"collectors
Try {
  $ResourcesXML = Invoke-RestMethod -Method GET -Uri $rest_url_remote_collectors -Headers $rest_authentication_session_xml

  $collectors = $ResourcesXML.'collectors'.'collector'

  Write-Host "Available Remote Collectors:" -ForegroundColor Blue
  $collector_uuid_array=@()

  foreach ($collector in $collectors) {
    $collector_uuid_array += $collector.uuId
    Write-Host  "Remote Collector Name:" $collector.name " | Collector ID" $collector.uuId
  }
}
Catch {
    $_.Exception.ToString()
    Write-Host "Error getting remote collectors. Exiting" -ForegroundColor Red
    exit
  }
Get Notification Rules
As with the other code snippets, you can use the API to obtain all the notification rules:

$rest_url_notification_rules = $rest_url_base+"notifications/rules"

Try {
  $NotificationXML = Invoke-RestMethod -Method GET -Uri $rest_url_notification_rules -Headers $rest_authentication_session_xml
  $notification_rules = $NotificationXML.'notification-rules'.'notification-rule'
  Write-Host "Available Notification Rules:"  -ForegroundColor Blue

  foreach ($notification_rule in $notification_rules) {
    Write-Host  $notification_rule.name
  }
}

Catch {
    $_.Exception.ToString()
    Write-Host "Error getting notification rules. Exiting" -ForegroundColor Red
    exit
}
Official Documentation
Once you have tried the above examples, check out the official documentation by appending /suite-api/doc/swagger-ui.html to the end of your vROps install FQDN.

This will open the vRealize Operations Manager API site and give you all the available API commands which you can substitute in the above code examples.

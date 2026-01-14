# soapInject
A simple py script that allows you to send custom SOAP packets with your own payloads

# Libraries
requests

# Ethical Notice
This script and lab are intended strictly for educational and research purposes. It should only be used on devices you own or have explicit permission to test. Unauthorized use on networks or devices without permission is illegal and unethical. Please practice responsible and ethical cybersecurity.

# Getting Started
To run type<br>
python3 soapCheck.py

# What do I type in ?
Example of usable ip for this script<br>
192.168.0.1, 10.0.0.1 ...etc

Example of usable port for this script<br>
5431, 1900, 80 ...etc

Example of usable payload for this script<br>
%x, %s ...etc

Example of usable uuid for this script<br>
uuid:0018-f8d7-a07102009adc

Example of usable target service for this script<br> 
WANIPConnection:1

Once done soapCheck concats your inputs into a URL and it should look like this<br>
http://192.168.0.1:5431/uuid:0018-f8d7-a07102009adc/WANIPConnection:1

# Extra's
linksysPentest.txt - An ethical vulnerability assessment on a device I own, use this as a reference to use the tool for your own ethical assessments!<br>
xmlExample.txt - A sample XML I gathered when testing, use it as a reference if you get lost when testing.

# Important
If targeting a similar device remember than in order to view the format string vulnerability you must first send your specifier to the module that sets the connection type (you should see code 200!)
and to be able to see if vulnerable you must call the get connection type module, you will then see a memory address.<br>
Use the "gupnp-universal-cp" command to initilize the UPNP connection, after this you can run the soapCheck.py script!

# Troubleshooting
Make sure requests library is imported correctly<br>
If soapCheck.py "freezes" it likely cannot reach the IP address provided make sure the IP address provided is on your network.<br>
Use Wireshark to review network traffic, to confirm soapCheck.py is sending packets<br>
Firewalls can block incoming and outgoing requests... so keep that in mind.<br>
Packet headers may need to be modified manually depending on the module you are targeting.

# Updates
Coming soon ...

Dynamic packet headers<br>
Dynamic module options




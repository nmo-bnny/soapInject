# soapInject
A simple py script that allows you to send custom SOAP packets with your own payloads

# Libraries
requests

# Ethical Notice
This script and lab are intended strictly for educational and research purposes. It should only be used on devices you own or have explicit permission to test. Unauthorized use on networks or devices without permission is illegal and unethical. Please practice responsible and ethical cybersecurity.

# Getting Started
To run type
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

# Troubleshooting
Make sure requests library is imported correctly
If soapCheck.py "freezes" it likely cannot reach the IP address provided make sure the IP address provided is on your network.  
Use Wireshark to review network traffic, to confirm soapCheck.py is sending packets
Firewalls can block incoming and outgoing requests... so keep that in mind.



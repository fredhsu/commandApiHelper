import json
from jsonrpclib import Server
from collections import namedtuple

switchIP = "192.168.56.200"
username = "fhsu"
password = "arista"
urlString = "https://{}:{}@{}/command-api".format(username, password, switchIP)
switch = Server( urlString )
class Interface:
    """ Ethernet Interface """
    def __init__(self, name=""):
        self.name = name
        self.attributes = []

    def setIpAddress(self, ipAddr):
        # could check if routed port, raise error or proceed
        # remove no switchport
        response = switch.runCmds( 1, ["enable", "configure", "interface " + self.name, "no switchport", "ip address " + ipAddr])
        print response

    def setVlan(self, vlan):
        # Check if switchport, raise error or proceed
        response = switch.runCmds( 1, ["enable", "configure", "interface " + self.name, "no switchport", "ip address " + ipAddr])
        print response

    def setTrunk(self):
        # Change mode to trunk

        
class AristaSwitch:
    """Switch class"""
    def __init__(self):
        self.data = []
        self.interfaces = []



response = switch.runCmds( 1, ["show version"] )
print "The switch's system MAC addess is", response[0]["systemMacAddress"]
print response[0]

print "object "
d = namedtuple('Version', response[0].keys())(*response[0].values())
print d
response = switch.runCmds( 1, ["show interfaces"] )
print "---"
#print response[0]
#for key, value in response[0]["interfaces"].iteritems():
#    print key 
#    print value
iface = Interface()
iface.setIpAddress("1.1.1.1/24")

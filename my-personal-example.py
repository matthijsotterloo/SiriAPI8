from SiriAPI8.SiriAPI8.SiriAPI import *

###############################################################################################
#         This is the configuration I use with my self build home automation system           #
# It uses a HTTP API to switch the light. The HTTP request is defined in the request function #
#         Lamps are loaded using a json request and compared with the detected input          #
###############################################################################################

import urllib.request
import json

def request (url): #HTTP request
    f = urllib.request.urlopen(url)
    return(f.read().decode('utf-8'))

def licht_toggle(q, wildcards):
    #Prozessverarbeitung
    receivers = json.loads(request("http://zimmer:2525/remote/list")) #JSON request
    found = False
    for id, val in enumerate(receivers):
        if (receivers[val]['title'].lower() == wildcards[0]):
            found = True
            request("http://zimmer:2525/remote/switch?id=" + str(val))


    if (found == False):
        print("I don't recognize this lamp")
    else:
        print("I changed the lamp")


SiriAPI = SiriAPI("my-email@me.com", "MyPassword")

SiriAPI.action.add([['zet de', '*']], licht_toggle)

print ("Siri API Version: " + SiriAPI.get_version())
SiriAPI.connect()
input("Press any key to exit...\n")
SiriAPI.disconnect()

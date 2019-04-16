import json
import urllib
import os

#this is the url to the authentication string generator script
url = "https://c1xjvd8g52.execute-api.us-west-2.amazonaws.com/dev/users/create?whoami="
#This above value is the Auth url

with open("/Library/VMware/Notify/my_text_file.txt") as txt:
    data = txt.readline()
    url = url+data


auth = {}
    
#we have to declare the exact path or the permissions get a little upset
with open("/Library/VMware/Notify/resources/Config.json", "r") as jsonFile:
    data = json.load(jsonFile)

response = urllib.urlopen(url) #this opens up the url to get the auth string from the server.
auth = json.loads(response.read())
#print auth['Auth']
data["Auth"] = auth['Auth'] #this is the value that saves the auth string on the device

with open("/Library/VMware/Notify/resources/Config.json", "w") as jsonFile:
    json.dump(data, jsonFile) #this dumps the info onto the config file.

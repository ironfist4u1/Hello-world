def promptOG():
    box=[]
    box.append('case $ANSWER in\n')
    box.append('"@TIMEOUT") echo "Timeout man, sorry" ;;\n')
    box.append('"@CLOSED") echo "You clicked on the default alert close button" ;;\n')
    box.append('"@CONTENTCLICKED") echo "You clicked the alert content !" ;;\n')
    box.append('"@ACTIONCLICKED") echo "You clicked the alert default action button" ;;\n')
    box.append('"Read Later") echo "Action LATER" ;;\n')
    box.append('"Dismiss") echo "Action DISMISS" ;;\n')
    box.append('"Read Now") echo "Action MORE" ;;\n')
    box.append('**) echo "? --> $ANSWER" ;;\n')
    box.append('esac\n')
    return box

def openf(abpath,rights): #opens the file we need for this
    
    content = open(abpath,rights)
    return content

def whoami(): # this function is used to run a command to get the username of the usert
    #os.popen("whoami > my_text_file.txt")
    commands = "dscl . list /Users | grep -v '_' | grep -v 'administrator' | grep -v 'daemon' | grep -v 'nobody' | grep -v 'root' | grep -v 'mfe' > my_text_file.txt"
    os.popen(commands)
    text = openf('my_text_file.txt','r')
    line = text.readline()
    line = line[:-1]
    text.close()
    #os.popen("system_profiler SPHardwareDataType | grep Serial > my_text_file.txt")
    #text = openf('my_text_file.txt','r')
    #line = line + text.readline()
    #text.close()
    return line

def writesh(path,title,sub,message): #this launches the SH script, appends the lines of the response to a box, and then also returns that
    sh = open(path,'w+')
    box2 = promptOG()
    #ANSWER="$(~/Documents/Note-app-alerts/alerter -title 'AirWatch Update' -subtitle 'Click here to see latest update' -message 'Click here to see latest update' -closeLabel Dismiss -actions More,Later)"
    #-appIcon http://vjeantet.fr/images/logo.png
    icon = "64@1x.png"
    note = 'ANSWER="$($MYDIR/alerter -title ' +"'"+title+"' -subtitle '" + sub + "' -message '" + message +"'"+ ' -closeLabel "Read Now" -actions "Dismiss","Read Later")"\n'
    #note = note+" -appIcon $MYDIR/Picture1.png \n"
    box = []
    statement = "#!/bin/sh\n"
    runner = 'MYDIR="$(dirname "$(which "$0")")"\n'
    box.append(statement)
    box.append(runner)
    box.append(note)
    for i in range(0,len(box2)):
        box.append(box2[i])

    sh.writelines(box)
    sh.close()


#need to make function for the actual pop up.
def posting(path, title,sub,message):
    writesh(path, title,sub,message)
    os.popen("sh promptre.sh > my_text_file.txt")
    text = openf('my_text_file.txt','rw')
    line = text.readline()
    return line

#this function is used to return the proper response after the user has clicked something.
def returning(line,link,title,sub,message,update):
    count = 0
    with open('Config.json') as getter:
        data = json.load(getter)
        count = int(data['Later'])
    while count <= 3:
        if line.find('MORE')>0 and count < 3: #if more button is clicked
            webbrowser.open(link)
            with open('Config.json') as f: #this loads up the config
                data = json.load(f) #reads the config into json
                auth = data['Auth']
                url = data['Post'] + '?button=MORE&whoami='+whoami()+'&version='+str(update)+"&auth="+auth #makes a url string 
                response = urllib.urlopen(url) #opens the url in a hidden http call.
                #print response.read()
                break
            break
        
        elif line.find('DISMISS') >0 and count < 3: #if dismissed button is clicked
            with open('Config.json') as f:
                data = json.load(f)
                auth = data['Auth']
                url = data['Post'] + '?button=DISMISS&whoami='+whoami()+'&version='+str(update)+"&auth="+auth
                response = urllib.urlopen(url)
                #print response.read()
                break
            break
        
        elif line.find('LATER')>0 and count < 3: #if later button is clicked
            count = count +1
            with open('Config.json') as getter:
                data = json.load(getter)
                data['Later'] = str(count)
            with open("Config.json", "w") as jsonFile:
                json.dump(data, jsonFile) #this dumps the info onto the config file.
                break
            break
            
        elif line.find("alert's content") > 0 and count < 3: #if the content box is clicked
            webbrowser.open(link)
            with open('Config.json') as f:
                data = json.load(f)
                auth = data['Auth']
                url = data['Post'] + '?button=MORE&whoami='+whoami()+'&version='+str(update) +"&auth="+auth
                response = urllib.urlopen(url)
                #print response.read()
                break
            break
        
        elif count == 3:
            #send the action of later was picked more than X times.
            with open('Config.json') as f:
                data = json.load(f)
                auth = data['Auth']
                data['Later']=str(0)
                url = data['Post'] + '?button=LATER&whoami='+whoami()+'&version='+str(update) +"&auth="+auth
                response = urllib.urlopen(url)
                #print response.read()
            with open("Config.json", "w") as jsonFile:
                json.dump(data, jsonFile) #this dumps the info onto the config file.
                break
            break
            
#print line

#add to the main while loop to make it take in the lambda return and see if the update actually needs to be posted.

import os
import sys

#needed to use json files
import json

#webbrowser is used to open links. While urllib is used to open links without a window.
import webbrowser
import urllib
import time




#this generates a job so we chan schedule the task.
def job():

    auth = ""
	#opens the config file as f
    with open('Config.json') as f:
        data = json.load(f)
        auth = data['Auth']
        url = data['Get'] +"?auth="+auth+"&whoami="+whoami() #we grab the get url from the config file
        response = urllib.urlopen(url) #opens the url which still a web object
        try:
            data = json.loads(response.read())	#this turns it into a read, then parses out the json part.
        except:
        #print "failed"
            pass
	
	
        error = None
        try: 
            #this try is becuase if the get link was successful then it will setup all the information
            title = data['Title']
            sub = data['Version']
            message = data['Message']
            link = data['Link']
            update = data['UpdateID']
            line = "Already updated"
        except:
            #this is for if the get link failed. Then we will throw that error.
            error = data['Error']


    with open('Config.json') as f:
        data = json.load(f)
        url = data['checker'] +"?whoami="+whoami()+"&updateID="+str(update)+"&auth="+auth
        checked = urllib.urlopen(url)
        isSeen = checked.read()

        #print isSeen



    if isSeen.find("True") < 0 and error == None: #makes sure there is no errors and that the user hasn't seen the update yet.
        line = posting("promptre.sh",title,sub,message)
        returning(line,link,title,sub,message,update)
    

#print line


job()

sys.exit()

#webbrowser.open('http://example.com')

    


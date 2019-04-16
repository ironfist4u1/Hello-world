import json
import urllib

### This is the admin script url change this for using admin scripts
url = "https://x7eqyqw34m.execute-api.us-west-2.amazonaws.com/dev/users/create"
###



def logic(com,url):
    if com == "readStatus":
        url = url+"?input="+com #makes a url string\
        response = urllib.urlopen(url) #opens the url in a hidden http call
        holder = json.loads(response.read())
        print "Would you like to search this information?"
        rep = raw_input("Enter the user name or !no ")
        if rep.find('!no')<0:
            for row in holder:
                if row[1] == rep:
                    print row
        else:
            for row in holder:
                print row
            
    elif com == "readControlU":
      url = url+"?input="+com #makes a url string 
      response = urllib.urlopen(url) #opens the url in a hidden http call.
      holder = json.loads(response.read())
      for row in holder:
            print row

    elif com == "readAuth":
        url = url+"?input="+com #makes a url string
        response = urllib.urlopen(url) #opens the url in a hidden http call.
        holder = json.loads(response.read())
        print "Would you like to search this information?"
        rep = raw_input("Enter the user name or !no ")
        if rep.find('!no')<0:
            for row in holder:
                if row[1] == rep:
                    print row
        else:
            for row in holder:
                print row

    elif com == "deleteStatus":
      print "Picked to delete a user out of the status table."
      print "To use this we will need the username or the who that got stored."
      print "Then will also need the version that the user saw."
      ver = raw_input("Version: ")
      whoami = raw_input("username: ")
  
      url = url+"?input=deleteStatus&version="+ ver + "&whoami="+ whoami#makes a url string 
      response = urllib.urlopen(url) #opens the url in a hidden http call.
      holder = json.loads(response.read())
      print holder

    elif com == "deleteAuth":
        print "Picked to delete a user out of the auth table."
        print "To use this we will need the username"
        print "Then this will remove their entire list of auth strings from the table."
        whoami = raw_input("username: ")
                
        url = url+"?input=deleteAuth&whoami="+ whoami#makes a url string
        response = urllib.urlopen(url) #opens the url in a hidden http call.
        holder = json.loads(response.read())
        print holder

    elif com == "deleteControlU":
      print "Picked to delete an update out of the controlU table."
      print "To use this we will need the Title of the update that got stored."
      print "Then will also need the version of the update."
      ver = raw_input("Version: ")
      title = raw_input("Title: ")
      url = url+"?input=deleteControlU&version="+ ver + "&title="+ title#makes a url string 
      response = urllib.urlopen(url) #opens the url in a hidden http call.
      holder = json.loads(response.read())
      print holder

    elif com == "updateStatus":
      print "Picked to add a user to the status table."
      print "To use this we will need the username or the who that will get stored."
      print "Then will also need the version that the user saw."
      print "Then we need what button was pressed."
      ver = raw_input("Version: ")
      whoami = raw_input("username: ")
      button = raw_input("Button: ")
      
      url = url+"?input=updateStatus&version="+ ver + "&whoami="+ whoami+"&button="+button#makes a url string 
      response = urllib.urlopen(url) #opens the url in a hidden http call.
      holder = json.loads(response.read())
      print holder
    elif com == "updateControlU":
      print "Picked to add an update to the controlU table."
      print "To use this we will need the Title"
      print "Then will also need the version."
      print "Then we need the message."
      print "Also need the link to the update."
      print "You will also need to pick if all Windows, Mac, or VMware"
      ver = raw_input("Version: ")
      title = raw_input("title: ")
      message = raw_input("message: ")
      link = raw_input("Link: ")
      device = raw_input("Device: ")
      url = url+"?input=updateControlU&version="+ ver + "&title="+ title+"&message="+message+"&link="+link+"&device="+device#makes a url string
      response = urllib.urlopen(url) #opens the url in a hidden http call.
      holder = json.loads(response.read())
      print holder


    elif com == "updateAuth":
        print "Picked to add a user to the auth table."
        print "To use this we will need the username or the who that will get stored."
        print "This will return the auth string for this user name"
        whoami = raw_input("username: ")
        
        url = "https://c1xjvd8g52.execute-api.us-west-2.amazonaws.com/dev/users/create"
        url = url + "?whoami="+whoami
        response = urllib.urlopen(url) #opens the url in a hidden http call.
        holder = json.loads(response.read())
        print holder

        
    elif com == "rdsConfig":
      print "This is rds config of the get and post scripts."
      print "This will need the DB name, user, password, and link for the RDS server."
    
      link = raw_input("Link: ")
      DBname = raw_input("Database name: ")
      user = raw_input("user: ")
      password = raw_input("password: ")
      url = url+"?input=rdsConfig&link="+ link + "&DBname="+ DBname+"&user="+user+"&password="+password#makes a url string 
      response = urllib.urlopen(url) #opens the url in a hidden http call.
      holder = json.loads(response.read())
      print holder
          
    elif com == "rdsConfigSelf":
      print "This is rds config of the admin script."
      print "This will need the DB name, user, password, and link for the RDS server."
      link = raw_input("Link: ")
      DBname = raw_input("Database name: ")
      user = raw_input("user: ")
      password = raw_input("password: ")
    
      url = url+"?input=rdsConfigSelf&link="+ link + "&DBname="+ DBname+"&user="+user+"&password="+password#makes a url string 
      response = urllib.urlopen(url) #opens the url in a hidden http call.
      holder = json.loads(response.read())
      print holder
        
    elif com == "urlConfig":
      print "This configures the urls in the admin script."
      print "This needs the url for the get and post scripts."
      get = raw_input("get: ")
      post = raw_input("post: ")
      
      url = url+"?input=urlConfig&post="+ post + "&get="+ get#makes a url string 
      response = urllib.urlopen(url) #opens the url in a hidden http call.
      holder = json.loads(response.read())
      print holder



    elif com == "CreateTable": #I dont list this one since its not a command one should use alot.
      print "This creates a table in the rds server."
      print "This needs the table name and columns you want."
      print "To quit the column adding type !!quit!!"
      table = raw_input("table: ")
      holder = []
      inner = raw_input("Column: ")

      while inner != "quit": #makes a list to hold all the columns
        if inner != "!!quit!!":
          holder.append(inner)
          inner = raw_input("Column: ")

      colnum = 1
      delivery = []
      for col in holder: #makes a dirct to change the strings to a json format
        delivery.append({"colnum"+str(colnun):'"'+col+'"'})

      delivery.append({"tableName":table}) #appends the tablename at the end

      delivery = json.dumps(delivery) #converts the type to json
      
      url = url+"?input=createTable&holder="+ delivery #makes a url string 
      response = urllib.urlopen(url) #opens the url in a hidden http call.
      messager = json.loads(response.read())
      print messager #prints the server response.

    elif com == "DeleteTable": #I dont list this one since its not a command one should use alot.
      print "This delete a table in the rds server."
      print "This needs the table name"
      yousure = raw_input("Are you sure you want to delete a table?: yes/no\n")
      
      if yousure == "yes":
        table = raw_input("table: ")
        delivery = []
        delivery.append({"tableName":table}) #appends the tablename at the end
        delivery = json.dumps(delivery) #converts the type to json
        
        url = url+"?input=deleteTable&holder="+ delivery #makes a url string 
        response = urllib.urlopen(url) #opens the url in a hidden http call.
        messager = json.loads(response.read())
        print messager #prints the server response.



com = "enter"
while com != "quit":
  print "This is the lambda admin script"
  print "This is used to manage the rds configs in the different lambdas."
  print "Also allows to print the different tables, and update tables."
  print "Displaying all the input commands enter which one you wish to use\n"
  
  #input has many different commands.
  #readStatus
  #readControlU
  #deleteStatus
  #deleteControlU
  #updateStatus
  #updateControlU
  #rdsConfig
  #rdsConfigSelf
  #urlConfig
  #CreateTable
  #DeleteTable
  #readAuth
  #updateAuth
  #deleteAuth
  
  #this is the list of input commands.
  #will break down these inputs when coming to each one.

  commands = ["readStatus","readControlU","deleteStatus","deleteControlU","updateStatus","updateControlU","rdsConfig","rdsConfigSelf","urlConfig"]
  commands.append("CreateTable")
  commands.append("DeleteTable")
  commands.append("readAuth")
  commands.append("updateAuth")
  commands.append("deleteAuth")
  
  for row in commands:#print the commands the user needs to enter.
      print row
  print "Enter quit to leave the script"
  com = raw_input("Enter command: ")
  if com != "quit":#puts the logic into a function and the wait.
    logic(com,url)
    raw_input("\n\n\n Press Enter to contine")#to wait for user

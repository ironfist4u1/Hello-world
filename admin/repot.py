import json
import rds_config
import urllib
import logging
import pymysql

logger = logging.getLogger()
logger.setLevel(logging.INFO)
rds_host = rds_config.host
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

def response(message, status_code,event):
    getinput = event['queryStringParameters']['input']
    if(status_code==200) and getinput == 'updateControlU':
        version = message[2]
        Title = message[0]
        Message = message[1]
        Link = message[3]
        
        tunnel = {"Version" : version,"Title" : Title,"Message": Message,"Link": Link,"Success":"Committed these items to controlU table",}
        final = json.dumps(tunnel)
        
        return {
            "statusCode" : status_code,
            "body" : final,
            }
    elif(status_code==200) and getinput == 'updateStatus':
        whoami = message[1]
        button = message[0]
        version = message[2]
        
        
        tunnel = {"Version" : version,"Who" : whoami,"Button": button,"Success":"Committed these items to status table",}
        final = json.dumps(tunnel)
        
        return {
            "statusCode" : status_code,
            "body" : final,
            }
    
    elif(status_code==200) and getinput == 'readControlU':
        
        final = json.dumps(message)
        
        return {
            "statusCode" : status_code,
            "body" : final,
            }
    elif(status_code==200) and getinput=='readStatus':
        
        final = json.dumps(message)
        
        return {
            "statusCode" : status_code,
            "body" : final,
            }
    
    else:
        
        return {
            "statusCode" : status_code,
            "body" : json.dumps(message)
        }

def deleteControlU(box,event):
    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, port=3306,connect_timeout=3)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        #print("test")
        return response("Error: Can not connect to the server",404,event)
        sys.exit()
    with conn.cursor() as cur:
        try:
            cur.execute("delete from controlU where verID='"+box[1]+"' and title='"+box[0]+"'")
            conn.commit()
            return response(box,200,event)
        except:
            logger.error("ERROR: Unexpected error: Could not delete from status table.")
            #print("test")
            return response("Error: Can not connect to the server",404,event)
            sys.exit()
                
                

def deleteAuth(box,event):
    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, port=3306,connect_timeout=3)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        #print("test")
        return response("Error: Can not connect to the server",404,event)
        sys.exit()
    with conn.cursor() as cur:
        try:
            cur.execute("delete from auth where whoami='"+box[0]+"'")
            conn.commit()
            return response(box,200,event)
        except:
            logger.error("ERROR: Unexpected error: Could not delete from auth table.")
            #print("test")
            return response("Error: Can not connect to the server",404,event)
            sys.exit()
            
                
def deleteStatus(box,event):
    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, port=3306,connect_timeout=3)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        #print("test")
        return response("Error: Can not connect to the server",404,event)
        sys.exit()
    with conn.cursor() as cur:
        try:
            cur.execute("delete from status where whoami='"+box[0]+"' and version='"+box[1]+"'")
            conn.commit()
            
            return response(box,200,event)
        except:
            logger.error("ERROR: Unexpected error: Could not delete from status table.")
            #print("test")
            return response("Error: Can not connect to the server",404,event)
            sys.exit()
            
            
def updateStatus(box,event):
    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, port=3306,connect_timeout=3)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        #print("test")
        return response("Error: Can not connect to the server",404,event)
        sys.exit()
    with conn.cursor() as cur:
        try:
            cur.execute("insert into status (whoami, Button, Version) values("+"'"+box[1]+"'"+", "+"'"+box[0]+"'"+","+"'"+box[2]+"'"+")")
            conn.commit()
            return response(box,200,event)
        except:
            return response("Error: intake failed", 405,event)
            
def updateAuth(box,event):
    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, port=3306,connect_timeout=3)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        #print("test")
        return response("Error: Can not connect to the server",404,event)
        sys.exit()
    with conn.cursor() as cur:
        try:
            cur.execute("insert into auth (whoami, authString, device) values("+"'"+box[0]+"'"+", "+"'"+box[1]+"', '"+box[2]+"')")
            conn.commit()
            return response(box,200,event)
        except:
            return response("Error: intake failed", 405,event)
            
            
def updateControlU(box,event):
    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, port=3306,connect_timeout=3)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        #print("test")
        return response("Error: Can not connect to the server",404,event)
        sys.exit()
    with conn.cursor() as cur:
        built = "'"+box[2]+"', "+"'"+box[0]+"', '"+box[1]+"', '"+box[3]+"', '"+box[4]+"'"
        cur.execute("insert into controlU (VerID, Title,Message,Link,device) values("+built+")")
        conn.commit()
        return response(box,200,event)
        
            
def readStatus(event):
    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, port=3306,connect_timeout=3)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        #print("test")
        return response("Error: Can not connect to the server",404,event)
        #sys.exit()
    with conn.cursor() as cur:
        cur.execute("select * from status")
        #cur.execute("SELECT * FROM controlU ORDER BY VerID DESC LIMIT 1")
        #print("Value1 = " + Event.get('key1'))
        box = []
        for row in cur:
            #logger.info(row)
            box.append(row)
        logger.info(box)

        return response(box,200,event)
        
        
def readAuth(event):
    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, port=3306,connect_timeout=3)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        #print("test")
        return response("Error: Can not connect to the server",404,event)
        sys.exit()
    with conn.cursor() as cur:
        cur.execute("select * from auth")
        #cur.execute("SELECT * FROM controlU ORDER BY VerID DESC LIMIT 1")
        #print("Value1 = " + Event.get('key1'))
        box = []
        for row in cur:
            #logger.info(row)
            box.append(row)
        logger.info(box)

        return response(box,200,event)
            
            
def readControlU(box,event):
    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, port=3306,connect_timeout=3)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        #print("test")
        return response("Error: Can not connect to the server",404,event)
        sys.exit()
    with conn.cursor() as cur:
        #cur.execute("select * from status")
        cur.execute("SELECT * FROM controlU ORDER BY ID DESC LIMIT 1")
        #cur.execute("SELECT * FROM controlU")
        #print("Value1 = " + Event.get('key1'))
        box = []
        for row in cur:
            #logger.info(row)
            box.append(row)
        logger.info(box)
    
        return response(box,200,event)
            
            
def rdsConfig(box,event):
    rds = "?link=" + box[0] +"&DBname="+box[1]+"&user="+box[2]+"&password="+box[3]
    geturl = rds_config.get + rds
    posturl = rds_config.post + rds
    checkurl = rds_config.check + rds
    table = urllib.urlopen(geturl) #opens the url in a hidden http call.
    replyget= table.read()
    table = urllib.urlopen(posturl) #opens the url in a hidden http call.
    replypost= table.read()
    table= urllib.urlopen(checkurl)
    replycheck= table.read()
    
    body = {
    "get": replyget,
    "post": replypost,
    "check": replycheck
    }
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    
def rdsConfigSelf(box,event):
    rds_config.db_username = box[2]
    rds_config.db_password = box[3]
    rds_config.db_name = box[1]
    rds_config.host = box[0]
    return {
        "statusCode": 200,
        "body": "Success: rds was updated on the admin script"
        }
        
        
def urlConfig(box, event):
    rds_config.get = box[0]
    rds_config.post = box[1]
    rds_config.check = box[2]
    return {
        "statusCode": 200,
        "body": "Success: urls was updated on the admin script"
        }
        
        
def createTable(box,event):
    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, port=3306,connect_timeout=3)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        #print("test")
        return response("Error: Can not connect to the server",404,event)
        sys.exit()
    with conn.cursor() as cur:
        #built = "'"+box[2]+"', "+"'"+box[0]+"', '"+box[1]+"', '"+box[3]+"'"
        #cur.execute("insert into controlU (VerID, Title,Message,Link) values("+built+")")
        #conn.commit()
        counter = box[0]-1
        tablename = box[0][counter]["table"]
        box[0].pop(counter)
        prime = box[0][0]["colnum1"]
        box[0].pop(0)
        box = box.pop(0)
        
        
        try:
            cur.execute("create table "+tablename+" ( "+prime+" varchar(255) NOT NULL, PRIMARY KEY ("+prime+"))")
            conn.commit()
            count = len(box)
            i = 0
            while i < count:
                for col in box[i]:
                    excuter = "ALTER TABLE "+tablename+" ADD "+box[i][col]+" varchar(255)"
                    cur.execute(excuter)
                    conn.commit
                i = i +1
        except:
            logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
            #print("test")
            return response("Error: Can not make the Table",502,event)
            
        body = {
            "Success": "Created table with table name: "+tablename
        }
        return {
            "statusCode": 200,
            "body": json.dumps(body)
        }

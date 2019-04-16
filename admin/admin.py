import json
import rds_config
import urllib
import logging
import pymysql
import repot
import parsing

#this is the function lambda calls
def controller(event, context):
    box = []
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    rds_host = rds_config.host
    name = rds_config.db_username
    password = rds_config.db_password
    db_name = rds_config.db_name
    
    try:
        getinput = event['queryStringParameters']['input']
    except:
        logger.error("Error: input was not provided")
        body = {
            "Error": "input was not provided"
        }
        return {
            "statusCode": 405,
            "body": json.dumps(body)
        }
        sys.exit()
    
    if getinput != 'readStatus' and getinput != 'readControlU' and getinput !='readAuth':
        try:
            box = parsing.parse(box,event)
        except:
            logger.error("Error: input was not provided")
            body = {
            "Error": "input was not provided"
            }
            return {
                "statusCode": 405,
                "body": json.dumps(body)
            }
            sys.exit()
    
    
    
    if getinput == 'deleteStatus':
        return repot.deleteStatus(box,event)
            
    elif getinput == 'deleteControlU':
        return repot.deleteControlU(box,event)
        
    elif getinput == 'deleteAuth':
        return repot.deleteAuth(box,event)
    
    elif getinput == 'updateStatus':
        return repot.updateStatus(box,event)
    
    elif getinput == 'updateControlU':
        return repot.updateControlU(box,event)
        
    elif getinput == 'updateAuth':
        return repot.updateAuth(box,event)
       
    elif getinput == 'readStatus':
        return repot.readStatus(event)
        
    elif getinput == 'readAuth':
        return repot.readAuth(event)
        
    elif getinput == 'readControlU':
        return repot.readControlU(box,event)
        
    elif getinput == 'rdsConfig':
        return repot.rdsConfig(box,event)
        
    elif getinput == 'rdsConfigSelf':
        return repot.rdsConfigSelf(box,event)
       
    elif getinput == 'urlConfig':
        return repot.urlConfig(box,event)
        
    elif getinput == "createTable":
        return repot.createTable(box,event)

#be able to change table controlU via here.
#be able to change table status via here.
#be able to change the rds_config of others here.
#change rds config on this script via itself.
#return if any of these commands were succesful
#take in different inputs to achive this.

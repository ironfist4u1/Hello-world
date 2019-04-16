def parse(box,event):
    getinput = event['queryStringParameters']['input']
    
    if getinput == 'updateStatus':
        box.append(event['queryStringParameters']['button'])
        box.append(event['queryStringParameters']['whoami'])
        box.append(event['queryStringParameters']['version'])
    elif getinput == 'updateControlU':
        box.append(event['queryStringParameters']['title'])
        box.append(event['queryStringParameters']['message'])
        box.append(event['queryStringParameters']['version'])
        box.append(event['queryStringParameters']['link'])
        box.append(event['queryStringParameters']['device'])
    elif getinput == 'updateAuth':
        box.append(event['queryStringParameters']['whoami'])
        box.append(event['queryStringParameters']['auth'])
        box.append(event['queryStringParameters']['device'])
    elif getinput == 'rdsConfig' or getinput == 'rdsConfigSelf':
        box.append(event['queryStringParameters']['link'])    #0
        box.append(event['queryStringParameters']['DBname'])  #1
        box.append(event['queryStringParameters']['user'])    #2
        box.append(event['queryStringParameters']['password'])#3
    elif getinput == 'deleteControlU':
        box.append(event['queryStringParameters']['title'])
        box.append(event['queryStringParameters']['version'])
    elif getinput == 'deleteStatus':
        box.append(event['queryStringParameters']['whoami'])
        box.append(event['queryStringParameters']['version'])
    elif getinput == 'deleteAuth':
        box.append(event['queryStringParameters']['whoami'])
    elif getinput == 'urlConfig':
        box.append(event['queryStringParameters']['get'])
        box.append(event['queryStringParameters']['post'])
        box.append(event['queryStringParameters']['check'])
    elif getinput == 'createTable':
        hold = event['queryStringParameters']['holder']
        loader = json.loads(hold)
        box.append(loader)
    return box
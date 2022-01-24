from smartapi import SmartConnect 
import os

def builtConnection():
    username = os.environ.get('angel_username')
    password = os.environ.get('angel_password')
    api_key = os.environ.get('angel_api')

    obj=SmartConnect(api_key)
    data = obj.generateSession(username, password)
    refreshToken= data['data']['refreshToken']
    
    feedToken=obj.getfeedToken()
    userProfile= obj.getProfile(refreshToken)
    print (feedToken)
    return obj, data, refreshToken, feedToken, userProfile
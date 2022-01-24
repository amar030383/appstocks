import smtplib, os

        
def sendEmail(Subject, Message):
    g_username = os.environ.get('g_username')
    g_password = os.environ.get('g_password')
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(g_username, g_password)
    msg = "\r\n".join(["From:"+g_username,"To:"+g_username, "Subject: "+Subject, Message])
    server.sendmail(g_username, g_username, msg)
    server.quit()


from nsetools import Nse
import json
from NSE_Info import NSE, NSE2
nse = Nse()
#data = nse.get_index_list()
#data = nse.get_quote('upl')
#print (data)
#print (json.dumps(data, indent = 2))


def get_quotes():
    data = nse.get_quote('upl')
    #print (data)
    print (json.dumps(data, indent = 2))

for stock in NSE2:
    data = nse.get_quote(stock)
    print (json.dumps(data, indent = 2))
    

    


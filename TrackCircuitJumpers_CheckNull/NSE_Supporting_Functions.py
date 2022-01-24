import smtplib, os

def findmonth(lastMonth):
    if lastMonth==0:
        goback = 12
        return (goback)
    else:
        return lastMonth
        
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
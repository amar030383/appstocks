from datetime import date, timedelta, datetime

present_date = date.today()
prev_date = date.today() - timedelta(days = 365)



times=datetime.now().strftime('%m_%d_%H_%M')
print (times)
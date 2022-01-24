from calendar import month
import csv
from nsepy import get_history
from datetime import date, datetime, timedelta
from NSE_Info import NSE, NSE2

def informationExtractor(sym,prev_date):
#    df = get_history(symbol=sym, start=prev_date, end=present_date)
    df = get_history(symbol=sym, start=prev_date, end=present_date)
    ######################### Find Jump frequecy data #########################
    df ['HighLow'] = ( df['High']-df['Low'])
    df ['Jumping%'] = (df['HighLow'].mul(100)/df['Prev Close']).round(1) # Jump Track
    df ['Jump5'] = df['Jumping%']>=5
    df ['Jump8'] = df['Jumping%']>=8
    df ['Jump10'] = df['Jumping%']>=10
    df ['Jump12'] = df['Jumping%']>=12
    df ['Jump15'] = df['Jumping%']>=15
    df ['Jump18'] = df['Jumping%']>=18
    df ['Jump20'] = df['Jumping%']>=20
    ######################### Find Jump frequecy data #########################

    ############################## Find Rise data #############################
    df ['PreClose_Close_Change'] = ( df['Close']-df['Prev Close'])
    df ['Rise %'] = (df['PreClose_Close_Change'].mul(100)/df['Close']).round(1)   #Rise Track
    df ['Rise2'] = df['Rise %']>=2
    df ['Rise3'] = df['Rise %']>=3
    df ['Rise4'] = df['Rise %']>=4
    df ['Rise5'] = df['Rise %']>=5
    df ['Rise6'] = df['Rise %']>=6

    df ['Drop0'] = df['Rise %']<=-0
    df ['Drop1'] = df['Rise %']<=-1
    df ['Drop2'] = df['Rise %']<=-2
    df ['Drop3'] = df['Rise %']<=-3
    df ['Drop4'] = df['Rise %']<=-4
    df ['Drop5'] = df['Rise %']<=-5
    ######################### Find Rise data #########################

    df3= (df [['Symbol','High', 'Low', 'Open', 'HighLow', 'Prev Close', 'Close','PreClose_Close_Change', 
    'Rise %','Rise2','Rise3','Rise4','Rise5','Rise6', 'Drop0', 'Drop1', 'Drop2', 'Drop3', 'Drop4', 'Drop5','Jumping%','Jump5','Jump8','Jump10','Jump12','Jump15','Jump18','Jump20']])
    #print (df3)
    df2= (df [['PreClose_Close_Change','Jumping%','Rise %','Drop0','Drop1', 'Drop2', 'Drop3', 'Drop4', 'Drop5']])
    #print (df2)
    df2.to_excel('DropShareAnalysis'+sym+'.xlsx')
    return df3

def dataprocessor(prev_date):
    loop = 1
    file =filename+'.csv'
    with open(file, 'w', newline='') as csvfile:
        fields = ['Stock', 'week', 'Up2%', 'Up3%','Up4%','Up5%','Up6%','',
        'Drop0','Drop1','Drop2','Drop3','Drop4','Drop5','',
        'Jump5%', 'Jump8%', 'Jump10%','Jump12%','Jump15%','Jump18%','Jump20%']
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

        for sym in NSE2:
            df3 = informationExtractor(sym, prev_date)
            Jump5 = (df3['Jump5']).sum()
            Jump8 = (df3['Jump8']).sum()
            Jump10 = (df3['Jump10']).sum()
            Jump12 = (df3['Jump12']).sum()
            Jump15 = (df3['Jump15']).sum()
            Jump18 = (df3['Jump18']).sum()
            Jump20 = (df3['Jump20']).sum()

            count2 = (df3['Rise2']).sum()
            count3 = (df3['Rise3']).sum()
            count4 = (df3['Rise4']).sum()
            count5 = (df3['Rise5']).sum()
            count6 = (df3['Rise6']).sum()

            Drop0 = (df3['Drop0']).sum()
            Drop1 = (df3['Drop1']).sum()
            Drop2 = (df3['Drop2']).sum()
            Drop3 = (df3['Drop3']).sum()
            Drop4 = (df3['Drop4']).sum()
            Drop5 = (df3['Drop5']).sum()

            rows = [[sym, week ,count2, count3, count4, count5, count6,'',
            Drop0,Drop1,Drop2,Drop3,Drop4,Drop5,'',
            Jump5,Jump8,Jump10,Jump12,Jump15,Jump18,Jump20]]  
            print (loop,rows)          
            csvwriter.writerows(rows)
            loop = loop+1

present_date = date.today()

weeks = [4]
for week in weeks:
    days = (week*7)
    times=datetime.now().strftime('%d_%H_%M')
    prev_date = date.today() - timedelta(days = days)
    filename = 'NSE_Circuit_'+str(week)+'_Week_'+times
    dataprocessor(prev_date)

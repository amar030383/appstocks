import csv
from BestShares import BestOnes

def mapTokenStock():

    file2 = ('IdentifiedStocks.csv')
    with open('NSE_BSEStockNamesCode.csv','r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        #print (BestOnes)
        loop = 1
        with open(file2, 'a', newline='') as csvfile2:
            All_fields=['Token','shareName', 'Name', 'Market']
            csvwriter2 = csv.writer(csvfile2)
            csvwriter2.writerow(All_fields)

            for row in readCSV:
                Token = row[0]
                shareName = row[1]
                Name = row[2]
                Market = row[3]

                if Name in BestOnes:
                    row= [Token,shareName,Name, Market]
                    print (row)
                    csvwriter2.writerow(row)
                    loop+=1

    
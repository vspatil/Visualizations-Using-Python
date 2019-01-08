#1. Reading the CSV file,which has temperature data
import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt
filename = 'sitka_weather_07-2014.csv'
#filename = 'sitka_weather_2014.csv'
#filename = 'death_valley_2014.csv'

file = filename.split("_",2)
file1=file[0] + " " + file[1]

with open(filename,'r+') as file:
    reader = csv.reader(file)
    header_row = next(reader)
    #print(len(header_row))
    #print(header_row)


#2 Reading the header row and getting the indices of each column
#for index,column in enumerate(header_row):
   # print(index,column)

#3 we are looking for info from columns 0,1,3
#5 now we need date from CSV file to put it into our graph
    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_dt = dt.strptime(row[0],"%Y-%m-%d")
            if row[1] and row[3]:
              maxt = int(row[1])
              mint = int(row[3])
            else:
                print ("missing")
        except ValueError:
            print(current_dt , "missing data!")
        else:
            dates.append(current_dt)
            highs.append(maxt)
            lows.append(mint)
        #lows
#4 plotting the graph with high temperature data
    fig = plt.figure(dpi=128 , figsize=(10,10))
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    plt.title("Daily High And low Temperature Data of " + file1 + "!",fontsize=16)
    plt.xlabel('')
    fig.autofmt_xdate()
    plt.ylabel('Temperatures (F)',fontsize=14)
    plt.yticks([10,20,30,40,50,60,70,80,90,100])
    plt.tick_params(axis='both',which = 'major',labelsize=16)
    plt.show()



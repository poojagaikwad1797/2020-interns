'''
author: Pooja Gaikwad

'''

import json


from datetime import timedelta, date


import matplotlib.pyplot as plt








def daterange(start_date, end_date):


    for n in range(int((end_date - start_date).days)):


        yield start_date + timedelta(n)








with open('data.json') as f:


    perf = json.load(f)


rates=perf['rates']


print("Enter currency symbol (eg: INR for Indian Rupees)")


sym=input()


print("Enter start date (YYYY-MM-DD)")


y,m,d=map(int,input().split("-"))


start_date = date(y,m,d)


print("Enter End date (YYYY-MM-DD)")


y,m,d=map(int,input().split("-"))


end_date = date(y,m,d)


date=[]


l1=[]


for single_date in daterange(start_date, end_date):


    try:


        l1.append(rates[single_date.strftime("%Y-%m-%d")][sym])


        date.append(single_date.strftime("%Y-%m-%d"))





    except:


       None


plt.figure(figsize=(25,15))       


plt.plot(date,l1,label=sym)


plt.xlabel("Dates in range of entered dates")


plt.xticks(rotation=90)


plt.ylabel("INR exchange rates")


plt.legend(loc="upper left")


plt.show() 
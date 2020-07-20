import json

import turtle

import datetime

import collections

import math



with open('data.json') as f :

    data = json.load(f)

    

# Extracting sub dictionary and sorting it

prices = data["rates"]

prices =collections.OrderedDict(sorted(prices.items()))



# Extracting x-axis value

maxCurValue = 0

for day ,value in prices.items():

    if value['INR'] > maxCurValue:

        maxCurValue = value['INR']



# Extracting y-axis value

startDate = datetime.datetime(2020,1,1) 

endDate = datetime.datetime(2020,1,31) 

daysDiff = endDate - startDate

totalDays = daysDiff.days





t =turtle.Turtle()

screen = t.getscreen()

screen.title("INR->Blue  & GBP->green compared with EUR X-> Dates & Y-> currency value")

screen.tracer(30)

screen.setworldcoordinates(0,0,maxCurValue,totalDays)

t.up()

t.goto(0.1,0.1)

t.write('(0,0)')

t.goto(0,0)

t.pensize(3)

t.color('blue')

t.down()



# plotting graph and math.log for flattening graph

for day , value in prices.items():

    day =datetime.datetime.strptime(day,'%Y-%m-%d')

    if day>=startDate and day<=endDate:

        daysDiff=day - startDate

        totalDay =daysDiff.days

        print(value['INR'])

        curVal = str(value['INR'])

        t.goto(totalDay,math.log(value['INR']))

    

        

t.up()

#t.color("white")

t.goto(0,0)

t.down()





for day , value in prices.items():

    day =datetime.datetime.strptime(day,'%Y-%m-%d')

    if day>=startDate and day<= endDate:

        daysDiff=day - startDate

        totalDay =daysDiff.days

        print(value['GBP'])

        t.color("green")

        t.goto(totalDay,math.log(value['GBP']))



with open('latest-rates.json') as f:

    newData =json.load(f)



latestRatesINR = newData['rates']['INR']

latestRatesGBP = newData['rates']['GBP']

t.up()

t.goto(18,18)

t.down()

t.write('Current INR : '+str(latestRatesINR)+ ' Current GBP : '+str(latestRatesGBP))

t.up()

t.goto(17,17)

t.down()

t.write('Total number of days : '+str(totalDay))







print('latest rates')

print(latestRatesINR)

print( latestRatesGBP)  

latestRatesINR = math.log(latestRatesINR)

latestRatesGBP = math.log(latestRatesGBP)

#t.color("white")

t.up()

t.goto(0,0)

t.goto(totalDays+1,latestRatesINR)

t.hideturtle

t.down()

t.dot(10,"purple")

t.up()

t.goto(0,0)

t.goto(totalDays+1,latestRatesGBP)

t.down()

t.dot(10,"red")

t.up()

t.color('black')

t.showturtle()

t.goto(20,20)

t.down()

t.write("x->Dates Y-> currency value")

t.up()

t.goto(19,19)

t.down()

t.write("INR-> blue GBP-> green latest INR->purple & GBP->red")

t.up()

t.pensize(1)

t.goto(-0.3,-0.3)

t.down()

t.fd(80)

t.bk(82)

t.fd(2)

t.rt(90)

t.fd(2)

t.bk(2)

t.rt(180)

t.fd(20)

    

screen.update()

screen.exitonclick() 
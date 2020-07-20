'''
author: Pooja Gaikwad

'''
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



t.color('black')

t.up()

t.showturtle()

t.goto(20,20)

t.down()

t.write("x->Dates Y-> currency value")

t.up()

t.goto(19,19)

t.down()

t.write("INR-> blue GBP-> green ")

t.up()

t.color('black')

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
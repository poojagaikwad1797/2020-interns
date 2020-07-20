from tkinter import *

import json
import math 
import collections
import datetime
import turtle

def plot():



    with open('data.json') as f :

        data = json.load(f)

        

    # Extracting sub dictionary and sorting it

    prices = data["rates"]

    prices =collections.OrderedDict(sorted(prices.items()))

    currency =cur.get()   

    # Extracting x-axis value

    maxCurValue = 0

    for day ,value in prices.items():

        if value[currency] > maxCurValue:

            maxCurValue = value[currency]



    # Extracting y-axis value

    startDate = datetime.datetime.strptime(start_txt.get(),'%Y-%m-%d')

    endDate =datetime.datetime.strptime(end_txt.get(),'%Y-%m-%d')

    daysDiff = endDate - startDate

    totalDays = daysDiff.days





    t =turtle.Turtle()

    screen = t.getscreen()

    screen.title("Compare currencies with EUR")

    screen.tracer(30)

    screen.setworldcoordinates(0,0,maxCurValue,totalDays)

    t.up()

    t.goto(-0.1,-0.1)

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

            print(value[currency])

            t.goto(totalDay,math.log(value[currency]))

            t.dot(2,'blue')

            

    t.up()

    t.showturtle()

    t.goto(30,30)

    t.down()

    t.write("x->Dates Y-> currency value",font=('Arial',12))

    t.up()

    t.goto(25,25)

    t.down()

    t.color('green')

    t.write("currency max value: "+str(maxCurValue),font=('Arial',12))

    t.up()

    t.color('black')

    t.pensize(1)

    t.goto(0,0.)

    t.down()

    t.fd(totalDay)

    t.bk(totalDay)

    #t.fd(4)

    t.rt(90)

    #t.fd(4)

    #t.bk(4)

    t.goto(0,0)

    t.rt(180) 

    t.fd(25)

    screen.update()

    screen.exitonclick()  

def reset():

    t =turtle.Turtle()

    screen = t.getscreen()

    screen.resetscreen()

    t.bye()








app = Tk()

app.title('Stats')

app.geometry('900x550')

start_txt = StringVar()

start_label = Label(app, text='Start date :(yyyy-mm-dd) ', font=('bold', 12),pady=20)

start_label.grid(row=0, column=0)

start_entry =Entry(app,textvariable =start_txt)

start_entry.grid(row =0 ,column=1)

end_txt = StringVar()

end_label = Label(app, text=' End date :(yyyy-mm-dd) ', font=('bold', 12),pady=20)

end_label.grid(row=0, column=3)

end_entry =Entry(app,textvariable = end_txt )

end_entry.grid(row =0 ,column=4)

select_label = Label(app, text=' Select currency : ', font=('bold', 12),pady=20)

select_label.grid(row=1, column=0)

cur = StringVar()

cur.set('select')

cur_list = OptionMenu(app ,cur, "CAD","HSD","ISK","PHP","DKK","HUF","CZK","AUD","RON","SEK","IDR","INR"

,"BRL","RUB","HRK","JYP","USD","NZD","GBP")

cur_list.grid(row =1 ,column=1)

submit_btn = Button(app, text='Submit',width = 12,command =plot)

submit_btn.grid(row=1,column=2)

reset_btn = Button(app, text='Reset',width = 12,command =reset)

reset_btn.grid(row=1,column=3)



app.mainloop()
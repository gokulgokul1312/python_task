import datetime

def daynumber1():
    print("weekday 1: SUNDAY")
daynumber1()

def daynumber2():
    print("weekday 2: MONDAY")
daynumber2()

def daynumber3():
    print("weekday 3: TUESDAY")
daynumber3()

def daynumber4():
    print("weekday 4: WEDNESDAY")
daynumber4()

def daynumber5():
    print("weekday 5: THURSDAY")
daynumber5()

def daynumber6():
    print("weekday 6: FRIDAY")
daynumber6()

def daynumber7():
    print("weekday 7: SATURDAY")
daynumber7()

def daynumber0():
    print("weekday 0: SATURDAY")
daynumber0()

def today():
    today=datetime.datetime.now()
    weekday_name=today.strftime("%A")
    print("TODAY IS: {}".format(weekday_name))

number=int(input("Enter Number: "))

if number==1:
    daynumber1()
elif number==2:
    daynumber2()
elif number==3:
    daynumber3()
elif number==4:
    daynumber4()
elif number==5:
    daynumber5()
elif number==6:
    daynumber6()
elif number==7:
    daynumber7()
elif number==0:
    daynumber0()
else:
    print("weekday {} error".format(number))
    today()
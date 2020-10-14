# import datetime
# dt=datetime.datetime.now()
# print(dt)

# import datetime as dtm
# dt1=dtm.datetime.now()
# dt1=dtm.date.today()
# print(dt1)



# import datetime as dtm
# dt1=dtm.date(2020,5,12)
# dt2=dtm.timedelta(30)
# print(dt1+dt2)

# import datetime as dtm
# dt1=dtm.date.today()
# print("Current Year:",dt1.year)
# print("Current Month:",dt1.month)
# print("Current Day:",dt1.day)

# import datetime as dtm
# dt1=dtm.date(2020,5,17)
# print(dt1.strftime("%A,%B,%d,%Y"))

# import datetime as dtm
# dt1=input("Enter date/month/year:")
# result=dtm.datetime.strptime(dt1,"%d/%m/%Y")
# print(result)

import datetime as dtm
t1=dtm.timedelta(50)
t2=dtm.timedelta(27)
t3=t2-t1
print(t3)

import datetime as dtm
t1=dtm.timedelta(50)
t2=dtm.timedelta(27)
t3=t1-t2
print(t3)
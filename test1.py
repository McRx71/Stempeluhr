weeknr = 15

#print("Select task,time FROM Chris WHERE weeknumber =" + ' ' +str(weeknr))


import datetime
date_string = "20.05.2021"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
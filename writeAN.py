import docx
import sqlite3
import datetime
import pandas as pd

try:
    connection = sqlite3.connect("timetable.db")
    cursor = connection.cursor()
    cursor.execute("Select * from Chris")
except:
    print('Database is missing!')


document = docx.Document('Ausbildungsnachweis.docx')

mon_list = ['Montag1','Montag2','Montag3','Montag4','Montag5','Montag6']
tue_list = ['Dienstag1','Dienstag2','Dienstag3','Dienstag4','Dienstag5','Dienstag6']
wed_list = ['Mittwoch1','Mittwoch2','Mittwoch3','Mittwoch4','Mittwoch5', 'Mittwoch6']
thu_list = ['Donnerstag1', 'Donnerstag2', 'Donnerstag3','Donnerstag4', 'Donnerstag5','Donnerstag6']
fri_list = ['Freitag1','Freitag2','Freitag3','Freitag4','Freitag5','Freitag6']
def wr_mon(task_list):
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for x in mon_list:
                        if x in paragraph.text:
                            for task in task_list:
                                print(x + ' mit Aufgabe: ' + task)
                                #print(task)
                                try:
                                    paragraph.text = paragraph.text.replace(x, task)
                                    exit()
                                except:
                                    exit()


def getdata_mon(weeknr):
    #print(type(weeknr))
    list = []
    #print("Select task,time FROM Chris WHERE weeknumber =" + ' ' +str(weeknr))
    cursor.execute("Select dayofweek,task,time FROM Chris WHERE weeknumber =" + ' ' +str(weeknr))
    rows = cursor.fetchall()
    for row in rows:
        #print(row)
        if row[0] == 'Monday':
            list.append(row[1])
            #print(row)
            #print(type(row))
        #continue
    #print(list)
    #print(type(list))
    return list



#def wr_sheet(weeknr):


#weeknr = input('WeekNr: ')
weeknr = '20'
task_list = getdata_mon(weeknr)
wr_mon(task_list)
#wr_sheet()
document.save('New.docx')
import os, sys, sqlite3, locale
from datetime import *

class create_entry:

    def __init__(self):


    locale.setlocale(locale.LC_TIME, locale.normalize("de"))

    def dow(self):
        dayofweek = date.today().strftime('%A')
        return dayofweek
    def weeknr(self):
        weeknumber = date.today().strftime('%W')
        return weeknumber
    def date(self):
        return date.today().strftime("%d.%m.%Y")
    # Verbindung zur Datenbank erzeugen
    connection = sqlite3.connect("timetable.db")
    # Datensatz-Cursor erzeugen
    cursor = connection.cursor()



    # Datensatz erzeugen
    sql = "INSERT INTO Chris VALUES(" + "'"+weeknr()+"'" + "," + "'"+dow()+"'"+")"
    cursor.execute(sql)
    connection.commit()

    # Verbindung beenden
    connection.close()


#https://www.python-lernen.de/python-modul-datetime.htm
#https://www.informatik-aktuell.de/betrieb/datenbanken/datenbanken-mit-python-und-sqlite.html#:~:text=%20Datenbanken%20mit%20Python%20und%20SQLite%20%201,WHERE%20k%C3%B6nnen%20Sie%20einen%20oder%20mehrere...%20More
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

    # Verbindung zur Datenbank erzeugen
    connection = sqlite3.connect("timetable.db")

    # Datensatz-Cursor erzeugen
    cursor = connection.cursor()



    # Datensatz erzeugen
    sql = "INSERT INTO Chris VALUES(" + "'"+dow()+"'" + "," + "'"+weeknr()+"'"+")"
    cursor.execute(sql)
    connection.commit()

    # Verbindung beenden
    connection.close()

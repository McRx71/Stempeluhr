import sqlite3, os, sys


class createDB:

    def checkDB():
        # Existenz feststellen, wenn nicht vorhanden, dann v
        if os.path.exists("timetable.db"):
            pass
        else:
            # Datenbanktabelle erzeugen
            connection = sqlite3.connect("timetable.db")
            cursor = connection.cursor()
            sql = "CREATE TABLE Chris(" \
                  "weeknumber INTEGER, " \
                  "dayofweek TEXT, " \
                  "date TEXT, " \
                  "time TEXT, " \
                  "task TEXT)"

            cursor.execute(sql)
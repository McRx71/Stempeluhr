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
                  "weeknumber TEXT, " \
                  "dayofweek TEXT, " \
                  "date DATE, " \
                  "time REAL, " \
                  "task TEXT)"

            cursor.execute(sql)
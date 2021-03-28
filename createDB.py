import sqlite3, os, sys


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
              "task TEXT," \
              "FirstLevelSupport BOOLEAN)"

        cursor.execute(sql)


if __name__ == '__main__':
    checkDB()

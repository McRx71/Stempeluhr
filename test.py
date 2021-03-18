import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("timetable.db")
cursor = connection.cursor()

# SQL-Abfrage
sql = "SELECT * FROM timetable"

# Kontrollausgabe der SQL-Abfrage
# print(sql)

# Absenden der SQL-Abfrage
# Empfang des Ergebnisses
cursor.execute(sql)

# Ausgabe des Ergebnisses
for dsatz in cursor:
    print(dsatz[0], dsatz[1])

# Verbindung beenden
connection.close()
import sqlite3

connection = sqlite3.connect("/Users/aleksandrzagorulko/Documents/Personal/Education/Sirius/Python/Practical_work/Quiz/Database_Quiz")
cursor = connection.cursor()
for i in range(5):
    cursor.execute('INSERT INTO Pycharm VALUES (' + str(i) + ");")
connection.commit()
cursor.close()
connection.close()
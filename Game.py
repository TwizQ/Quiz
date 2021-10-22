import random
import sqlite3

connect = sqlite3.connect("quiz.db")

for i in range(1, 6):
    table = "SELECT *FROM level_" + str(i) + " WHERE id=" + str(random.randint(1, 2))

    for j in range(len(connect.cursor().execute(table).fetchall()[0]) - 2):
        print(connect.cursor().execute(table).fetchall()[0][j + 1])
    try:
        a = int(input())
    except:
        exit()
    if a >= 1 and a <= 4:
        if connect.cursor().execute(table).fetchall()[0][6] == connect.cursor().execute(table).fetchall()[0][a + 1]:
            print("You answered correctly")
        else:
            print("The answer is wrong")
            exit()
    else:
        print("There is no such answer")
        exit()
print("Victory")

connect.commit()
connect.cursor().close()
connect.close()
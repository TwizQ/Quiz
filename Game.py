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
    if a > 0 and a < 5:
        if connect.cursor().execute(table).fetchall()[0][6] == connect.cursor().execute(table).fetchall()[0][a + 1]:
            print("Вы ответили верно (｡◕‿◕｡)")
        else:
            print("Ответ неверно (ノಠ益ಠ)ノ彡┻━┻")
            exit()
    else:
        print("Такого ответа нету ಠ_ಠ")
        exit()
print("Победа (づ｡◕‿‿◕｡)づ")

connect.commit()
connect.cursor().close()
connect.close()
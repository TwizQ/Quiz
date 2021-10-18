import sqlite3

connect = sqlite3.connect('Database_Quiz')
cursor = connect.cursor()

def users_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Quiz_1(
        id_leval INTEGER,
        id_question INTEGER,
        question TEXT,
        answer_1 TEXT,
        answer_2 TEXT,
        answer_3 TEXT,
        answer_4 TEXT,
        correct_answer
    )
    """)

    connect.commit()

    Quiz_ist = [1, 1, 'Какой национальный цветок Японии?', '1.Сакура', '2.Лотос', '3.Ликорис', '4.Бонсай', 2]
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [1, 2, 'В какой из следующих империй не было письменности?', '1.Римлян', '2.Ацтеков', '3.Инков', '4.Египтян', 3]
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [2, 1, 'До 1923 года как назывался турецкий город Стамбул?', '1.Константинополь', '2.Стамбул', '3.ЦарьГрад', '4.ЦарьГрад', 1]
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [2, 2, 'Какой национальный цветок Японии? ', 'Сакура', 'Лотос', 'Ликорис', 'Бонсай', 2]
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [3, 1, 'Какой национальный цветок Японии? ', 'Сакура', 'Лотос', 'Ликорис', 'Бонсай', 2]
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [3, 2, 'Какой национальный цветок Японии? ', 'Сакура', 'Лотос', 'Ликорис', 'Бонсай', 2]
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [4, 1, 'Какой национальный цветок Японии? ', 'Сакура', 'Лотос', 'Ликорис', 'Бонсай', 2]
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [4, 2, 'Какой национальный цветок Японии? ', 'Сакура', 'Лотос', 'Ликорис', 'Бонсай', 2]
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [5, 1, 'Какой национальный цветок Японии? ', 'Сакура', 'Лотос', 'Ликорис', 'Бонсай', 2]
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [5, 2, 'Какой национальный цветок Японии? ', 'Сакура', 'Лотос', 'Ликорис', 'Бонсай', 2]
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    #INTEGER, REAL (10.5), TEXT
def users_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Quiz_1(
        question TEXT,
        answer_1 TEXT,
        answer_2 TEXT,
        answer_3 TEXT,
        answer_4 TEXT,
        correct_answer
    )
    """)

    connect.commit()

    Quiz_1_list = ['Какой национальный цветок Японии? ', 'Сакура', 'Лотос', 'Ликорис', 'Бонсай', 2]
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?);", Quiz_1_list)
    connect.commit()

    #INTEGER, REAL (10.5), TEXT
def delete_db():
    cursor.execute("DROP TABLE ....")
    connect.commit()
def search_db():
    cursor.execute("SELECT * FROM users")
    all_results = cursor.fetchall()
    print(all_results[0][1])

users_db()
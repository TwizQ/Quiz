

import sqlite3

connect = sqlite3.connect('Database_Quiz/Database_Quiz.db')
cursor = connect.cursor()

def quiz_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Quiz_1(
        id_leval INTEGER,
        id_question INTEGER,
        question TEXT,
        answer_1 TEXT,
        answer_2 TEXT,
        answer_3 TEXT,
        answer_4 TEXT,
        correct_answer INTEGER
    )
    """)

    connect.commit()

    quiz_ist = (1, 1, 'Какой национальный цветок Японии?', '1.Сакура', '2.Лотос', '3.Ликорис', '4.Бонсай', 2)
    cursor.execute("INSERT INTO Quiz_1 VALUES(%d,%d,%s,%s,%s,%s,%s,%d);" % quiz_ist)
    connect.commit()

    Quiz_ist = [1, 2, 'В какой из следующих империй не было письменности?', '1.Римлян', '2.Ацтеков', '3.Инков', '4.Египтян', 3]
    cursor.execute("INSERT INTO Database_Quiz VALUES(?,?,?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [2, 1, 'До 1923 года как назывался турецкий город Стамбул?', '1.Константинополь', '2.Стамбул', '3.ЦарьГрад', '4.ЦарьГрад', 1]
    cursor.execute("INSERT INTO Database_Quiz VALUES(?,?,?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [2, 2, 'В 1952 году президентом какой страны был предложен Альберт Эйнштейн?', '1.Израиль', '2.Швеция', '3.Франция', '4.Турция', 1]
    cursor.execute("INSERT INTO Database_Quiz VALUES(?,?,?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [3, 1, 'Как называется столица американского штата Калифорния?', '1.Северная дакота', '2.Монтана', '3.Сакроменто', '4.Невада', 3]
    cursor.execute("INSERT INTO Database_Quiz VALUES(?,?,?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [3, 2, 'Какое животное можно увидеть на логотипе Porsche?', '1.Олень', '2.Олень', '3.Корову', '4.Лошадь', 4]
    cursor.execute("INSERT INTO Database_Quiz VALUES(?,?,?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [4, 1, 'Сколько спутников у Марса?', '1.1', '2.2', '3.3', '4.', 2]
    cursor.execute("INSERT INTO Database_Quiz VALUES(?,?,?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [4, 2, 'Чтобы доказать, что Микеланджело не умел рисовать, какой художник предложил Папе Римскому расписать Сикстинскую капеллу?', '1.Микеланджело', '2.Леонардо да Винчи', '3.Рафаэль', '4.Донателло', 1]
    cursor.execute("INSERT INTO Database_Quiz VALUES(?,?,?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [5, 1, 'Назовите два самых известных в мире и популярных произведения русских писателей?', '1.<<Преступление и наказание>> Достоевского, <<Анна Каренина>> Льва Толстого', '2.Иван Тургенев<<Отцы и дети>> Льюис<<Космическая трилогия>>', '3.Булгаков<<Мастер и Маргарита>> Михаил Лермонтов <<Герой нашего  времени>>', '4.Лев Толстой <<Война и Мир>> Достоевский  <<Братья Карамазовы>>', 1]
    cursor.execute("INSERT INTO Database_Quiz VALUES(?,?,?,?,?,?,?,?);", Quiz_ist)
    connect.commit()

    Quiz_ist = [5, 2, 'Кто изобрел всемирную паутину?', '1.Павел Валерьевич Дуров', '2.Тим Бернерс-Ли', '3.Бил Гейтс', '4.Линус Торвальдс', 2]
    cursor.execute("INSERT INTO Database_Quiz VALUES(?,?,?,?,?,?,?,?);", Quiz_ist)
    connect.commit()


def delete_db():
    cursor.execute("DROP TABLE ....")
    connect.commit()
def search_db():
    cursor.execute("SELECT * FROM users")
    all_results = cursor.fetchall()
    print(all_results[0][1])

quiz_db()
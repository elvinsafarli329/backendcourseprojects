import sqlite3

con = sqlite3.connect("tournament")
cursor = con.cursor()

# bu birinci table di, ve 5 data var(inputdan alinib)
def tournament_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS science_tour_winners(name TEXT, subject TEXT, score INT, place INT)")


    cursor.execute("PRAGMA table_info(science_tour_winners)")
    columns = [column[1] for column in cursor.fetchall()]

    if 'age' not in columns:
        cursor.execute("ALTER TABLE science_tour_winners ADD COLUMN age INT")
        con.commit()

name = input("enter the name of the winner: ")
subject = input("enter the subject of tournament: ")
score = int(input("enter the score of the winner: "))
place = int(input("enter the place taken by the winner: "))
age = int(input("enter the age of the winner: "))

def tournament_data(name, subject, score, place, age):
    cursor.execute("INSERT INTO science_tour_winners VALUES(?, ?, ?, ?, ?)", (name, subject, score, place, age))
    con.commit()

def update_subject(subject, new_subject):
    cursor.execute("UPDATE science_tour_winners SET subject = ? WHERE subject = ?", (new_subject, subject))
    con.commit()

subject = input("Enter the name of thesubject you want to update: ")
new_subject = input("Enter the new subject: ")

update_subject(subject, new_subject)

def delete_row():
    cursor.execute("DELETE FROM science_tour_winners WHERE rowid = (SELECT rowid FROM science_tour_winners ORDER BY rowid LIMIT 1)")
    con.commit()


delete_row()
tournament_data(name, subject, score, place, age)


# ikinci table di (en son 1ci ile cross join olunacaq)
def tournament_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS science_tour_winners(name TEXT, subject TEXT, score INT, place INT)")
    con.commit()

def create_underage_winners_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS underage_winners(name TEXT, subject TEXT, score INT, place INT)")
    con.commit()

    cursor.execute("PRAGMA table_info(underage_winners)")
    columns = [column[1] for column in cursor.fetchall()]

    if 'age' not in columns:
        cursor.execute("ALTER TABLE underage_winners ADD COLUMN age INT")
        con.commit()

def datas_of_second_tournament():
    data_to_insert = [
        ('Gunay', 'Physics', 80, 3, 10),
        ('Jale', 'Chemistry', 85, 2, 11),
        ('Ezo', 'Physics', 90, 2, 10),
        ('Fuad', 'Biology', 95, 1, 12)
    ]
    
    cursor.executemany("INSERT INTO underage_winners(name, subject, score, place, age) VALUES (?, ?, ?, ?, ?)", data_to_insert)
    con.commit()


cursor.execute("SELECT * FROM science_tour_winners CROSS JOIN underage_winners")

result = cursor.fetchall()
for row in result:
    print(row)

tournament_table()
create_underage_winners_table()

datas_of_second_tournament()
con.close()


import sqlite3

connection = sqlite3.connect('ustoz-shogirt.db')
cursor = connection.cursor()


def create_database():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conditate(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       type TEXT NOT NULL,
       full_name NOT NULL,
       age INTEGER NOT NULL,
       tools TEXT NOT NULL,
       phone_number TEXT NOT NULL,
       location TEXT NOT NULL,
       price TEXT NOT NULL,
       job TEXT NOT NULL,
       time TEXT NOT NULL,
       aim TEXT NOT NULL
       )

""")





connection.commit()

def insert_into_database(type,full_name,age,tools,phone_number,location,price,job,time,aim):
    cursor.execute('INSERT INTO conditate(type,full_name,age,tools,phone_number,location,price,job,time,aim) VALUES (?,?,?,?,?,?,?,?,?,?)', (type,full_name,age,tools,phone_number,location,price,job,time,aim) )
    connection.commit()

def get_conditates():
    return cursor.execute('SELECT * FROM conditate WHERE id = 1').fetchone()
def deleete_id():
    cursor.execute('DELETE FROM conditated WHERE id = 1', ('full_name',))

def update_condidate(id,age):
    cursor.execute('UPDATE conditate SET age = ? WHERE id = ?', (age,id))
    connection.commit()


# insert_into_database('Ish kerak', 'Jaloliddin',24,'Python,aiogram','+998909997065','Toshkent','Tekin','Remote','9-19','ish uchun')
update_condidate(1, 19,)
print(get_conditates())


connection.close()






import sqlite3

connection = sqlite3.connect('ustoz-shogirt.db')
cursor = connection.cursor()


def create_database():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conditate(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       company TEXT NOT NULL,
       tools NOT NULL,
       phone_number INTEGER NOT NULL,
       place TEXT NOT NULL,
       ceo TEXT NOT NULL,
       time TEXT NOT NULL,
       remaining time TEXT NOT NULL,
       price TEXT NOT NULL,
       aim  TEXT NOT NULL,
    
       )

""")


connection.commit()

def insert_into_database(id,company,tools,phone_number,location,price,job,time,aim):
     cursor.execute('INSERT INTO conditate(id,company,tools,phone_number,location,price,job,time,aim) VALUES (?,?,?,?,?,?,?,?,?)', (id,company,tools,phone_number,location,price,job,time,aim) )
     connection.commit()


def get_conditates():
    return cursor.execute('SELECT * FROM conditate').fetchall()


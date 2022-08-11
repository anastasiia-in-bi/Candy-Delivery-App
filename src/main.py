import sqlite3


def init_db():
    f = open('../sql/init.sql', 'r')
    conn = sqlite3.connect('../candy.db')
    conn.execute(f.read())
    conn.close()

def add_courier(name, age, courier_type):
    add_sql=f"INSERT INTO courier(name, age, courier_type) VALUES('{name}', {age}, '{courier_type}')"
    conn = sqlite3.connect('../candy.db')
    conn.execute(add_sql)
    conn.commit()
    conn.close()

def all_couriers():
    select_couriers="SELECT * FROM courier"
    conn = sqlite3.connect('../candy.db')
    cur = conn.cursor()
    cur.execute(select_couriers)
    rows = cur.fetchall()
    conn.close()

    return rows

init_db()
add_courier('vasya', 17, 'foot')

print(all_couriers())
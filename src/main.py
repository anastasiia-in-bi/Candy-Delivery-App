import sqlite3
from models.courier import CourierManager
from models.order import OrderManager

def init_db():
    f = open('../sql/init.sql', 'r')
    conn = sqlite3.connect('../candy.db')
    conn.execute(f.read())
    conn.close()

def main():
    # init_db()
    courier=CourierManager('../candy.db')
    print(courier.create('vasya', 17, 'foot'))
    print(courier.update(1, 'kotefeichik', 30, 'car'))
    print(courier.delete(1))
    print(courier.all())

main()

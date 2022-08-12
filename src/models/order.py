import sqlite3


class OrderManager:
    def __init__(self, db_path):
        self.conn=sqlite3.connect(db_path)
        self.cur=self.connect.cursor()

    def create(self, weight, region, time_start, time_finish):
        add_order=f"INSERT INTO order(weight, region, time_start, time_finish) VALUES({weight}, {region}, {time_start}, {time_finish}) RETURNING *;"
        self.cur.execute(add_order)
        self.conn.commit()
        rows = self.cur.fetchall()

        return rows
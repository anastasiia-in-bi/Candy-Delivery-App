import sqlite3


class CourierManager:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def create(self, name, age, courier_type):
        add_sql = f"INSERT INTO courier(name, age, courier_type) VALUES('{name}', {age}, '{courier_type}') RETURNING *"
        self.cur.execute(add_sql)
        row = self.cur.fetchall()
        self.conn.commit()

        return row

    def all(self):
        select_couriers = "SELECT * FROM courier;"
        self.cur.execute(select_couriers)

        return self.cur.fetchall()

    def update(self, courier_id, name, age, courier_type):
        alter_courier = f"UPDATE courier SET name='{name}', age={age}, " \
                        f"courier_type='{courier_type}' WHERE {courier_id}=courier_id RETURNING *;"
        self.cur.execute(alter_courier)

        return self.cur.fetchall()

    def delete(self, courier_id):
        del_courier = f"DELETE FROM courier WHERE courier_id={courier_id} RETURNING *;"
        self.cur.execute(del_courier)

        return self.cur.fetchall()

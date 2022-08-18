import sqlite3


class Manager:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self.conn = None
        self.cur = None

    def open_connect(self) -> None:
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def execute_and_return(self, sql: str) -> list:
        self.open_connect()
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        self.conn.commit()
        self.conn.close()

        return rows

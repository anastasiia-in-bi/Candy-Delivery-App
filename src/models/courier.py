from .manager import Manager


class CourierManager(Manager):
    def __init__(self, db_path: str) -> None:
        super(CourierManager, self).__init__(db_path)

    def create(self, name: str, age: int, courier_type: str) -> list:
        add_sql = f"INSERT INTO courier(name, age, courier_type) VALUES('{name}', {age}, '{courier_type}') RETURNING *"

        return self.execute_and_return(add_sql)

    def all(self) -> list:
        select_couriers = "SELECT * FROM courier;"

        return self.execute_and_return(select_couriers)

    def update(self, courier_id: int, name: str, age: int, courier_type: str) -> list:
        alter_courier = f"UPDATE courier SET name='{name}', age={age}, " \
                        f"courier_type='{courier_type}' WHERE {courier_id}=courier_id RETURNING *;"

        return self.execute_and_return(alter_courier)

    def delete(self, courier_id: int) -> list:
        del_courier = f"DELETE FROM courier WHERE courier_id={courier_id} RETURNING *;"

        return self.execute_and_return(del_courier)

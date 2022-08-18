from .manager import Manager


class OrderManager(Manager):
    def __init__(self, db_path: str) -> None:
        super(OrderManager, self).__init__(db_path)

    def create(self, weight: float, region: int, time_start: str, time_finish: str) -> list:
        add_order = f"INSERT INTO 'order'(weight, region, time_start, time_finish) " \
                    f"VALUES({weight}, {region}, strftime('%H:%M:%S', '{time_start}'), strftime('%H:%M:%S', '{time_finish}')) RETURNING *;"

        return self.execute_and_return(add_order)

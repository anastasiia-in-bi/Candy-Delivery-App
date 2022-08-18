from models.courier import CourierManager
from models.order import OrderManager


def main():
    courier = CourierManager('../candy.db')
    print(courier.create('vasya', 17, 'foot'))
    print(courier.update(1, 'kotefeichik', 30, 'car'))
    print(courier.delete(1))
    print(courier.all())
    order = OrderManager('../candy.db')
    print(order.create(12.4, 2, '16:00:00', "18:02:00"))


if __name__ == '__main__':
    main()

from models.courier import CourierManager
from models.order import OrderManager
from aiohttp import web
from src.views.couriers import all_couriers


def main_managers():
    courier = CourierManager('../candy.db')
    print(courier.create('vasya', 17, 'foot'))
    print(courier.update(1, 'kotefeichik', 30, 'car'))
    print(courier.delete(1))
    print(courier.all())
    order = OrderManager('../candy.db')
    print(order.create(12.4, 2, '16:00:00', "18:02:00"))

def main():
    def handle(request):
        name = request.match_info.get('name', "Anonymous")
        text = "Hello, " + name
        return web.Response(text=text)

    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/couriers', all_couriers),
                    web.get('/{name}', handle)])
    web.run_app(app)

if __name__ == '__main__':
    main()

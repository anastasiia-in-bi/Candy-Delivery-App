from src.models.courier import CourierManager
from aiohttp import web


async def all_couriers(request):
    manager = CourierManager('../candy.db')
    couriers_list = manager.all()

    return web.json_response(couriers_list)

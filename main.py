from aiogram.utils import executor
from config import dp
from handlares import client, callback, extra, admin, fsm_anketa, notification
import logging
from database.bot_db import sql_create
import asyncio

async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()



client.register_handler_client(dp)
callback.register_handler_callback(dp)
admin.register_handler_admin(dp)
fsm_anketa.registor_handler_fsm_anketa(dp)
notification.register_handlers_notification(dp)


extra.registor_handler_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

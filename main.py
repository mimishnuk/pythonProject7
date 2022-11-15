from aiogram.utils import executor
from config import dp
from handlares import client, callback, extra, admin
import logging

client.register_handler_client(dp)
callback.register_handler_callback(dp)
admin.register_handler_admin(dp)

extra.registor_handler_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

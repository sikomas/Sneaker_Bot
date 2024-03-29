
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import token


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)
# loop = asyncio.get_event_loop()
# Поток нам не нужен, т.к. он и так создается в диспатчере.

storage = MemoryStorage()

bot = Bot(token=token, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)
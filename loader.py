from unittest import loader

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from parser import CurrencyParser

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

difference = 0.1
try:
    with open('data/data.txt', 'r') as f:
        difference = int(f.read()) / 100
except:
    pass
cp = CurrencyParser(difference)

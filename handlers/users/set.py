from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, cp


@dp.message_handler(commands="set")
async def bot_set(message: types.Message):
    if message.get_args():
        try:
            with open('data/data.txt', 'w') as f:
                f.write(message.get_args())
        except:
            pass

        cp.difference = int(message.get_args()) / 100

        await message.answer(f"✅ Изменение: {message.get_args()} коп.")
    else:
        await message.answer(f"Формат команды:\n/set 10 (ед. изм. копейки)")


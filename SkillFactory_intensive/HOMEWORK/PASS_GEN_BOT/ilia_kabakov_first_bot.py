from main import *
from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
db = Dispatcher(bot)


@db.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Enter the length of password you want?(6-100)")


@db.message_handler()
async def get_length(message: types.Message):
    try:
        values: int = message.text
        p_gen = Password(int(values))
        await message.reply(f'Your new password: {p_gen.generate()}')


    except Exception:
        await message.reply(f"Exception. Something went wrong.")


if __name__ == '__main__':
    executor.start_polling(db)

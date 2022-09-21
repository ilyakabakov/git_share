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
        # p_gen.choice1 = message.text
        await message.reply(f'Your new password: {p_gen.generate()}')
        # await message.reply(f'Do you want add the digits in password?(y/n)')

    except:     #Yes, PEP8 i know it :)
        await message.reply(f"Exception. Something went wrong.")


# @db.message_handler()
# async def get_choice1(message: types.Message):
#     try:
#         text_v: str = message.text
#         p_gen = Password()
#         p_gen.with_digits(text_v)
#         await message.answer("Do you want add the spec symbols in the password?(y/n)")
#     except TypeError:
#         await message.reply("Что-то пошло не так")


if __name__ == '__main__':
    executor.start_polling(db)

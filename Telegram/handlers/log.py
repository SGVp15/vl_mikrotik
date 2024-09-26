import os

from aiogram import types
from aiogram.filters import Command

from Telegram.main import dp
from Utils.log import log


def is_empty_file(file) -> bool:
    if not os.path.exists(file):
        return True

    try:
        with open(file=file, mode="r", encoding='utf-8') as f:
            s = f.read()
            return len(s) <= 10
    except UnicodeDecodeError:
        log.error('UnicodeDecodeError')
    return False


@dp.message(Command('id'))
async def send_id(message: types.Message):
    await message.answer(str(message.chat.id))

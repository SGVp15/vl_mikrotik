from aiogram import types

from Telegram.main import dp
from config import SYSTEMLOG


@dp.message()
async def echo(message: types.Message):
    await message.reply('Не понимаю, что это значит.'
                        'Воспользуйтесь командой /help')
    with open(SYSTEMLOG, encoding='utf-8', mode='a') as f:
        for k, v in message:
            f.write(f'{k} {v}', )
        f.write('\n')

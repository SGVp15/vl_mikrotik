from aiogram import types, F

from SSH_MIKROTIK.command import Command
from SSH_MIKROTIK.mikrotik_ssh import run_command_ssh
from Telegram.Call_Back_Data import CallBackData
from Telegram.config import USERS_ID, ADMIN_ID
from Telegram.keybords.inline import inline_kb_main
from Telegram.main import bot, dp
from Utils.log import log


@dp.callback_query(F.data.in_({CallBackData.vpn_down}) & F.from_user.id.in_({*ADMIN_ID, *USERS_ID}))
async def show_registration(callback_query: types.callback_query):
    log.info(f'{F.data} {F.from_user.id}')
    text = f'on_vpn\n'
    text += run_command_ssh(Command.off_vpn())
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=text,
        reply_markup=inline_kb_main
    )


@dp.callback_query(F.data.in_({CallBackData.vpn_up}) & F.from_user.id.in_({*ADMIN_ID, }))
async def show_registration(callback_query: types.callback_query):
    log.info(f'{F.data} {F.from_user.id}')
    text = f'off_vpn\n'
    text += run_command_ssh(Command.on_vpn())
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=text,
        reply_markup=inline_kb_main
    )


@dp.callback_query(F.data.in_({CallBackData.vpn_wg_status}) & F.from_user.id.in_({*ADMIN_ID, }))
async def show_registration(callback_query: types.callback_query):
    text = f'vpn_wg_status:\n'
    s = run_command_ssh(Command.status_wg_vpn()).split('\n')
    text += '\n'.join(s[:2])
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=text,
        reply_markup=inline_kb_main
    )

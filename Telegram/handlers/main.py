from aiogram import types, F

from SSH_MIKROTIK.mikrotik_ssh import run_command_ssh
from Telegram.Call_Back_Data import CallBackData
from Telegram.config import USERS_ID, ADMIN_ID
from Telegram.keybords.inline import inline_kb_main
from Telegram.main import bot, dp
from config import ON_VPN_COMMAND, OFF_VPN_COMMAND, STATUS_WG_VPN_COMMAND


@dp.callback_query(F.data.in_({CallBackData.vpn_down}) & F.from_user.id.in_({*ADMIN_ID, *USERS_ID}))
async def show_registration(callback_query: types.callback_query):
    text = '_ON_VPN_COMMAND'
    text += run_command_ssh(ON_VPN_COMMAND)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=text,
        reply_markup=inline_kb_main
    )


@dp.callback_query(F.data.in_({CallBackData.vpn_up}) & F.from_user.id.in_({*ADMIN_ID, }))
async def show_registration(callback_query: types.callback_query):
    text = '_OFF_VPN_COMMAND'
    text += run_command_ssh(OFF_VPN_COMMAND)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=text,
        reply_markup=inline_kb_main
    )



@dp.callback_query(F.data.in_({CallBackData.vpn_wg_status}) & F.from_user.id.in_({*ADMIN_ID, }))
async def show_registration(callback_query: types.callback_query):
    text = f'vpn_wg_status:\n'
    text += run_command_ssh(STATUS_WG_VPN_COMMAND)[:300]
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=text,
        reply_markup=inline_kb_main
    )

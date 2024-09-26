from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData

inline_btn_logs = InlineKeyboardButton(text='Скачать Логи', callback_data=CallBackData.download_logs)


def add_return_main_menu():
    return [InlineKeyboardButton(text='<< Back <<', callback_data=CallBackData.back_to_main), ]


inline_kb_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дед мороз пришел', callback_data=CallBackData.vpn_down), ],
    [InlineKeyboardButton(text='>> Admin >>', callback_data=CallBackData.admin_menu), ],
])

inline_kb_admin = InlineKeyboardMarkup(inline_keyboard=[
    add_return_main_menu(),
    [InlineKeyboardButton(text='vpn_up', callback_data=CallBackData.vpn_up),],
    [InlineKeyboardButton(text='📩  Скачать Логи Программные', callback_data=CallBackData.get_log_program), ],
])

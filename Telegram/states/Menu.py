from aiogram.filters.state import StatesGroup, State


class Menu(StatesGroup):
    main_menu = State()
    admin_menu = State()
    users_menu = State()

from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

IP_MIKROTIK: str | None = config.get('IP_MIKROTIK')
USERNAME_SSH: str | None = config.get('USERNAME_SSH')
PASSWORD_SSH: str | None = config.get('PASSWORD_SSH')
PORT_SSH: int | None = int(config.get('PORT_SSH'))

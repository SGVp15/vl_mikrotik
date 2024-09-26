from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

IP: str | None = config.get('IP')
USERNAME_SSH: str | None = config.get('USERNAME_SSH')
PASSWORD_SSH: str | None = config.get('PASSWORD_SSH')

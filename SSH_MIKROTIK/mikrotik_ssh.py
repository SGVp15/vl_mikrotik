from time import sleep

import paramiko

from SSH_MIKROTIK.config import IP_MIKROTIK, USERNAME_SSH, PASSWORD_SSH, PORT_SSH
from Utils.log import log


def run_command_ssh(commands: tuple, ip=IP_MIKROTIK, username=USERNAME_SSH, password=PASSWORD_SSH,
                    port=PORT_SSH) -> str:
    # Создаем объект SSH клиента
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        output = ''
        # Подключаемся к устройству
        ssh.connect(hostname=ip, username=username, password=password, port=port, timeout=2.0)
        # Выполняем команду
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            sleep(0.5)
            output += stdout.read().decode('utf-8') + stderr.read().decode('utf-8')
        return output
    except Exception as e:
        log(f"Ошибка подключения: {e}")
        return str(e)
    finally:
        ssh.close()

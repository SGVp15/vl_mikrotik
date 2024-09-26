import paramiko

# Создаем объект SSH клиента
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def run_command_ssh(commands: tuple) -> str:
    # Подключаемся к устройству
    try:
        ssh.connect(IP, username=username, password=password, port=PORT_SSH)
        output = ''
        # Выполняем команду
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            output += stdout.read().decode('utf-8')

        print(output)
        return output
    except Exception as e:
        print(f"Ошибка подключения: {e}")

    finally:
        ssh.close()

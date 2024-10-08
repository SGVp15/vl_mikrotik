import asyncio

from Telegram.main import start_bot
from Utils.log import log


async def main():
    tasks = [
        start_bot(),
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    try:
        log.info('BOT START')
        asyncio.run(main())
    finally:
        log.error('BOT STOP')

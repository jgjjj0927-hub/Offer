import asyncio
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers import router

BOT_TOKEN = "8642013882:AAFdDVh_PVp73BK_wRottcRkMKUU73rohUI"


async def main():
    if not BOT_TOKEN or "ВСТАВЬ" in BOT_TOKEN:
        print("[!] BOT_TOKEN не задан.")
        sys.exit(1)

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.include_router(router)

    print("[*] Бот запущен. Нажми Ctrl+C для остановки.")
    await dp.start_polling(bot, drop_pending_updates=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\n[*] Бот остановлен.")

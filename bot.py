import asyncio
import logging

from aiogram import  Dispatcher

from handlers.echo import echo_router
from handlers.menu import menu_router
from handlers.start import start_router
from handlers.dasturlash import programming_router
from handlers.dasturlash_haqida import dasturlash_router
from handlers.grafik_dizayn import graphic_design_router
from handlers.grafik_dizayn_haqida import about_graphic_design_router
from handlers.savodxonlik import savodxonlik_router
from handlers.savodxonlik_haqida import savodxonlik_haqida_router
from handlers.ingliz_tili_haqida import ingliz_tili_haqida_router
from handlers.ingliz_tili import ingliz_tili_router
from loader import bot, db

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
       
    )

    logger.info("Starting bot")

    try:
        db.create_table_users()
    except Exception as err:
        print(err)

    dp: Dispatcher = Dispatcher()

    dp.include_routers(
        start_router,
        menu_router,
        graphic_design_router, 
        programming_router,
        savodxonlik_router,
        dasturlash_router,
        about_graphic_design_router,
        savodxonlik_haqida_router,
        ingliz_tili_router,
        ingliz_tili_haqida_router,
        echo_router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")

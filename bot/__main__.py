from bot import TelegramBot
from bot.server import server, init_app

if __name__ == '__main__':
    init_app()
    TelegramBot.loop.create_task(server.serve())
    TelegramBot.run()

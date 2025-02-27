import DiscordBot.bot as bot
from pytrending import *

if __name__ == '__main__':
    # bot.run_discord_bot()
    df = get_daily_trends()
    print(df)
import bot
from prompts import *

if __name__ == '__main__':
    # bot.run_discord_bot()
    df = get_yearly_trends(2018)
    print(df)
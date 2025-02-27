import discord
import DiscordBot.responses as responses

# Function to send embedded message to dm or channel
async def send_embed(message, user_message, is_private):
    try:
        if user_message == 'help':
            is_private = True
        
        embed = responses.get_response(user_message)
        # if help is requested, dm it to user requesting, else send in main channel
        await message.author.send(embed=embed) if is_private else await message.channel.send(embed=embed)

    except Exception as e:
        print(e)

# run discord bot
def run_discord_bot():
    TOKEN = ''
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    # notify when ready
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to discord!')

    # listen for messages
    @client.event
    async def on_message(message):
        # ignore bot messages
        if message.author == client.user:
            return
        
        # get/print info to terminal
        username = str(message.author)
        user_msg = str(message.content)
        channel = str(message.channel)
        print(f'{username} said: {user_msg} in the {channel} channel.')

        # check for ! commands
        if user_msg[0] == '!':
            user_msg = user_msg[1:]
            await send_embed(message, user_msg, is_private=False)

    client.run(TOKEN)
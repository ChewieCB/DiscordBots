import discord

TOKEN = 'NTkwMjgzMzQ2OTQxMTgxOTgy.XQf-ZA._I5HN8UwKrFLJdigHyfaKoBH6pE'

client = discord.Client()

# list of days in the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


@client.event
async def on_message(message):
    # we don't want the bot replying to itself
    if message.author == client.user:
        return
    # greet busybot
    if message.content.startswith('!hello'):
        _msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(_msg)
    #
    for item in days:
        for _word in message.content.split():
            print(_word)
            if len(_word) > 2 and item.lower().startswith(_word):
                _msg = '{0.author.mention}, are you busy or free on {1}?\n(Respond with !busy or !free to confirm.)'.format(message, item)
                await message.channel.send(_msg)


@client.event
async def confirm(message, item):
    # we don't want the bot replying to itself
    if message.author == client.user:
        return
    # check user response
    if message.content.startswith('!busy'):
        _confirm = '{0.author.mention} is busy on {1}.'.format(message, item)
        await message.channel.send(_confirm)
    elif message.content.startswith('!free'):
        _confirm = '{0.author.mention} is free on {1}.'.format(message, item)
        await message.channel.send(_confirm)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')


client.run(TOKEN)

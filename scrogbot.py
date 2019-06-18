import discord
import random

TOKEN = 'NTkwMjk4MjA4NzA2NDk0NDc1.XQgMGQ.R3RGlZxzq_FPujDqkRbDzsMNpdQ'

client = discord.Client()

scrogdog = ['scrog', 'dog']

scroggedy = (
    'scroggedy doggedy scrog dog',
    'scroggedy doggedy scrog dog dog',
    'scroggedy dog dog',
    'scroggedy scrog dog',
    'scrog dog',
    'doggedy scrog dog',
    'doggedy scrog',
    'scroggedy dog'
)


@client.event
async def on_message(message):
    # we don't want the bot replying to itself
    if message.author == client.user:
        return
    # greet scrogbot
    if message.content.startswith('!hello'):
        _rand_bool = bool(random.getrandbits(1))
        _msg = scrogdog[_rand_bool]
        await message.channel.send(_msg)
    if 'scrog my dog' in message.content.lower():
        scrog_list = ["\N{Multiple Musical Notes}"]
        for x in range(random.randint(1, 5)):
            scrog_list.append(random.choice(scroggedy))

        scrog_print = '\n\t'.join(scrog_list)
        scrog_print += "\n\N{Multiple Musical Notes}"
        await message.channel.send(scrog_print)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

client.run(TOKEN)


import discord

TOKEN = 'NzY2ODEwOTUwMjI1MzYyOTQ0.X4oyWQ.diIzYBz3bk0Yb3mRsv7WxPtrZgY'

client = discord.Client()
in_list = []

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('bora?'):
        #msg = 'Hello {0.author.mention}'.format(message)
        msg = 'Bora jogar hoje! manda um "in!" pra entrar na lista!'.format(message)
        await message.channel.send(msg)

    elif message.content.startswith('in!'):
        auth = '- {0.author.name}'
        if auth not in in_list:
            if len(in_list) < 10:
                in_list.append(auth)
                msg = 'Amongãs hoje: '
                for i in in_list:
                    msg = msg+'\n'+i
                msg = msg.format(message)
                await message.channel.send(msg)
                if len(in_list) == 10:
                    msg = 'Já temos 10! lista fechada.'.format(message)
                    await message.channel.send(msg)
            else:
                msg = 'Sinto muito {0.author.name}, já tem 10, fica esperto ai caso alguem desista.'.format(message)
                await message.channel.send(msg)
    
    elif message.content.startswith('out!'):
        auth = '- {0.author.name}'
        if auth in in_list:
            in_list.remove(auth)
            msg = 'Amongãs hoje: '
            for i in in_list:
                msg = msg+'\n'+i
            msg = msg.format(message)
            await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
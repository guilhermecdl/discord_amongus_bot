import discord
import config

horario = [] #o discord nao tava salvando a string, entao vai ficar em uma lista
client = discord.Client()
in_list = []

TOKEN = config.TOKEN

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
        auth = str(message.author.name)
        print(auth)
        if auth not in in_list:
            if len(in_list) < 10:
                in_list.append(auth)
                if len(horario) > 0:
                    ho = horario[-1]
                else: ho = ':'
                msg = 'Amongãs hoje'+ho
                for i in in_list:
                    msg = msg+'\n'+i
                msg = msg.format(message)
                await message.channel.send(msg)
                if len(in_list) == 10:
                    msg = 'Já temos 10! lista fechada.'.format(message)
                    await message.channel.send(msg)
            else:
                msg = f'Sinto muito {message.author.name}, já tem 10, fica esperto ai caso alguem desista.'.format(message)
                await message.channel.send(msg)

    elif message.content.startswith('out!'):
        auth = str(message.author.name)
        if auth in in_list:
            in_list.remove(auth)
            if len(horario) > 0:
                ho = horario[-1]
            else: ho = ':'
            msg = 'Amongãs hoje'+ho
            for i in in_list:
                msg = msg+'\n'+i
            msg = msg.format(message)
            await message.channel.send(msg)

    elif message.content.startswith('!among us'):
        cont = message.content
        cont = cont.split(' ')
        if len(cont) == 3:
            hora = cont[2]
            if 'h' not in hora:
                msg = f'{message.author.mention} só entendo horario no formato XXh ou XXhXX'
                msg = msg.format(message)
                await message.channel.send(msg)
                return    
            elif len(hora) == 3:
                h = hora[:-1]
                m = 0
            elif len(hora) == 5:
                h = hora[:2]
                m = hora[-2:]
            else:
                msg = f'{message.author.mention} só entendo horario no formato XXh ou XXhXX'
                msg = msg.format(message)
                await message.channel.send(msg)
                return                
            print(h) #! for testing
            try:
                h = int(h)
                m = int(m)
                if h > 24 or h < 0:
                    msg = f'O dia só tem 24h {message.author.mention}...'
                    msg = msg.format(message)
                    await message.channel.send(msg)
                    return
                if m > 59 or m < 0:
                    msg = f'Uma hora só tem 60 minutos {message.author.mention}...'
                    msg = msg.format(message)
                    await message.channel.send(msg)
                    return       

                horario.append(' '+hora+':')
                msg = f'Marcado pras '+hora
                msg = msg.format(message)
                await message.channel.send(msg)


            except ValueError:
                msg = f'{message.author.mention} só entendo horario no formato XXh ou XXhXX'
                msg = msg.format(message)
                await message.channel.send(msg)
                return



            

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
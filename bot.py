import discord

from discord.ext import commands

from discord import Activity, ActivityType

import asyncio

import json

bot = commands.Bot(command_prefix='>')

@bot.event

async def on_voice_state_update(member,before,after):

    if after.channel.id == 832025063044939856:

        mainCategory = discord.utils.get(member.guild.categories, id=825726760972714014)

        channel2 = await member.guild.create_voice_channel(name=f"🚬 Комната {member.display_name}",category=mainCategory)

        await member.move_to(channel2)

        await channel2.set_permissions(member,mute_members=True,move_members=True,manage_channels=True)

        def check(a,b,c):

            return len(channel2.members) == 0

        await bot.wait_for('voice_state_update', check=check)

        await channel2.delete()

@bot.event

async def on_ready():

    print("Бот запустился")

    await bot.change_presence(status=discord.Status.idle,activity=Activity(name="Порнуху",type=ActivityType.watching))

a = ['гей','пидарас','КТО ВЗАИМКУ В ЛС','Кто хочет голды в лс','Кому голды в лс']

@bot.event

async def on_message(message):

	if message_author == bot.user:		return

	else:

			content = message.content.split()

			for word in--content:

				if word in a:

					await message.delete()

					await message.channel.send('Еще́ раз напишешь такое gg тебе')

	await bot.process.commands(message)

	

@bot.event

async def on_message(message):

    with open('/storage/emulated/0/MyBot/lvl.json','r') as f:

        users = json.load(f)

    async def update_data(users,user):

        if not user in users:

            users[user] = {}

            users[user]['exp'] = 0

            users[user]['lvl'] = 1

    async def add_exp(users,user,exp):

        users[user]['exp'] += exp

    async def add_lvl(users,user):

        exp = users[user]['exp']

        lvl = users[user]['lvl']

        if exp > lvl:

            await message.channel.send(f'<a:a_black_tick:817214655176376371> {message.author.mention} **о ебать + 1уровень, хуя ты общительный:/** <a:a_black_tick:817214655176376371>')

            users[user]['exp'] = 0

            users[user]['lvl'] = lvl + 1

    await update_data(users,str(message.author.id))

    await add_exp(users,str(message.author.id),0.1)

    await add_lvl(users,str(message.author.id))

    with open('/storage/emulated/0/MyBot/lvl.json','w') as f:

        json.dump(users,f)

        

	

bot.run('ODMyMjM0NDcyMDE5NTkxMTk4.YHg0wA.QcZ8U7K_Wq-DdQMbnlNvtCxbVnc')

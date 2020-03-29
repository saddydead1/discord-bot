import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix = '.')

@Bot.event

async def on_ready():
    print('Bot started')

@Bot.command()

async def hello(ctx):
    await ctx.send("hello")

@Bot.command()
@commands.has_permissions(administrator = True)
async def mute(ctx, member: discord.Member):
    await member.add_roles(discord.utils.get(ctx.message.guild.roles, name = "mute"))
    await ctx.send("Muted complete")

@Bot.command()
@commands.has_permissions(administrator = True)
async def unmute(ctx, member: discord.Member):
    await member.delete_roles(discord.utils.get(ctx.message.guild.roles, name = "mute"))
    await ctx.send("Unmuted complete")


#connect
token = open ( 'token.txt', 'r' ).readline() 
Bot.run( token )   

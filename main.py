import discord
import os
from discord.ext import commands

from comandos.guia import GuiaView

TOKEN = os.getenv("TOKEN")

intents: discord.Intents = discord.Intents.all()
def get_prefix(bot: commands.Bot | discord.AutoShardedBot, msg: discord.Message):
    if not bot.user:
        return ["!"]
    return ["!", f"<@{bot.user.id}> ", f"<@!{bot.user.id}> "]

bot = commands.Bot(command_prefix=get_prefix,
                   intents=intents,
                   description='Bot oficial del Ejército General del Orden')



@bot.command()
@commands.has_permissions(administrator = True)
async def reload(ctx: commands.Context[commands.Bot], command: str = "", sync: bool = False):
    """Recarga todas las extensiones del bot"""

    if command:
        extension_name = f"comandos.{command}"
        try:
            bot.reload_extension(extension_name)
            await ctx.send(f"Se recargo el comando: {command}")
        except discord.ExtensionNotLoaded:
            bot.load_extension(extension_name)
            await ctx.send(f"Se cargo el comando: {command}")
        except discord.ExtensionNotFound:
            await ctx.send(f"No existe el comando: {command}")
    else:
        extensions = list(bot.extensions.keys())
        for extension in extensions:
            bot.reload_extension(extension)
        await ctx.send('Todas las extensiones han sido recargadas.')

    if sync:
        await bot.sync_commands()

for filename in os.listdir('./comandos'):
    if filename.endswith('.py'):
        bot.load_extension(f'comandos.{filename[:-3]}')

# Eventos
@bot.event
async def on_ready():
  print(f'Conectado a Discord como {bot.user}')


bot.run(TOKEN)


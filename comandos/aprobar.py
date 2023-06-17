import datetime
from typing import Dict, Optional
import discord
import re
from discord.ext import commands
from discord.utils import get
import asyncio


class Aprobar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.miembros_aprobados: Dict[int, str] = {}
        self.evaluadores: Dict[int, discord.User | discord.Member] = {}
        self.channel: Dict[int, discord.abc.MessageableChannel] = {}
        self._canal_invitacion = None

    @commands.Cog.listener()
    async def on_ready(self):
        self._canal_invitacion = self.bot.get_guild(1073709568703602785).get_channel(1073709570733658154)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 1073709568703602785 and member.id in self.miembros_aprobados:
            minecraft_nick = self.miembros_aprobados[member.id]
            ahora = int(datetime.datetime.now().timestamp())
            await member.edit(nick=f"【REC】 {minecraft_nick}")
            registro = f"`{self.evaluadores[member.id]}` aprobó a `{member} ({minecraft_nick})` y autorizó su ingreso a la facción oficialmente el <t:{ahora}:F>"
            await self.channel[member.id].send(registro)
            # Enviar mensaje al canal especificado con el nick válido y la fecha de ingreso
            canal_mensaje = self.bot.get_guild(1082500682533306439).get_channel(1083112404679934044)
            mensaje_ingreso = f"------------------------------------------\n**Entrada registrada**\nNick: {minecraft_nick}\nFecha: <t:{ahora}:F>\n------------------------------------------"
            await canal_mensaje.send(mensaje_ingreso)
            del self.miembros_aprobados[member.id]  # Eliminar el miembro de la lista después de cambiar el apodo
            del self.evaluadores[member.id]  # Eliminar el miembro que ejecutó el comando luego de que se registre que el usuario ingresó al servidor
            del self.channel[member.id]  # Eliminar el canal de la lista luego de que se registre que el usuario ingresó al servidor
    @commands.command(help = "El bot invitará automáticamente al servidor principal al usuario etiquetado")
    @commands.has_any_role(1073835819875450912, 1073835819875450914,
                       1073835819875450915, 1073835819875450916)
    async def aprobar(self, ctx: commands.Context, member: discord.Member):
        if ctx.guild != member.guild:
            await ctx.send("El usuario que indicaste no se encuentra en el servidor.")
            return
        await member.send("\n¡Enhorabuena, me alegra informarle que su __examen de ingreso al **Ejército General del Orden** ha sido **APROBADO**__\n **Antes de invitarlo al servidor principal, indíqueme su nombre de usuario de Minecraft.**")
        await ctx.message.add_reaction("👍🏿")

        while True:
            minecraft_nick = await get_minecraft_nick(ctx, member)
            msg = await member.send(f"\n**¿Es este su nick de Minecraft?** \n\n> `{minecraft_nick}`\n\n`Si es así reaccione con '✅', caso contrario reaccione con '❌'`")
            await msg.add_reaction("✅")
            await msg.add_reaction("❌")

            def check(reaction, user):
                return user == member and str(reaction.emoji) in ["✅", "❌"]

            reaction, user = await ctx.bot.wait_for('reaction_add', check=check)
            emoji = str(reaction.emoji)

            if emoji == "❌":
                await member.send("Corrija su nick en el siguiente mensaje.")
                continue
            elif emoji == "✅":
                if self._canal_invitacion:
                    invitacion = await self._canal_invitacion.create_invite(max_uses=1, max_age=604800, unique=True)
                    mensaje = f"Perfecto, su nick ha sido registrado como {minecraft_nick}. Esta es la invitación al servidor, ingrese para continuar: {invitacion.url}\n\n **IMPORTANTE:**\n• Verifíquese como `recluta` para tener acceso a los principales canales del servidor.\n\n **ACLARACIONES:**\n_• En la facción hay actividades diarias a las cuales debe asistir, las miamas se indican por el canal `#actividades`\n• Si usted no puede presentarse, llega tarde o se debe retirar de una actividad, justifique el motivo en el canal `#justificación` \n• El uniforme de servicio está disponible a partir del rango Voluntario de 4ta (revisar `#orden`)\n• Ante cualquier duda utilice el canal `#soporte` para resolver sus inquietudes._\n\nDesarrollado por <@764932041015427073>, cualquier duda contáctese con él.\n© EGO"
                    await member.send(mensaje)
                rol_add = get(member.guild.roles, name="╭---╮➣ Recluta")
                rol_rem = get(member.guild.roles, name="╭---╮➣ Ingresante")
                await member.remove_roles(rol_rem) # type: ignore
                await member.add_roles(rol_add) # type: ignore
                break
        self.miembros_aprobados[member.id] = minecraft_nick
        self.evaluadores[member.id] = ctx.author
        self.channel[member.id] = ctx.channel




def setup(bot):
    bot.add_cog(Aprobar(bot))




async def get_minecraft_nick(ctx, member: discord.Member) -> str:
    def check(ctx: commands.Context) -> bool:
        return ctx.channel == member.dm_channel and not ctx.author.bot

    minecraft_nick = ""
    intentos = 0  # variable para controlar el envío de mensajes

    while intentos <= 12:
        try:
            respuesta = await ctx.bot.wait_for('message', check=check, timeout=7200.0)
            intentos += 1   # establecer como False después de recibir una respuesta

            minecraft_nick = respuesta.content
            if re.match("^[a-zA-Z0-9_]{3,16}$", minecraft_nick):
                break
            else:
                await member.send("Ese no es un nick válido de Minecraft. Por favor intente de nuevo.")

        except asyncio.TimeoutError:
            await member.send("Le repito, antes de invitarlo al servidor debe confirmar su nick de Minecraft. Responda en el siguiente mensaje.")
    return minecraft_nick


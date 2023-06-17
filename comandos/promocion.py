from typing import Optional, Set
import discord
from discord.utils import get
from discord.ext import commands
import asyncio



class Promocion(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot: commands.Bot = bot

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def promocion(self, ctx: commands.Context[commands.Bot], promocion: int,
                      *miembros_promocionados: discord.Member) -> None:
    num_promocion: str = str(promocion).zfill(3) # Rellenar el número de promoción con ceros hasta que tenga una longitud de 3 caracteres
    miembros_validos: Set[discord.Member] = set()
    for miembro in miembros_promocionados:
      if any(r.id == 1073709569697660947 for r in miembro.roles):
        miembros_validos.add(miembro)
      else:
        await ctx.send(f'El miembro {miembro.mention} no es recluta, por lo que es imposible promocionarlo.')

    # Lista de menciones a miembros válidos
    menciones: str = ", ".join([m.mention for m in miembros_validos])

        # Obtener los roles recluta y voluntario de 4ta del server principal
    ejercito_union: Optional[discord.Guild] = ctx.bot.get_guild(1073709568703602785)
    if not ejercito_union:
      return

    rol_recluta: Optional[discord.Role] = ejercito_union.get_role(1073709569697660947)
    rol_voluntario: Optional[discord.Role] = ejercito_union.get_role(1073709569752178749)

    if not rol_recluta:
      return
    if not rol_voluntario:
      return

        # Mensaje de confirmación
    mensaje_confirmacion: discord.Message = await ctx.send(f'¿Desea promocionar a {menciones} con la promoción {num_promocion}?')
    await mensaje_confirmacion.add_reaction('✅')

    def confirmacion(reaction: discord.Reaction, user: discord.User):
      return user == ctx.author and str(reaction.emoji) == '✅'

    try:
      await ctx.bot.wait_for('reaction_add',
                                              timeout=60.0,
                                              check=confirmacion)
    except asyncio.TimeoutError:
      await ctx.send('No se recibió una confirmación, la promoción se cancela.')
      return

    # Ejecutar la promoción
    await ctx.send(f'Los miembros {menciones} serán promocionados.')
        # Dar y quitar los roles anteriormente mencionados
    for miembro in miembros_validos:

      await miembro.remove_roles(rol_recluta)
      await miembro.add_roles(rol_voluntario)

    # Crear el mensaje de ascenso
    msjascenso: str = """
  ╒══════════════════════════════════════╕

  ◦ Ascenso por: `Reglamento`

  ◦ Redacta: `Cuerpo de Instrucción Militar`

  ◦ Todos los presentes en esta lista, han ascendido de manera satisfactoria. Felicitamos, esto es resultado de su desempeño y como lograron mostrar lo merecido que es su ascenso. Recuerden no ser conformistas, pueden dar mucho más de lo que ya hacen.

  ╘═════════════════════════════════════╛

  """

    ascensos: str = "\n".join(f"{member.mention} | Recluta [OR-0] -----------► Voluntario de 4ta [OR-1]" for member in miembros_validos)
    msjascenso += ascensos
    msjascenso += "\n\n<@&1073709569357914168>"
    canal_ascenso = ctx.bot.get_channel(1073709572243607626)
    last_id: int = 0
    if not ctx.guild:
      return
    for member in ctx.guild.members:
      nick: str = member.display_name
      start_index: int = nick.find('「')
      end_index: int = nick.find('」')
      if start_index != -1 and end_index != -1:
        id_str = nick[start_index + 1:end_index]
        try:
          id_num: int = int(id_str)
          last_id = max(last_id, id_num)
        except ValueError:
          pass


  # Asignar un nuevo apodo a cada miembro promocionado


    for miembro in miembros_validos:
      last_id += 1
      # Rellenar el número de identificación con ceros hasta que tenga una longitud de 4 caracteres
      id_str: str = str(last_id).zfill(4)
      # Eliminar el texto "【REC】" al inicio del apodo del miembro
      display_name: str = miembro.display_name.replace('【REC】', '', 1).strip()
      # Filtrar los caracteres no admitidos en los nicks de Minecraft
      display_name = filter_minecraft_chars(display_name)
      new_nick: str = f'【7.{num_promocion}】{display_name}「{id_str}」'
      # Verificar si el nuevo apodo supera el límite de 32 caracteres
      if len(new_nick) > 32:
        # Truncar el nuevo apodo para que no supere el límite de 32 caracteres
        new_nick = new_nick[:32]
      await miembro.edit(nick=new_nick)

    await canal_ascenso.send(msjascenso) # type: ignore

    # Crear el mensaje de promoción y definir una cadena inicial
    mensaje_promocion: str = f"═══════════════════════════════════════\n\n ◦ 𝘗𝘳𝘰𝘮𝘰𝘤𝘪ó𝘯 𝘯ú𝘮𝘦𝘳𝘰 {num_promocion} \n\n═══════════════════════════════════════\n\n"

    # Para cada miembro válido en la lista de miembros
    for miembro in miembros_validos:

      # Obtener el apodo del miembro
      apodo_miembro: str = miembro.display_name

      # Centrar el apodo de miembro alrededor de la flecha
      flecha = "──────────────────➣"
      ancho_total = 32 # la longitud de la cadena de la flecha
      apodo_centrado = apodo_miembro.center(ancho_total - len(flecha), " ")

      # Agregar una línea al mensaje_promocion con una mención al miembro, la flecha y su apodo centrado
      mensaje_promocion += f"【REC】{miembro.mention} {flecha} `{apodo_centrado}`\n"

    # Agregar una línea al mensaje_promocion y una mención "@here"
    mensaje_promocion += f"\n ═══════════════════════════════════════\n@here"

    # Obtener el canal de promociones y enviar el mensaje_promocion
    canal_promocion = ctx.bot.get_channel(1073835820408119327)  # ID del canal de promociones
    await canal_promocion.send(mensaje_promocion) # type: ignore



      # Obtener el objeto del servidor "1073840321483526165"
    intendencia: Optional[discord.Guild] = ctx.bot.get_guild(1073840321483526165)

    if not intendencia:
      return
      # Obtener el objeto de la categoría "1073840323639398424" #VOLUNTARIADO 3: 1119706071225868370
    voluntariado: Optional[discord.CategoryChannel] = get(intendencia.categories, id=1119706071225868370)

      # Canal "asuntos generales"
    asuntos_generales = ctx.bot.get_channel(1073840322406273026)

    for miembro in miembros_validos:

          # Agarra el apodo de los miembros válidos del servidor principal
      apodo_int: str = miembro.display_name

          # Crear un canal con el apodo del miembro en la categoría especificada
      canal: discord.TextChannel = await intendencia.create_text_channel(apodo_int, category=voluntariado)



          # Crear el mensaje con la mención al canal creado
      mensaje: str = f'Se ha creado el canal {canal.mention} para el miembro de la promoción {num_promocion}'

          # Enviar el mensaje en el canal especificado
      await asuntos_generales.send(mensaje) # type: ignore


def setup(bot: commands.Bot):
  bot.add_cog(Promocion(bot))

# Asignar un nuevo apodo a cada miembro promocionado
# Crear una función para filtrar los caracteres no admitidos en los nicks de Minecraft
def filter_minecraft_chars(text: str):
  # Definir los caracteres admitidos en los nicks de Minecraft
  allowed_chars: Set[str] = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
  # Filtrar los caracteres no admitidos
  filtered_text = ''.join(c for c in text if c in allowed_chars)
  return filtered_text




from typing import Optional
import discord
from discord.ext import commands, pages


      
def miembros_enlistados(escuadra: discord.Role, mando: discord.Role, submando: discord.Role):
    mandos = mando.members
    submandos = submando.members

    # Obtener miembros que son parte de la escuadra pero no son parte del rol de mando o submando
    miembros = [miembro for miembro in escuadra.members if miembro not in mandos and miembro not in submandos]
    miembros_ordenados = sorted(miembros, key=lambda m: m.display_name) # Ordenar los miembros por nombre

    # Obtener miembros que son parte del rol de mando o submando y también son parte de la escuadra
    mandos_en_escuadra = [miembro for miembro in mandos if miembro in escuadra.members]
    submandos_en_escuadra = [miembro for miembro in submandos if miembro in escuadra.members]

    # Remover los miembros que ya están en la lista de mandos y submandos
    miembros_sin_mandos = [miembro for miembro in miembros_ordenados if miembro not in mandos_en_escuadra and miembro not in submandos_en_escuadra]

    # Convertir las listas a strings
    mandos = "\n".join([f"• {mando.mention}" for mando in mandos])
    miembros = "\n".join([f"• {miembro.mention}" for miembro in miembros_sin_mandos])
    submandos = "\n".join([f"• {submando.mention}" for submando in submandos])

    return f"""
    **Mando ↴**
    {mandos}

    **SubMandos ↴**
    {submandos}

    **Miembros ↴**
    {miembros}
    """

class EscView(discord.ui.View):

    def __init__(self, bot):
        super().__init__(timeout=None) # No tiene que tener timeout para ser persistente

        self.bot = bot

        # Una pagina puede tener multiples embeds
        self._guiaesc = [
            pages.Page(embeds=[discord.Embed(
            title="𝙴𝚜𝚌𝚞𝚊𝚍𝚛𝚊𝚜", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            > Dentro del **Ejército General del Orden**, las escuadras son unidades militares que agrupan a miembros para cumplir objetivos específicos. Estas unidades se forman para cumplir una o más tareas específicas, y suelen encargarse de realizar diversas actividades para beneficio de la facción.
            """,
            color=16246733
        ).set_footer(text=
                     "© Ejército General del Orden"
        )]),
            
            pages.Page(embeds=[discord.Embed(
            title="𝙾𝚛𝚍𝚎𝚗", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            > Cada una está liderada por un mando (comandante) designado, quien es responsable de tomar decisiones y dar órdenes a los miembros del grupo. Además, las escuadras suelen contar con un gran número de miembros, lo que les permite trabajar con mayor eficacia.
            """, 
            color=16246733
        ).set_footer(text="© Ejército General del Orden")]),

            pages.Page(embeds=[discord.Embed(
            title="𝚃𝚊𝚛𝚎𝚊𝚜", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            > Las tareas que realizan las escuadras pueden variar en función de las necesidades de la facción, y pueden incluir desde organización de actividades hasta operaciones de combate directo. En cualquier caso, las escuadras son fundamentales para el éxito de la facción, y los miembros que aportan a la misma son altamente valorados por su dedicación y habilidades.
            """,
            color=16246733
        ).set_footer(text="© Ejército General del Orden")]),
            
            pages.Page(embeds=[discord.Embed(
            title="¡𝙶𝚛𝚊𝚌𝚒𝚊𝚜 𝚙𝚘𝚛 𝚕𝚎𝚎𝚛!", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            > Esperamos que la lectura haya sido amena y hayas aprendido más sobre la facción.
            
            `Cabe aclarar que al ser miembro de una escuadra (lo cuál es obligación) debes cumplir las tareas encomendadas a las mismas, de lo contrario obtendrás una sanción correspondiente`
            """
        ).set_footer(text="© Ejército General del Orden")])]
        


        self._funcesc = [
            pages.Page(embeds=[discord.Embed(
            title="𝙵𝚞𝚗𝚌𝚒𝚘𝚗𝚊𝚖𝚒𝚎𝚗𝚝𝚘", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            > Las escuadras llevan a cabo tareas específicas designadas por el <@&1073709569659916303>. Cada escuadra está liderada por un mando que se encarga de hacer cumplir las órdenes y asignar tareas a sus miembros. De esta manera, las escuadras operan de manera eficiente y coordinada, asegurando el cumplimiento de las misiones encomendadas por la facción.
            """,
            color=16246733
        ).set_footer(text="© Ejército General del Orden")]
        ),

            pages.Page(embeds=[discord.Embed(
            title="𝙰𝚌𝚝𝚒𝚟𝚒𝚍𝚊𝚍𝚎𝚜", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            > A cada escuadra se le facilita un servidor de Minecraft privado y preconfigurado en el host [PloudOS](https://ploudos.com/) donde se deben llevar a cabo las actividades que realicen. Es obligatorio que cada miembro de la escuadra contribuya de manera activa en el cumplimiento de las tareas asignadas. Además, estas actividades suelen tener temáticas específicas para mantener la cohesión y motivación del equipo, las mismas se publican en el canal <#1088298848855806022> con al menos 1 semana de antelación.
            """,
            color=16246733
        ).set_footer(text="© Ejército General del Orden")]
        ),

            pages.Page(embeds=[discord.Embed(
            title="𝙲𝚘𝚖𝚙𝚕𝚎𝚖𝚎𝚗𝚝𝚘𝚜", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            > Como se mencionó anteriormente, el servidor que se ofrece a las escuadras viene preconfigurado con una serie de complementos (plugins) por defecto. A continuación se proporcionará información detallada sobre el servidor, así como la lista de complementos y sus enlaces correspondientes para que puedan ser estudiados y se pueda verificar su legitimidad.
            
            > **Información de los servidores**
            ◦ Host: [PloudOS](https://ploudos.com/)
            ◦ Versión: **1.16.5** NATIVA _(Versión de los plugins y complementos)_. Funciona desde **1.8** hasta **1.19.3**
            ◦ Software: [Paper](https://papermc.io/)

            > **Lista de plugins**
            ◦ [EssentialsX](https://essentialsx.net/): Agrega elementos esenciales para cualquier servidor de Minecraft, como comandos básicos, protección, teletransporte y más. Tiene una configuración sencilla de leer y es importante estudiarlo (**Revisar Wiki**).
            ◦ [HolographicDisplays](https://dev.bukkit.org/projects/holographic-displays): Permite crear y mostrar hologramas en el juego, útiles para mostrar información como el nombre de una tienda o un letrero informativo.
            ◦ [DiscordSRV](https://www.spigotmc.org/resources/loginsecurity.3976/): Plugin para enlazar a los usuarios de Minecraft con su cuenta de Discord. (BETA)
            ◦ [LuckPerms](https://luckperms.net/): Un plugin de permisos avanzado que permite una gestión detallada de los permisos y grupos de jugadores.
            ◦ [Multiverse-Core](https://www.spigotmc.org/resources/multiverse-core.390/): Permite crear múltiples mundos en el servidor y personalizarlos según las necesidades del juego.
            ◦ [SkinsRestorer](https://www.spigotmc.org/resources/skinsrestorer.2124/): Permite a los jugadores usar skins personalizadas en el servidor, incluso si no tienen la skin original en su cuenta de Minecraft.
            ◦ [ViaVersion](https://viaversion.com/): Permite a los jugadores con diferentes versiones de Minecraft conectarse al servidor sin problemas, lo que permite a los jugadores con versiones antiguas unirse al servidor.
            ◦ [WorldEdit](https://worldedit.enginehub.org/): Una herramienta poderosa que permite a los jugadores editar grandes áreas de tierra, crear estructuras y más con comandos simples.
            ◦ [WorldGuard](https://dev.bukkit.org/projects/worldguard): Protege el servidor de daños y alteraciones no deseadas mediante la definición de áreas de protección
            
            Esta lista se puede modificar en cualquier momento y es importante que mantengan actualizados los plugins, nosotros no nos haremos cargo de errores en las actividades.
            """,
            color=16246733
        ).set_footer(text="© Ejército General del Orden")]
        ),
            pages.Page(embeds=[discord.Embed(
            title="¡𝙶𝚛𝚊𝚌𝚒𝚊𝚜 𝚙𝚘𝚛 𝚕𝚎𝚎𝚛!", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            > Aclaramos que cualquier modificación a la guía puede ocurrir sin previo aviso.
            > En caso de cualquier error contactarse con <@764932041015427073>
            """,
            color=16246733
        ).set_footer(text="© Ejército General del Orden")]
        )]




        # Botones customizados para que sean gris y usen el emoji en vez de < >
        self._buttons = [pages.PaginatorButton(button_type="prev", emoji="⬅", custom_id="atras", style=discord.ButtonStyle.gray), # Boton para atras
                    pages.PaginatorButton(button_type="page_indicator", custom_id="indicador", style=discord.ButtonStyle.gray, disabled=True), # Boton indicando la pagina actual / cantidad de paginas
                    pages.PaginatorButton(button_type="next", emoji="➡", custom_id="adelante", style=discord.ButtonStyle.gray)] # Boton para adelante
        # Aparentemente tiene que tener como minimo esos tres

        # Crear el paginador
        

    @discord.ui.button(style=discord.ButtonStyle.secondary, label="Información", custom_id="infoesc", emoji="❔")
    async def boton_info(self, button, interaction):
        # Enviamos la guia
        guia_pag = pages.Paginator(pages=self._guiaesc, use_default_buttons=False, custom_buttons=self._buttons)
        await guia_pag.respond(interaction=interaction, ephemeral=True)
    
    @discord.ui.button(style=discord.ButtonStyle.secondary, label="Funcionamiento", custom_id="funcionamientoesc", emoji="❕")
    async def boton_func(self, button, interaction):
        # Enviamos la guia
        func_pag = pages.Paginator(pages=self._funcesc, use_default_buttons=False, custom_buttons=self._buttons)
        await func_pag.respond(interaction=interaction, ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.secondary, label="Miembros", custom_id="miembrosroles", emoji="👥")
    async def boton_miembros_roles(self, button, interaction):
        guild = self.bot.get_guild(1073709568703602785)
        members1 = miembros_enlistados(guild.get_role(1073709569613766709), guild.get_role(1073709569613766710), guild.get_role(1105561934453022801))
        members2 = miembros_enlistados(guild.get_role(1073709569508917369), guild.get_role(1073709569613766708), guild.get_role(1105561950726926336))
        members3 = miembros_enlistados(guild.get_role(1073709569508917367), guild.get_role(1073709569508917368), guild.get_role(1105561957332942948))

        miembrosesc = [
            pages.Page(embeds =[discord.Embed(title="Escuadra de Infantería 1 'Covenant'", description=members1, color=16246733).set_footer(text="© Ejército General del Orden")]),
            pages.Page(embeds =[discord.Embed(title="Escuadra de Infantería 2 """, description=members2, color=16246733).set_footer(text="© Ejército General del Orden")]),
            pages.Page(embeds =[discord.Embed(title="Escuadra de Infantería 3 'San Martin'", description=members3, color=16246733).set_footer(text="© Ejército General del Orden")])
            ]

        _miembrosesc = pages.Paginator(pages=miembrosesc, use_default_buttons=False, custom_buttons=self._buttons)
        await _miembrosesc.respond(interaction=interaction, ephemeral=True)
class GuiaEscuadras(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def guiaesc(self, ctx):
        embed = discord.Embed(
            title="Escuadras",
            description="""
El objetivo de este canal es proporcionarte información detallada sobre uno de los principales elementos de nuestra facción: **las escuadras**.

> ◦ Las escuadras son un componente esencial de nuestra organización, por lo que queremos brindarte todo el conocimiento necesario para que puedas entender cómo funcionan y cómo puedes participar en ellas.
> ◦ Para ayudarte en este proceso, hemos creado una serie de botones interactivos que te permitirán navegar fácilmente por toda la información relacionada con las escuadras. Podrás conocer su funcionamiento y todo lo que debes saber para aportar en la tuya.

`Nos aseguraremos de proporcionarte toda la información necesaria para que puedas tomar decisiones informadas y contribuir al éxito de tu escuadra.`
            """,
            color=16246733
        ).set_footer(text="© Ejército General del Orden")

        await ctx.send(embed=embed, view=EscView(self.bot))

    # Se añade la view al bot para que los botones funcionen después de reiniciarlo
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(EscView(self.bot))


def setup(bot: commands.Bot):
  bot.add_cog(GuiaEscuadras(bot))

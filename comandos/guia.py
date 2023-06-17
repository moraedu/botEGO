import discord
from discord.ext import commands, pages


class GuiaView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None) # No tiene que tener timeout para ser persistente

        # añadir boton de links, los botones de url no tienen que tener custom_id para ser persistentes, los demás si
        button_links = discord.ui.Button(label="Redes sociales", emoji="❕", style=discord.ButtonStyle.gray, url="https://linktr.ee/newEGO") 
        self.add_item(button_links)

        # Una pagina puede tener multiples embeds
        self._pages = [
            pages.Page(embeds=[discord.Embed(
            title="𝙶𝚞í𝚊 𝙱á𝚜𝚒𝚌𝚊 🔖", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            **¡Bienvenido al Ejército General del Orden!** 
            Nos complace tenerte aquí y agradecemos tu disposición a prestar servicio activo en busca de la constante mejora.
            
            > Nos comprometemos a acompañarte en este proceso y apoyarte en todo lo que necesites para que puedas integrarte de manera efectiva a nuestro equipo. Estamos convencidos de que tu contribución será valiosa para alcanzar nuestros objetivos y fortalecer nuestra facción.
            """,
            color=16246733
        ).set_footer(text=
                     """
Recuerda que la conscripción es una decisión importante y te agradecemos por elegirnos.
© Ejército General del Orden
"""
        )]),
            
            pages.Page(embeds=[discord.Embed(
            title="𝙸𝚗𝚝𝚛𝚘𝚍𝚞𝚌𝚌𝚒ó𝚗 👋", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            ◦  Este mensaje está diseñado para guiarte de manera clara y concisa, resaltando los puntos más esenciales para que sepas qué hacer en la facción.
            ◦  Queremos que sepas que eres bienvenido y que puedes hacer cualquier pregunta que tengas. Es normal tener dudas y estamos aquí para hacer que tu estadía en el **Ejército General del Orden** sea lo más fácil y accesible posible.
            """, 
            color=16246733
        ).set_footer(text="© Ejército General del Orden")]),

            pages.Page(embeds=[discord.Embed(
            title="𝙰𝚌𝚝𝚒𝚟𝚒𝚍𝚊𝚍𝚎𝚜 💂‍♂️", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            Cada día llevamos a cabo diversas actividades dentro de Minecraft que se publican mediante <#1073709572243607624>, donde podrás encontrar toda la información necesaria. Además, cada semana se establece un <#1073709572243607627> que se decide mediante una votación en la que participan todos los miembros de la facción. 
            > Cabe destacar que, en la facción, no se busca únicamente realizar actividades de carácter militar, ya que se presentarán una gran variedad de eventos, actualizaciones y novedades con el tiempo.  
            """,
            color=16246733
        ).set_footer(text="© Ejército General del Orden")]),
            
            pages.Page(embeds=[discord.Embed(
            title="𝙹𝚎𝚛𝚊𝚛𝚚𝚞í𝚊 🏢", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            La facción cuenta con una estructura [jerárquica](https://es.wikipedia.org/wiki/Jerarqu%C3%ADa) que se compone de diversos niveles con el fin de establecer una clara línea de mando y asegurar que las decisiones y órdenes sean comunicadas y ejecutadas de manera efectiva y eficiente. La puedes encontrar organizada en el canal <#1073709570733658158>
            
            > Si participas activamente en la facción y demuestras un compromiso constante, tendrás la oportunidad de ascender de rango de <@&1073709569697660947> a <@&1073709569752178749>. 
            > Una vez que hayas alcanzado este rango, podrás solicitar tu propio uniforme rellenando el **formulario** que se encuentra en el canal <#1073709572692394121>. 
            
            > Además, si tu desempeño es excepcional, tendrás la posibilidad de ascender aún más en la jerarquía, lo que te permitirá encontrar nuevas formas de contribuir y ayudar a la facción. 
            
            *¡Estamos ansiosos por ver tu progreso y crecimiento en nuestra comunidad!*
            """
        ).set_footer(text="© Ejército General del Orden")]),

            pages.Page(embeds=[discord.Embed(
            title="¡𝙶𝚛𝚊𝚌𝚒𝚊𝚜 𝚙𝚘𝚛 𝚕𝚎𝚎𝚛! ☺", 
            description=
            """
            ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
            Esperamos que este breve resumen te haya brindado una comprensión más clara del funcionamiento de la facción y que encuentres un lugar en nuestra comunidad.

            *¡Recuerda pasarte por <#1073709571660587058> para conversar con tus compañeros!*
            """,
            color=16246733
        ).set_footer(text="© Ejército General del Orden")])
        ]
    
        # Botones customizados para que sean gris y usen el emoji en vez de < >
        self._buttons = [pages.PaginatorButton(button_type="prev", emoji="⬅", custom_id="atras", style=discord.ButtonStyle.gray), # Boton para atras
                    pages.PaginatorButton(button_type="page_indicator", custom_id="indicador", style=discord.ButtonStyle.gray, disabled=True), # Boton indicando la pagina actual / cantidad de paginas
                    pages.PaginatorButton(button_type="next", emoji="➡", custom_id="adelante", style=discord.ButtonStyle.gray)] # Boton para adelante
        # Aparentemente tiene que tener como minimo esos tres

        # Crear el paginador
        


    @discord.ui.button(style=discord.ButtonStyle.secondary, label="Guía", custom_id="guia", emoji="❔")
    async def boton_guia(self, button, interaction):
        # Enviamos la guia
        paginador = pages.Paginator(pages=self._pages, use_default_buttons=False, custom_buttons=self._buttons)
        await paginador.respond(interaction=interaction, ephemeral=True)
        

    @discord.ui.button(style=discord.ButtonStyle.secondary, label="Normas", custom_id="normas", emoji="📖") 
    async def boton_normas(self, button, interaction):
        normas_emb = discord.Embed(
            title="Políticas y Directrices",
            description="Para conocer el reglamento y los procedimientos que usamos más específicamente en la facción haz click **[aquí](https://discord.com/channels/1073709568703602785/1073709570733658157)**\n\nA continuación se encuentran las directrices generales para la facción. Estas reglas son importantes para mantener el orden y garantizar la seguridad de nuestros miembros.\n\nNo se permitirá ningún tipo de promoción de incumplimiento de los [términos y condiciones](https://discord.com/tos) o [directivas de la plataforma](https://discord.com/guidelines).\n───────────────────────────────────\n:one: · **Comportamiento.**\n · Nuestro personal tomará medidas en caso de mala conducta. Este apartado [no busca ser exhaustivo](https://discord.com/safety), por lo que es importante usar el sentido común y el buen juicio en todo momento.\n:two: · **Sé amable con las demás.**\n ·Sigue la regla de oro: «[trata a los demás como te gustaría que te traten](https://discord.com/moderation/1500000178101-303)». Sé respetuoso con los demás y evita hacer sentir mal. No discrimine por ningún motivo, incluidos, entre otros: raza, género, sexualidad, religión o cualquier discapacidad.\n:three: · **Utiliza adecuadamente los canales.**\n · Recuerda que cada canal tiene su propia función. El uso inapropiado de los canales puede molestar a otros miembros que los usan correctamente.\n:four: · **No se permite el contenido NSFW**\n · Queremos que nuestra comunidad sea accesible para todas las edades. Evita publicar [contenido para adultos o sensible](https://es.wikipedia.org/wiki/NSFW). Si no estás seguro de si algo es apropiado, probablemente deberías abstenerte de publicarlo.\n:five: · **Spam y Privacidad**\n · La publicidad no esta permitida, evita enviar mensajes de promoción dentro del servidor o en los mensajes directos.\n · Respeta la privacidad de los demás y no compartas información personal sin su consentimiento, también intenta limitar la información que das sobre ti mismo.",
            color=16246733
        ).set_footer(text="© Ejército General del Orden")
        await interaction.response.send_message(embed=normas_emb, ephemeral=True)

    


class Guia(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def guia(self, ctx):
        embed = discord.Embed(
            title="¡Bienvenido!",
            description=":wave: La misión de este canal es guiarlo durante su ingreso a la facción. Como miembro deberás participar activamente por lo que debes expandir tus conocimientos sobre nuestra comunidad.\n──────── ∘°❉°∘ ────────\n>     Contamos con herramientas que le resultarán de utilidad, como un canal de [soporte](https://discord.com/channels/1073709568703602785/1100790885228232754), espacio para aclarar tus principales inquietudes.\n─────────────────────\n> Junto a este mensaje encontrarás **botones interactivos** que contienen información. Haz click sobre ellos para adentrarte en nuestra comunidad.\n──────── °∘❉∘° ────────\n ¡Esperamos que disfrutes tu estancia en la facción!",
            color=16246733
        ).set_footer(text="© Ejército General del Orden").set_image(url="https://media.discordapp.net/attachments/1100790885228232754/1102255698752057435/Banner_EGO.png?width=1053&height=592")

        await ctx.send(embed=embed, view=GuiaView())


    # Se añade la view al bot para que los botones funcionen después de reiniciarlo
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(GuiaView())


def setup(bot):
    bot.add_cog(Guia(bot))

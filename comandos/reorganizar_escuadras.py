import random
from discord.ext import commands


class ReorgEscuadras(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reorganizar(self, ctx: commands.Context[commands.Bot]) -> None:
        guild = ctx.guild

        if guild is None:
            await ctx.send("No se pudo obtener la información en este servidor")
            return

        # Roles: Escuadra 1, 2 y 3
        role_ids = {1073709569508917367, 1073709569508917369, 1073709569613766709}
        roles_to_assign = list(filter(None, {guild.get_role(role_id) for role_id in role_ids}))
        # Roles: Oficialidad, Suboficiales Supervisores, Suboficiales Técnicos, Suboficialidad, Voluntariado
        member_role_ids = {
            1073709569659916305,
            1073709569659916306,
            1073709569659916307,
            1073709569659916308,
            1073709569697660938,
        }
        member_roles = filter(
            None, {guild.get_role(role_id) for role_id in member_role_ids}
        )
        # Aplanar la lista de miembros: de [[Miembro A, Miembro B], [Miembro C, Miembro D]...] a [Miembro A, Miembro B, Miembro C, Miembro D...]
        members = {member for role in member_roles for member in role.members}

        # Filtrar todos los miembros sin una escuadra asignada
        unassigned_members = list(
            filter(
                lambda member: not any(
                    role in roles_to_assign for role in member.roles
                ),
                members,
            )
        )

        length = len(unassigned_members) // len(roles_to_assign)
        random.shuffle(roles_to_assign)
        for i, role in enumerate(roles_to_assign):
            start = i * length
            end = start + length
            for member in unassigned_members[start:end]:
                await member.add_roles(role)

        remaining = len(unassigned_members) % len(roles_to_assign)

        if remaining > 0:
            filler = random.choice(roles_to_assign)
            for remainder in unassigned_members[-remaining:]:
                await remainder.add_roles(filler)
        await ctx.send(
            f"Se asignaron los siguientes roles de las escuadras aleatoriamente"
        )


def setup(bot: commands.Bot):
    bot.add_cog(ReorgEscuadras(bot))

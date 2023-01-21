#Библиотеки
import discord
from discord.ext import commands
from discord.ext.commands import guild_only

#Класс
class injector(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Удаление сообщений
    @commands.command(aliases = ["удалить", "удали", "очисти", "Очисти", "очистить", "Очистить", "Удали", "clear", "Clear", "delete", "Delete", "purge", "Purge", "del", "Del"])
    @commands.has_permissions(manage_messages = True)   #Выдем права
    async def Удалить(self, ctx, arg):

        await ctx.message.delete()  #Удаляем свое же сообщение
        await ctx.channel.purge(limit = int(arg))

        purge_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), description = f"<:blurple_verified:1063470348777050163> ┆ Очищенно {int(arg)} сообщений")
        await ctx.send(embed = purge_embed)

        print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <Удалить>, было удаленно {int(arg)} сообщений {self}")    #Отчет в консоль

        pass

    #Кик
    @commands.command(aliases = ["кик", "kick", "Kick", "кикнуть", "Кикнуть"])
    @commands.has_permissions(kick_members = True)  #Выдем права
    async def Кик(self, ctx, member: discord.Member, reason = "Не указано"):

        kick_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), description = f"<:blurple_verified:1063470348777050163> ┆ Изгоняем {member} по причине {reason}")

        await member.kick(reason = reason)
        await ctx.reply(embed = kick_embed)

        print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <Кик> {self}")    #Отчет в консоль

        pass

    #Бан
    @commands.command(aliases = ["забань", "забанить", "Забанить", "Бан",  "бан", "ban", "Ban"])
    @commands.has_permissions(ban_members = True)   #Выдем права
    async def Забань(self, ctx, member: discord.Member, reason = 'не указано'):

        ban_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), description = f"<:blurple_verified:1063470348777050163> ┆ {member} навсегда забанен по причине {reason}")

        await member.ban(reason = reason)
        await ctx.reply(embed = ban_embed)

        print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <Забань> {self}")    #Отчет в консоль

        pass

    #Разбан
    @commands.command(aliases = ["разбанить", "разбань", "Разбань", "унбан", "Унбан", "unban", "Unban"])
    @commands.has_permissions(ban_members = True)   #Выдем права
    async def Разбанить(self, ctx, *, member_id: int):

        await ctx.guild.unban(discord.Object(id=member_id))

        unban_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), description = f"<:blurple_verified:1063470348777050163> ┆ Разбаннен {member_id}")
        await ctx.send(embed = unban_embed)

        print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <Разбанить> {self}")    #Отчет в консоль

        pass

#Запуск
def setup(client):
    client.add_cog(injector(client))
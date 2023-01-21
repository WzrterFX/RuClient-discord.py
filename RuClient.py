#Библиотеки
import discord
from discord.ext import commands
import os
import psutil
import sys

#Консоль
os.system("cls && title RuClient")
print("""
                      \033[91mdMMMMb   dMP dMP\033[0m  .aMMMb   dMP     dMP   dMMMMMP  dMMMMb  dMMMMMMP
                     \033[91mdM  dMP  dMP dMP\033[0m  dMP"VMP  dMP     amr   dMP      dMP dMP    dMP   
                    \033[91mdMMMMP   dMP dMP\033[0m  dMP      dMP     dMP   dMMMP    dMP dMP    dMP    
                   \033[91mdMP AM"  dMP aMP\033[0m  dMP.aMP  dMP     dMP   dMP      dMP dMP    dMP     
                  \033[91mdMP dMP   VMMMP"\033[0m   VMMMP"  dMMMMMP dMP   dMMMMMP  dMP dMP    dMP         
                                        \033[91mBy\033[0m WzrterFX#0601
""")

#Префикс
client = commands.Bot(command_prefix=commands.when_mentioned_or("r.", "r!", "r$", "r?", "ru.", "ru!", "ru$", "ru?"), owner_id = ТВОЙ ID)

#Ручная перезагрузка модулей
@client.command(aliases = ["рестарт", "Перезагрузка", "перезагрузка", "restart", "Restart", "reload", "Reload"])
@commands.is_owner()    #Проверка на разработчика
async def Рестарт(ctx):

    restart_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), description= "<:blurple_verified:1063470348777050163> ┆ Я перезагрузился") #Делаем плажку

    await ctx.reply(embed = restart_embed)
    await client.close()    #Не лучший способ завершение бота, но на Windows client.stop не работает

    os.system("RuClient.py")
    
    pass

#Завершение без доступпа к консоли
@client.command(aliases = ["завершение", "завершись", "Завершись", "shut_down", "Shut_down", "exit", "Exit"])
@commands.is_owner()
async def Завершение(ctx):

    shut_down_accepted_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), description="<:blurple_verified:1063470348777050163> ┆ Я завершился") #Делаем плажку

    await ctx.reply(embed = shut_down_accepted_embed)

    await client.change_presence(status=discord.Status.offline)  #Ставим статус offline ибо он долго меняет статус
    await client.close()

    pass

#Характеристики бота
@client.command(aliases = ["cтатус", "status", "Status"])
@commands.is_owner()
async def Cтатус(ctx):
    virtual_memory = psutil.virtual_memory()

    client_stats_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240))

    client_stats_embed.add_field(name="<:blueple_info:1063513754857373776> ┆ RAM используется", value=f"{round(virtual_memory.used / 1000000000, 2)}GB из {round(virtual_memory.total / 1000000000, 2)}GB")
    client_stats_embed.add_field(name="<:blueple_info:1063513754857373776> ┆ CPU используется", value=f"{psutil.cpu_percent()}%")
    client_stats_embed.add_field(name="<:blueple_info:1063513754857373776> ┆ RuClient информация", value=f"Владелец <@!{client.owner_id}>")

    await ctx.reply(embed=client_stats_embed)

    print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <Cтатус>")

    pass

#Список серверов на котором есть клиент
@client.command(aliases = ["сервера", "servers", "Servers"])
@commands.is_owner()
async def Сервера(ctx):
    servers = len(client.guilds)

    servers_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), description = f"<:blueple_info:1063513754857373776> ┆ Я на {servers} серверах")
    await ctx.reply(embed = servers_embed)

    pass

#Проверка соединение
@client.command(aliases = ["пинг", "ping", "Ping"])
@commands.is_owner()
async def Пинг(ctx):

    ping_embed = discord.Embed(color = discord.Color.from_rgb(85, 100, 240), description = f"<:blueple_info:1063513754857373776> ┆ Соединение с клиентом {round(client.latency * 1000)} ms")

    await ctx.reply(embed=ping_embed)

    print("\033[91m [КЛИЕНТ] \033[0m" + f"{ctx.author} использовал <Пинг>, cоединение с клиентом {round(client.latency * 1000)}ms")     #Отчет в консоль

    pass

#Отправка сообщения от лица бота, может пригодится
@client.command(aliases = ["эхо", "echo", "Echo"])
async def Эхо(ctx, *, arg):

    await ctx.message.delete()  #Удаляем свое сообщение

    await ctx.send(arg)

    pass

#Чтение модулей
for filename in os.listdir("./Модули"):
    if filename.endswith(".py"):
        client.load_extension(f"Модули.{filename[:-3]}")  #Убираем разшерение и привязываем

        print("\033[91m [КЛИЕНТ] \033[0m" + f"Модуль {filename} обнаружен") #Отчет в консоль

        pass

#Запуск
client.run("ТВОЙ ТОКЕН")  #Токен совершенно секретный, уникальный
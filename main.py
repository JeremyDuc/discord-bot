import discord
from discord.ext import commands
from discord.utils import get

# creer le bot
bot = commands.Bot(command_prefix='$')
warnings = {}


# detecter quand le bot est allumé
@bot.event
async def on_ready():
    print("Bot prêt")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Réagissez dans le channel Bienvenue !"))


@bot.event
async def on_message(message):
    if message.content == 'cringe':
        await message.add_reaction("<:cringe:809385487215231046>")
    if message.author == 230720809218342912:
        await message.add_reaction("<:cringe:809385487215231046>")
    await bot.process_commands(message)


# creer la commande $cringe
@bot.command()
async def cringe(ctx):
    await ctx.send("Je vais te labourer tes morts")








@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id  # recupere le numero du message
    user = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)


    if canal == 819564129589264398 and message == 819659226959839232 and emoji == "LeagueofLegends":
        print("Grade ajouté !")
        await user.add_roles(get(bot.get_guild(payload.guild_id).roles, name="LEAGUE OF LEGENDS"))
        await user.send("Tu as maintenant accès aux channels League of legends !")


    if canal == 819564129589264398 and message == 819661727377391686 and emoji == "APEX":
        print("Grade ajouté !")
        await user.add_roles(get(bot.get_guild(payload.guild_id).roles, name="BATTLE ROYAL"))
        await user.send("Tu as maintenant accès aux channels Battle Royal !")


    if canal == 819564129589264398 and message == 819659922794610727 and emoji == "CSGO":
        print("Grade ajouté !")
        await user.add_roles(get(bot.get_guild(payload.guild_id).roles, name="CSGO"))
        await user.send("Tu as maintenant accès aux channels CSGO !")


    if canal == 819564129589264398 and message == 819662308866785342 and emoji == "AMONGUS":
        print("Grade ajouté !")
        await user.add_roles(get(bot.get_guild(payload.guild_id).roles, name="AMONG US"))
        await user.send("Tu as maintenant accès aux channels Among Us !")


    if canal == 819564129589264398 and message == 819662063814443028 and emoji == "FORTNITE":
        print("Grade ajouté !")
        await user.add_roles(get(bot.get_guild(payload.guild_id).roles, name="BATTLE ROYAL"))
        await user.send("Tu as maintenant accès aux channels Battle Royal !")


    if canal == 819564129589264398 and message == 819635045056118795 and emoji == "💯":
        print("Grade ajouté !")
        await user.add_roles(get(bot.get_guild(payload.guild_id).roles, name="Membre"))
        await user.send("Tu obtiens le grade membre !")







@bot.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji.name  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id  # recupere le numero du message
    user = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)


    if canal == 819564129589264398 and message == 819659226959839232 and emoji == "LeagueofLegends":
        print("Grade supprimé !")
        await user.remove_roles(get(bot.get_guild(payload.guild_id).roles, name="LEAGUE OF LEGENDS"))
        await user.send("Tu n'as plus accès aux channels League of legends !")


    if canal == 819564129589264398 and message == 819661727377391686 and emoji == "APEX":
        print("Grade supprimé !")
        await user.remove_roles(get(bot.get_guild(payload.guild_id).roles, name="BATTLE ROYAL"))
        await user.send("Tu n'as plus accès aux channels Battle Royal !")


    if canal == 819564129589264398 and message == 819659922794610727 and emoji == "CSGO":
        print("Grade supprimé !")
        await user.remove_roles(get(bot.get_guild(payload.guild_id).roles, name="CSGO"))
        await user.send("Tu n'as plus accès aux channels CSGO !")


    if canal == 819564129589264398 and message == 819662308866785342 and emoji == "AMONGUS":
        print("Grade supprimé !")
        await user.remove_roles(get(bot.get_guild(payload.guild_id).roles, name="AMONG US"))
        await user.send("Tu n'as plus accès aux channels Among Us !")


    if canal == 819564129589264398 and message == 819662063814443028 and emoji == "FORTNITE":
        print("Grade supprimé !")
        await user.remove_roles(get(bot.get_guild(payload.guild_id).roles, name="BATTLE ROYAL"))
        await user.send("Tu n'as plus accès aux channels Battle Royal !")






# phrase
print("Lancement du bot...")

# connecter le bot au serveur
bot.run("ODA5MTc2OTI2MTM1Nzc5MzU5.YCRSvA.1KQjQz6ztpXnwo7_HI8i3mwOXps")

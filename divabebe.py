#this file do all the work about the Diva Bebe discord bot.
#Diva Bebe discord bot allows you to playing every Melike Sahin performance on your Discord server

#first of all we need to import the discord module.
#to import the discord module you need to write this command to the cmd
#--> pip install -U discord
import discord
intents = discord.Intents.all()
bot = discord.Client(intents = intents)

#this async function is about the bot is ready or not ready
@bot.event
async def on_ready():
    print("Diva Bebe simdi hazir")

#this async function role is when you write your regards the bot sends their regards
@bot.event
async def on_message(message):
    #It allows us to print a personalized greeting message by taking the username.
    kullanici = message.author.display_name

    if message.author == bot.user:
        return
    else:
        if message.content == "selamlar divam":
            await message.channel.send("Divan seni selamliyor "+kullanici) 
       #with the await command we make sure that the regards has reached or not

#this function allows us to send a special message from the bot to the user who joined to the server
@bot.event
async def on_member_join(member):
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"Diva bebenizin istediginiz zaman konser verdigi {guildname} adli sunucuya hos geldin")

bot.run("TOKEN ID BURAYA GELECEK")

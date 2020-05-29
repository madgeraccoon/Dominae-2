# Modules
from datetime import datetime, timedelta, timezone, date # Centipeetle by Madison "Maddie" Adger Badger Raccoon, Gay Dragon and Possum Extraordinare
from discord.ext.commands import Bot ##################### Original Dominae (Screengrabbot) by Wobin OwO (robinuniverse)
from discord.ext import commands ######################### Screenplay by Ray William Johnson
from dateutil import parser, tz ########################## Associate Producer: Dick Wolf
from acapyla import acapyla ############################## Date of last major update: 5/28/20
from mutagen.mp3 import MP3
from re import sub, search
from pathlib import Path
import soundfile as sf
import urllib.request
import subprocess
import traceback
import mimetypes
import requests
import discord
import asyncio
import logging
import random
import time
import praw
import json
import sys
import os

# File Paths
cwd = str(Path.home()) + "/.centipeetle" # The following are just filepath ease-of-access variables
aud = cwd + "/audio" # Split into 3 directories: 'centisounds' for cnoise Centi sounds, 'queries' for cquery Madison soundbytes, and 'sound' for cplay sound effects
img = cwd + "/img" # Predefined image directory
sh = cwd + "/sh" # Bash script directory
txt = cwd + "/txt" # Text and json file directory
out = cwd + "/out" # Command output file (including output images) and non-image predefined file directory
rems = cwd + "/rems" # Reminder directory

# Pre-Load Bot Variables
client = commands.Bot(command_prefix='>>')

with open(txt + '/centi.json','r') as cenjs: # First json load; defines important values
    data = json.load(cenjs)
    token = data['token'] # Discord bot token
    centiversion = data['version'] # Purely visual version number
    statrand = data['randstatus'] # Toggle for random status, which is pulled from the responses file
    centistat = data['status'] # When statrand is off, Centi's defined status
    redd_id = data['redd_id'] # PRAW Reddit client ID
    redd_secret = data['redd_secret'] # PRAW Reddit client secret ID
    currconv_key = data['currconv_key'] # cconv API key from currconv
    wttr_key = data['wttr_key'] # cweather API key (from OpenWeatherMap)

reddit = praw.Reddit(client_id=redd_id,client_secret=redd_secret,user_agent='python:centipeetle.randompost:v1.1.0 (by /u/madgeraccoon)')

logging.basicConfig(level=logging.WARNING, format='%(message)s')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler(txt + '/centi.log', 'a'))
print = logger.warning

def urltyper(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg", "image/gif")
    audio_formats = ("audio/mpeg", "audio/ogg", "audio/vorbis", "audio/wav", "audio/x-wav")
    global linkext
    r = requests.head(image_url)
    contype = r.headers["content-type"]
    if contype in image_formats:
        linkext = mimetypes.guess_extension(contype)
        return "image"
    elif contype in audio_formats:
        if contype == "audio/mpeg":
            linkext = ".mp3"
        else:
            linkext = mimetypes.guess_extension(contype)
        return "audio"
    return False

nicelist = ("thank you", "thanks", "love you", "good")
embedicon = 'https://i.imgur.com/GcdZl7c.png' #Replace link to change embed icon
embedcolor = 0x7900CE # Replace "0x7900CE" with "0x{HEX CODE}" to change embed color

# Client Events
@client.event
async def on_ready(): # Run/Defined when Centi is loaded
    now = datetime.now()
    print("Squaw! Centipeetle " + centiversion + " Loaded and Connected!")
    print('Ready at {} \n'.format(now.strftime("%I:%M%p on %A, %B %d, %Y")))
    if statrand == "on":
        with open(txt + "/responses.txt", 'r') as resps:
            randstat = random.choice(resps.readlines())
        status = randstat
    else:
        status = centistat
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.streaming, url="https://twitch.tv/maddoxdragon", name=status))

@client.event
async def on_message(message): # Run/Defined whenever a message is sent
    if message.author == client.user:
        if "https://youtu.be/" in message.content or "https://youtube.com/watch?v=" in message.content:
            pass
        else:
            return
    if message.guild is None and message.author != client.user:
        print("Direct message from " + message.author.name + ": " + message.content)
    await client.process_commands(message)

# Per-Message Bot Variables (Cont)
    channel = message.channel
    author  = message.author

    now = datetime.now() # Gets the current time when a command is run
    justtimey = 'at {} \n'.format(now.strftime("%I:%M%p on %A, %B %d, %Y")) # "at 06:00AM on Wednesday, January 2, 2019"
    embedtimey = '{}'.format(now.strftime("%a at %I:%M%p")) # "Wed at 06:00AM"
    timeydate = 'User: {}\nTime: {} \n'.format(author, now.strftime("%I:%M:%S%p on %A, %B %d, %Y")) # "by madgeraccoon#1983 at 06:00:00AM on Wednesday, January 2, 2019"
    remtimey = '{} at {}'.format(now.strftime("%x"), now.strftime("%I:%M%p")) # 01/02/19 at 06:00AM

    if "{WC}" in message.content or "{ALLWC}" in message.content:
        is_wc = True
        wildcard = list()
        with open(txt + "/responses.txt", 'r') as resps:
            if "{WC}" in message.content:
                for i in resps:
                    if "https://" not in i:
                        wildcard.append(i.rstrip())
            elif "{ALLWC}" in message.content:
                for i in resps:
                    wildcard.append(i.rstrip())
            for word in message.content.split():
                if "{WC}" in word or "{ALLWC}" in word:
                    WC = (random.choice(wildcard)).replace("\\","\n")
                    message.content = message.content.replace("{WC}",WC, 1).replace("{ALLWC}",WC, 1)
    else:
        is_wc = False

    with open(txt + '/centi.json','r') as cenjs:
        data = json.load(cenjs)
        permallow = data['admins']
        pre = data['prefix']
        adm = data['prefix_admin']
        toggle = data['toggle']
        remoteip = data['remoteip']
        remoteport = data['remoteport']
        weather_rightalign = data['weather_rightalign']

# Special Case Rules
    messageUnchanged = message.content
    message.content = message.content.lower()

    # if message.content.startswith("mc » <"): #% Minecraft Chatbot Command Handler
    #     message.content = message.content.rsplit('> ',1)[1]
    #     if not message.content.startswith(pre):
    #         pass

# Function Hole
    async def embuilder(edesc="Embed Description",ename="Embed",eimage=None,efooter=embedtimey,ecolor=embedcolor,eicon=embedicon, ethumb=None): # Function for custom built Discord embeds

        bembed = discord.Embed(description=edesc,color=ecolor)
        bembed.set_author(name=ename, icon_url=eicon)
        if efooter:
            bembed.set_footer(text=efooter)
        if ethumb:
            bembed.set_thumbnail(url=ethumb)
        if eimage:
            bembed.set_image(url=eimage)
        return bembed

    async def playvoice(audiofile = aud + "/sound/gnome.mp3", length = 1): # Function for easy voice chat file playing, given a filepath and a length

        if author.voice is None:
            await channel.send("You're not in a voice channel!")
        if author.voice is not None:
            vcid = author.voice.channel
        voice = await vcid.connect()
        player = voice.play(discord.FFmpegPCMAudio(audiofile))
        await asyncio.sleep(float(length))
        await voice.disconnect()

    async def centirestart():
        print("Restarting..." + "\n" + timeydate)
        os.execl(sys.executable, sys.executable, *sys.argv)

    def print_timey(printarg=""):
        if printarg == "":
            print("Command run!\n{}".format(timeydate))
        else:
            print("{}\n{}".format(printarg,timeydate))

# Bot-Related Admin Commands
    if message.content.startswith(adm + 'restart'): #% Restarts Centi 

        if str(author.id) in permallow:
            await channel.send("Restarting Centi...")
            await centirestart()

    if messageUnchanged.startswith(adm + 'setval'): #% Changes json config values
        rest = messageUnchanged.replace(adm + 'setval ','')
        opts = rest.split(" ",1)
        if opts[0] in data:
            data[opts[0]] = opts[1]
            with open(txt + '/centi.json','w') as cenjs:
                json.dump(data, cenjs, indent=4, sort_keys=True)
            await channel.send("Changed value `" + opts[0] + "` to `" + opts[1] + "`! Restart?")
            msg = await client.wait_for('message', check=lambda message: message.author == author)
            if "y" in msg.content:
                await channel.send("Value successfully changed. Restarting...")
                print_timey("Value '" + opts[0] + "' changed to '" + opts[1] + "'.")
                await centirestart()
            else:
                await channel.send("Value successfully changed.")
                print_timey("Value '" + opts[0] + "' changed to '" + opts[1] + "'.")

        elif opts[0] == adm + "setval":
            valbed = await embuilder(ename="Available JSON Variables", edesc="**Each variable corresponds to a value in the config file:**\n`prefix` - The default command prefix (default: `c`)\n`prefix_admin` - The admin command prefix (default: `$`)\n`status` - The bot's 'Now Playing' status\n`toggle` - The bot's toggled status (default: `ON`)\n`token` - The bot's token\n`version` - The customizable version number displayed in terminal on run")
            await channel.send(embed=valbed)
            print_timey("Help displayed for setval!")
            
        else:
            await channel.send("The specified value doesn't exist in the config!")
            print_timey("Invalid value specified for changing.")

    if message.content.startswith(adm + 'off'): #% Disables Centi
        if str(author.id) in permallow:
            with open(txt + '/centi.json','w') as tog:
                data['toggle'] = "OFF"
                json.dump(data, tog, indent=4, sort_keys=True)
            embed = await embuilder("Centipeetle is now **Away.**","Centipeetle")
            await channel.send(embed=embed)
            print_timey("Centi toggled OFF!")

    if message.content.startswith(adm + 'on'): #% Re-enables Centi from an OFF state
        if str(author.id) in permallow:
            with open(txt + '/centi.json','w') as tog:
                data['toggle'] = "ON"
                json.dump(data, tog, indent=4, sort_keys=True)
            embed = await embuilder("Centipeetle is **back!**","Centipeetle")
            await channel.send(embed=embed)
            print_timey("Centi toggled ON!")

    if toggle == "ON":
        try:

    # Utility/Fun
            if message.content.startswith(pre + 'd'): #% Rolls a specified die

                try:
                    dicey = int(message.content.replace(pre + "d",""))
                    roll = str(random.randint(1, int(dicey)))
                    if str(dicey) == "1":
                        await channel.send("This is going to take a while...")
                        await asyncio.sleep(5)
                        await channel.send("**Almost there...**")
                        await asyncio.sleep(3)
                        await channel.send("Your number is " + roll + ". What did you expect?")
                    elif roll == str(dicey):
                        await channel.send("Rolling the **D" + str(dicey) + "**, **you rolled a natural " + str(dicey) + "!!!** Congratulations!")
                    elif str(dicey) != "1" and roll == "1":
                        await channel.send("Rolling the **D" + str(dicey) + "**, you rolled a natural **one**. Congratulations, your roll sucks!")
                    else:
                        await channel.send("Rolling the **D" + str(dicey) + "**, your number is **" + roll + "**!")
                    print_timey("The Dicepeetle has been cast! Roll = {}".format(roll))
                except:
                    await channel.send("The Dicepeetle wasn't cast. Use natural numbers.")
                    print_timey("The Dicepeetle wasn't cast. Use natural numbers.")

            if message.content.startswith(pre + 'roll'): #% Rolls multiple of a specified die
                rest = message.content.replace(pre + 'roll ','')
                restargs = rest.split('d')
                howmany = restargs[0]
                whatkind = restargs[1]
                if howmany == "%":
                    howmany = "100"
                if whatkind == "%":
                    whatkind = "100"
                endlist = []
                for i in range(int(howmany)):
                    roll = str(random.randint(1, int(whatkind)))
                    endlist.append(roll)
                total = sum(list(map(int, endlist)))
                embed = await embuilder("You rolled a **{}**:\n{}\nTotal: **{}**".format(rest, ', '.join(endlist), total),"Multiroll for {}#{}".format(author.name, author.discriminator))
                await channel.send(embed=embed)
                print_timey("Multi-dice roll cast!")

            if message.content.startswith(pre + 'rate'): #% Gives the user their gay rating

                roll = str(random.randint(0, 100))
                await channel.send("You are " + roll + "% gay! :gay_pride_flag:")
                print_timey("Gay rated! ({}%)".format(roll))

            if message.content.startswith(pre + 'trate'): #% Combination cd20 and crate (d20 roll and gay rating)

                gayrate = str(random.randint(0, 100))
                twentyroll = str(random.randint(1, 20))
                embed = await embuilder("🎲 Rolling the **D20**, your number is **{}**!\n:gay_pride_flag: You are **{}% gay**!".format(twentyroll, gayrate),"Concentrated roll for {}#{}".format(author.name, author.discriminator))
                await channel.send(embed=embed)
                print_timey("Combo roll posted!")

            if message.content.startswith(pre + 'fetch'): #% Grabs a screenfetch of the host computer

                subprocess.check_output(sh + "/cfetch.sh")
                with open(txt + '/screenfetch.txt', 'r') as fetchfile:
                    fetch = fetchfile.readlines()
                for i in fetch[:]:
                    if i == "**\n":
                        fetch.remove(i)
                    if i.endswith(": \n"):
                        fetch.remove(i)
                fetch = "".join(fetch)
                embed = await embuilder(fetch,"Screenfetch")
                await channel.send(embed=embed)
                print_timey("Screenfetch posted!")

            if message.content.startswith(pre + "choose"): #% Chooses from a specified set of options separated by commas or semicolons, or yes/no by default

                rest = message.content.replace(pre + "choose ","")
                if rest == pre + "choose":
                    rest = "yes, no"
                if ";" not in rest:
                    opts = rest.split(",")
                elif ";" in rest:
                    opts = rest.split(";")
                for i in range(len(opts)):
                    if opts[i].startswith(" "):
                        opts[i] = opts[i].lstrip()
                chosen = random.choice(opts)
                await channel.send("I choose option `" + chosen + "`!")
                if len(opts) == 1:
                    await asyncio.sleep(1)
                    await channel.send("Tip: Use commas (or semicolons) to separate different choice options!")
                try:
                    msg = await client.wait_for('message', timeout=5, check=lambda message: message.author == author)
                    if msg.content == "peetle.":
                        profanity = ["golly","gosh","jeez","wow","ugh"]
                        await channel.send("fine!!!! your NEW choice is `{}`! {}!!!!!!".format(random.choice(opts),random.choice(profanity)))
                        print_timey("someone was PICKY and got a SECOND CHOICE")
                    else:
                        print_timey("Random choice! \n({})".format(chosen))
                except asyncio.TimeoutError:
                    print_timey("Random choice! \n({})".format(chosen))

            if message.content.startswith(pre + 'conv'): #% Converts a given amount of one currency to another OR kilometer-mile conversion
                if message.content == pre + 'conv':
                    embed = await embuilder(ename="Currency Conversion",edesc="You forgot to list currencies to convert!\n**Here are some common currencies:**\nUSD\nEUR\nJPY\nGBP\nAUD\nCAD")
                    await channel.send(embed=embed)
                    print_timey("Currency conversion help given!")
                else:
                    rest = message.content.replace(pre + 'conv ','')
                    rest = rest.upper()
                    curs = rest.split(" ",1)
                    fromcur = sub(r"\d+","",curs[0])
                    fromcur = fromcur.strip(".")
                    tocur = curs[1]
                    toamt = sub(r'[^\d]+', '', curs[0])
                    fromto = str(fromcur) + "_" + str(tocur)
                    if toamt == "":
                        toamt = 1
                    if fromcur == "MI" and tocur == "KM":
                        apiret = {}
                        mult = float(toamt) * 1.60934
                    elif fromcur == "KM" and tocur == "MI":
                        apiret = {}
                        mult = float(toamt) / 1.60934
                    else:
                        convurl = "https://free.currconv.com/api/v7/convert?q={}&compact=ultra&apiKey={}".format(fromto,currconv_key)
                        conver = requests.get(url=convurl)
                        apiret = conver.json()
                        mult = float(apiret[str(fromto)]) * float(toamt)
                    try:
                        result = round(mult, 2)
                        embed = await embuilder(ename="Currency Conversion",edesc="**{} {}** is equal to **{} {}!**".format(toamt,fromcur,result,tocur))
                        await channel.send(embed=embed)
                        print_timey("Currencies converted! ({} {} to {} {})".format(toamt,fromcur,result,tocur))
                    except:
                        await channel.send("Invalid currency!")
                        print_timey("Invalid currency type given!")

            if message.content.startswith(pre + 'nether'): #% Minecraft Overworld-Nether distance/portal calculator
                rest = message.content.replace(pre + 'nether ','')
                opts = rest.split(" ")
                if opts[0] == "to":
                    newx = int(float(opts[1])) / 8
                    newz = int(float(opts[2])) / 8
                    worldname = "Nether Coordinates"
                    thumb = "https://gamepedia.cursecdn.com/minecraft_gamepedia/1/18/Nether_Bricks_JE3.png"
                elif opts[0] == "from":
                    newx = int(float(opts[1])) * 8
                    newz = int(float(opts[2])) * 8
                    worldname = "Overworld Coordinates"
                    thumb = "https://gamepedia.cursecdn.com/minecraft_gamepedia/4/44/Grass_Block_Revision_6.png"
                embed = await embuilder(ename=worldname, edesc="Your **coordinates** are:\nX: {}\nZ: {}".format(str(newx),str(newz)), ethumb=thumb, efooter=None)
                await channel.send(embed=embed)
                print_timey("Nether-Overworld distance calculated!")
            
            if message.content.startswith(pre + 'weather'): #% New version of cweather; relies on OpenWeatherMap

                if message.content == pre + 'weather':
                    with open(txt + '/weather.json','r') as wttrjs:
                        weatherdata = json.load(wttrjs)
                    try:
                        rest = weatherdata[str(author.id)]["loc"]
                        wttrunit = weatherdata[str(author.id)]["unit"]
                        if wttrunit == "imperial":
                            wttrunit_speed = "mph"
                            wttrunit_temp = "°F"
                        elif wttrunit == "metric":
                            wttrunit_speed = "kmh"
                            wttrunit_temp = "°C"
                        nodefault = "False"
                    except:
                        rest = "Denver, Colorado"
                        wttrunit = "imperial"
                        wttrunit_speed = "mph"
                        wttrunit_temp = "°F"
                        nodefault = "True"
                else:
                    nodefault = "False"
                    rest = message.content.replace(pre + 'weather ','').replace(' ','+')
                    if "metric" in rest:
                        rest = rest.replace("metric","")
                        wttrunit = "metric"
                        wttrunit_speed = "kmh"
                        wttrunit_temp = "°C"
                    else:
                        wttrunit = "imperial"
                        wttrunit_speed = "mph"
                        wttrunit_temp = "°F"
                os.system('curl "api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}" | jq \'.\' > $HOME/.centipeetle/txt/weatherresult.json'.format(rest,wttrunit,wttr_key))
                with open(txt + "/weatherresult.json",'r') as weatherfile:
                    resultdata = json.load(weatherfile)
                    wttr_temp = int(resultdata["main"]["temp"])
                    wttr_feelslike = int(resultdata["main"]["feels_like"])
                    wttr_name = resultdata["name"]
                    wttr_main = resultdata["weather"][0]["main"]
                    wttr_desc = resultdata["weather"][0]["description"]
                    wttr_icon = resultdata["weather"][0]["icon"]
                    wttr_timezone = int(resultdata["timezone"])
                    wttr_wind = int(resultdata["wind"]["speed"])
                    try:
                        wttr_wind_deg = int(resultdata["wind"]["deg"])
                    except KeyError:
                        wttr_wind_deg = 0
                    try:
                        wttr_rain = str(resultdata["rain"]["1h"])
                    except KeyError:
                        wttr_rain = "0.00"

                dirs = ['↓', '↙', '←', '↖', '↑', '↗', '→', '↘']
                ix = round(wttr_wind_deg / (360. / len(dirs)))
                wttr_dir = dirs[ix % len(dirs)]
                wttr_time = (datetime.now(timezone.utc) + timedelta(seconds=wttr_timezone)).strftime("%I:%M%p")
                weatherstrings = ["{} - {}".format(wttr_name,wttr_time),"=","{0}{1} (feels like {2}{1})".format(wttr_temp,wttrunit_temp,wttr_feelslike),"{} ({})".format(wttr_main,wttr_desc),"{} {} {}".format(wttr_dir,wttr_wind,wttrunit_speed),"{} mm".format(wttr_rain)]
                weatherlongest = len(max(weatherstrings, key=len))
                weatherstrings[1] = weatherstrings[1] * weatherlongest
                if weather_rightalign == "ON":
                    for e, i in enumerate(weatherstrings):
                        weatherstrings[e] = i.rjust(weatherlongest)
                embed = await embuilder(ecolor=0x7ef577,ename="{} Weather".format(wttr_name),edesc="```ml\n{}\n```".format('\n'.join(weatherstrings)))
                embed.set_thumbnail(url="https://openweathermap.org/img/wn/{}@2x.png".format(wttr_icon))
                if nodefault == "True":
                    await channel.send("No default weather location found! To set, please use the command `" + pre + "setweather [location]`.")
                await channel.send(embed=embed)
                print_timey("Weather given for host location!")

            if message.content.startswith(pre + 'wttr'): #% Old version of cweather; relies on wttr.in

                if message.content == pre + 'wttr':
                    with open(txt + '/weather.json','r') as wttrjs:
                        weatherdata = json.load(wttrjs)
                    try:
                        rest = weatherdata[str(author.id)]["loc"]
                        nodefault = "False"
                    except:
                        rest = "@radardetector.ml"
                        nodefault = "True"
                else:
                    nodefault = "False"
                    rest = message.content.replace(pre + 'wttr ','').replace(' ','+')
                subprocess.check_output('curl wttr.in/' + rest.replace(' ','+') + '?0tqp | sed "s/\x1B\[[0-9;]\+[A-Za-z]//g" > $HOME/.centipeetle/txt/weather.txt | date +\'Last updated: %D at %r \' > $HOME/.centipeetle/txt/weatherdate.txt',shell=True)
                with open(txt + "/weather.txt",'r') as weatherfile:
                    centiweather = weatherfile.read()
                centiweather = centiweather.replace("  .", '   ').replace(" "," ")
                embed = await embuilder("```python\n" + centiweather + "```","Weather")
                if nodefault == "True":
                    await channel.send("No default weather location found! To set, please use the command `" + pre + "setweather [location]`.")
                await channel.send(embed=embed)
                print_timey("Weather given for host location! (WTTR STYLE)")
    
            if message.content.startswith(pre + 'setweather'): #% Sets your default weather location and measurement units 
                rest = messageUnchanged.replace(pre + 'setweather ','')
                with open(txt + '/weather.json','r') as wttrjs:
                    weatherdata = json.load(wttrjs)
                try:
                    await channel.send("Weather entry found! Overwriting...\n{} -> {}".format(weatherdata[str(author.id)]["loc"], rest))
                    weatherdata[str(author.id)]["loc"] = rest
                    await channel.send("Would you like your default weather in `metric` or `imperial` units?")
                    msg = await client.wait_for('message', check=lambda message: message.author == author)
                    if msg.content.startswith("m"):
                        weatherdata[str(author.id)]["unit"] = "metric"
                    elif msg.content.startswith("i"):
                        weatherdata[str(author.id)]["unit"] = "imperial"
                    else:
                        await channel.send("Invalid unit! Defaulting to imperial...")
                        weatherdata[str(author.id)]["unit"] = "imperial"
                except KeyError:
                    await channel.send("Weather entry not found! Writing new...\nWould you like your default weather in `metric` or `imperial` units?")
                    wttrentry = {str(author.id): {"loc": rest, "unit": "imperial"}}
                    msg = await client.wait_for('message', check=lambda message: message.author == author)
                    if msg.content.startswith("m"):
                        wttrentry[str(author.id)]["unit"] = "metric"
                    elif msg.content.startswith("i"):
                        pass
                    else:
                        await channel.send("Invalid unit! Defaulting to imperial...")
                        pass
                    weatherdata.update(wttrentry)
                with open(txt + '/weather.json','w+') as wttrjs:
                    json.dump(weatherdata, wttrjs, indent=4, sort_keys=True)
                await asyncio.sleep(1)
                await channel.send("Weather entry set!")
                print_timey("Weather entry set for user!")

            if message.content.startswith(pre + 'embed'): #% Creates a discord embed based on your profile picture and message
                simonmsg = messageUnchanged.replace(pre + 'embed ','')
                await message.delete()
                embed = await embuilder(ename="Embed by {}#{}".format(author.name, author.discriminator), edesc="**" + simonmsg + "**", eicon=author.avatar_url)
                await channel.send(embed=embed)
                print_timey("Custom embed created!")

            if message.content.startswith(pre + 'pfp'): #% Grabs a user's profile picture given a user ID
                uid = message.content.replace(pre + 'pfp ','')
                if message.content == pre + 'pfp':
                    pfpuser = author
                else:
                    if uid.startswith("<@!"):
                        uid = sub('[<>@!]', '', uid)
                    pfpuser = await client.fetch_user(int(uid))
                embed = await embuilder(ename="@{}#{}'s profile picture".format(pfpuser.name, pfpuser.discriminator), eimage=pfpuser.avatar_url, edesc=None)
                await channel.send(embed=embed)
                print_timey("@{}#{}s profile picture grabbed!".format(pfpuser.name,pfpuser.discriminator))
                
            if message.content.startswith(pre + 'quote'): #% Quotes a user's message given a message ID
                qid = message.content.replace(pre + 'quote ','')
                msg = await channel.fetch_message(int(qid))
                msgdatetimey = msg.created_at - timedelta(hours = 6)
                msgdatey = msgdatetimey.strftime("%x")
                msgtimey = msgdatetimey.strftime("%I:%M%p")
                embed = await embuilder(ename="@{}#{}".format(msg.author.name, msg.author.discriminator), efooter="{} at {} CST".format(msgdatey, msgtimey), edesc=msg.content, eicon=msg.author.avatar_url)
                for attachment in msg.attachments:
                    embed.set_image(url=attachment.url)
                await channel.send(embed=embed)
                print_timey("User message quoted!")

    # Chatting (Novelty)
            if 'centi' in message.content and 'how' in message.content and 'day' in message.content: #% Centipeetle, how was your day?

                with open(txt + "/responses.txt", 'r') as resps:
                    response = resps.readlines()
                    chosenresp = random.choice(response).replace("\\","\n")
                    if messageUnchanged.isupper():
                        if "https://" in chosenresp:
                            await channel.send(chosenresp)
                        else:
                            await channel.send(chosenresp.upper())
                    else:            
                        await channel.send(chosenresp)
                    print_timey("How was my day?")

            if message.content.startswith(pre + 'addresp'): #% Adds a response to Centi's pool of responses

                with open(txt + "/responses.txt", 'a') as resps:
                    preless = messageUnchanged.split(" ",1)
                    resps.write(preless[1].replace("\n","\\") + "\n")
                    await channel.send("Response added: `" + preless[1] + "`")
                    print_timey("'" + preless[1] + "' added to the response pool!")

            if message.content.startswith(pre + 'regional'): #% Builds your message out of regional_indicator emojis

                rest = message.content.replace(pre + 'regional ','')
                rest = sub(r'[^A-Za-z0-9 ]+', '', rest)
                numbers = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine", '0': "zero"}
                emojey = []
                for i in list(rest):
                    if i in numbers.keys():
                        emojey.append(":{}:".format(numbers[i]))
                    elif i == " ":
                        emojey.append("  ")
                    elif not i in numbers:
                        emojey.append(":regional_indicator_{}:".format(i))
                await channel.send(''.join(emojey))
                print_timey("Text converted to regional_indicator emojis!\n'{}'".format(rest))

            if 'wasd' in message.content: #% Inside joke; When you are walkin

                outtext = ("https://youtu.be/d_dLIy2gQGU", "I'm walkin\' here!")
                outfiles = (img + "/h.gif", img + "/feelit.png", out + "/walking.mp3", img + "/feeldragon.png", img + "/schlop.png")
                outtype = random.choice(("file", "text"))
                if outtype == "file":
                    outcome = random.choice(outfiles)
                    await channel.send(file=discord.File(outcome))
                if outtype == "text":
                    outcome = random.choice(outtext)
                    await channel.send(outcome)
                print_timey("WASD")

            if 'hi centi' in message.content or 'hello centi' in message.content: #% Greetle the 'Peetle
                
                await channel.send("hi!!!")
                print_timey("hello!!!")

            if 'chaps' in message.content or 'chips' in message.content: #% Reacts to the mention of chips, specifically Chaps

                await message.add_reaction('🥔')
                print_timey("Squaw! (chaps detected)")

            if 'steve' in message.content: #% Reacts to the word 'Steven'...... most of the time
                
                await message.add_reaction('⭐')
                print_timey("Squaw! (Steven detected)")

            if "centi" in message.content and any(x in message.content.lower() for x in nicelist): #% Centipeetle love response
            
                squawchance = random.randint(1, 200)
                if squawchance == 69:
                    await channel.send("congratulations! your kindness to me (centipeetle) has paid off!!! you get a mystery gif")
                    await channel.send(file=discord.File(img + '/cronch.gif'))
                elif "dummy" in message.content:
                    await channel.send(file=discord.File(img + '/angry.gif'))
                else:
                    await channel.send(file=discord.File(img + '/lovepeetle.gif'))
                    print_timey("Love given!")

    # Media
            if message.content.startswith(pre + 'web'): #% Grabs an image from the webcam attached to the host computer

                await message.add_reaction('✋')
                try:
                    subprocess.check_output(sh + "/web.sh")
                    embed = await embuilder(None,"Trashbox Cam","attachment://sweb.png")
                    sweb = discord.File(out + "/sweb.png")
                    await channel.send(embed=embed, file=sweb)
                    print_timey("Webcam image (sweb) uploaded!")
                except subprocess.CalledProcessError as e:
                    await channel.send("`" + pre + "web` has failed! (Perhaps the camera is in use or disconnected?)")
                    print_timey("Webcam image (sweb) failed! (in use?)")
                await message.remove_reaction('✋',client.user)

            if message.content.startswith(pre + 'mov'): #% Grabs a video from the webcam attached to the host computer (MIGHT NOT WORK)

                await channel.send("Recording... Please wait forever. (it takes a while.)")
                subprocess.check_output(sh + "/smov.sh")
                await channel.send(file=discord.File(out + "/smov.webm"))
                print_timey("Webcam (smov) somehow uploaded!")

            if message.content.startswith(pre + 'full'): #% Grabs an image of the host computer's screen

                try:
                    subprocess.check_output(sh + "/full.sh")
                    embed = await embuilder(None,"Trashbox Desktop","attachment://sfull.png")
                    sfull = discord.File(out + "/sfull.png")
                    await channel.send(embed=embed, file=sfull)
                    print_timey("Screenshot (sfull) uploaded!")
                except subprocess.CalledProcessError as e:
                    await channel.send("`" + pre + "full` has failed! (Is X open?)")
                    print_timey("\nDesktop image (sfull) failed! (X open?)")

            if message.content.startswith(pre + 'window'): #% Grabs an image of the host computer's currently focused window

                try:
                    subprocess.check_output(sh + "/window.sh")
                    embed = await embuilder(None,"Trashbox Window","attachment://swindow.png")
                    swindow = discord.File(out + "/swindow.png")
                    await channel.send(embed=embed, file=swindow)
                    print_timey("Desktop window (swindow) uploaded!")
                except subprocess.CalledProcessError as e:
                    await channel.send("`" + pre + "window` has failed! (Is X open?)")
                    print_timey("\nDesktop window (swindow) failed! (X open?)")

            if message.content.startswith(pre + 'video'): #% Reuploads a video from a given source to discord (sometimes)
                simonmsg = messageUnchanged.replace(pre + 'video ','').split()
                if Path(out + '/cvideo.mp4').exists() == True:
                    Path(out + '/cvideo.mp4').unlink()
                if len(simonmsg) == 3:
                    os.system("youtube-dl --postprocessor-args '-ss 0:{} -to 0:{}' -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' {} --output $HOME/.centipeetle/out/cvideo.mp4".format(simonmsg[1], simonmsg[2], simonmsg[0]))
                else:
                    os.system("youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' {} --output $HOME/.centipeetle/out/cvideo.mp4".format(simonmsg[0]))
                try:
                    if (Path(out + '/cvideo.mp4').stat().st_size / 1048576) > 8:
                        await channel.send("Video is too big!")
                        print_timey("Video was too big!")
                    else:
                        await message.delete()
                        await channel.send("Embedded video by `{}#{}`".format(author.name, author.discriminator), file=discord.File(out + '/cvideo.mp4'))
                        print_timey("Video reuploaded!")
                except:
                    await channel.send("Invalid video!")
                    print_timey("Invalid video!")

            if message.content.startswith(pre + 'audio'): #% Reuploads audio from a given source to discord (sometimes)
                simonmsg = messageUnchanged.replace(pre + 'audio ','')
                if Path(out + '/caudio.mp3').exists() == True:
                    Path(out + '/caudio.mp3').unlink()
                os.system("youtube-dl -x --audio-format mp3 {} --output $HOME/.centipeetle/out/caudio.mp3".format(simonmsg))
                try:
                    if (Path(out + '/caudio.mp3').stat().st_size / 1048576) > 8:
                        await channel.send("Audio is too big!")
                        print_timey("Audio was too big!")
                    else:
                        await message.delete()
                        await channel.send("Embedded audio by `{}#{}`".format(author.name, author.discriminator), file=discord.File(out + '/caudio.mp3'))
                        print_timey("Audio reuploaded!")
                except:
                    await channel.send("Invalid audio!")
                    print_timey("Invalid audio!")

            if message.content.startswith(pre + 'give'): #% Grabs an image from a specified repository (or a folder, in the case of cursedcat)

                givetype = message.content.replace(pre + 'give ', '')
                if givetype == pre + "give":
                    subprocess.check_output(sh + "/give.sh")
                elif givetype == "cat":
                    subprocess.check_output(sh + "/cat.sh")
                elif givetype == "dog":
                    subprocess.check_output(sh + "/dog.sh")
                else:
                    subprocess.check_output(sh + "/give.sh " + givetype, shell=True)
                with open(txt + "/give.txt", 'r') as givefile:
                    giveurl = givefile.read()
                await channel.send("Here's your image result for `" + givetype + "`!:\n" + giveurl)
                print_timey("Image given! (cgive)")

            if message.content.startswith(pre + 'col'): #% Creates a solid color image OR color gradient with given color hex values

                target = message.content.replace(pre + 'col ','')
                
                if len(target.split()) >= 2: #Gradient
                    eachcolor = target.split()
                    gradcommand = "convert -size 300x300 \\"
                    newlist = []
                    for i in eachcolor:
                        if i == "random":
                            i = "%06x" % random.randint(0, 0xFFFFFF)
                        if not i.startswith('#'):
                            i = "#" + i
                        newlist.append(i)
                    for cur, nxt in zip (newlist, newlist[1:]):
                        gradcommand = gradcommand + '\n\( gradient:"{}-{}" \) \\'.format(cur, nxt)
                    gradcommand = gradcommand + '\n-append -scale 500x500! -rotate -90 {}/ccol.png'.format(img)
                    barcol = discord.Colour.greyple()
                    coltitle = "{} to {}".format(newlist[0], newlist[-1])
                    os.system(gradcommand)
                    print_timey("Gradient {} to {} generated!".format(newlist[0], newlist[-1]))

                else: #Solid Color
                    if target == "random":
                        target = "%06x" % random.randint(0, 0xFFFFFF)
                    if not target.startswith("#"):
                        target = "#" + target
                    if target[1:] == "ffffff":
                        barcol = 0xFFFFFE
                    else:
                        barcol = int(target[1:], 16)
                    coltitle = target
                    subprocess.check_output('convert -size 300x300 xc:{} {}/ccol.png'.format(target, img), shell=True)
                    print_timey("Color {} generated!".format(target))
                embed = await embuilder(ename=coltitle, eimage="attachment://ccol.png", edesc=None, ecolor=barcol)
                await channel.send(embed=embed, file=discord.File(img + "/ccol.png"))

            if message.content.startswith(pre + 'flag'): #% Creates a flag with given color hex values

                target = message.content.replace(pre + 'flag ','')
                eachcolor = target.split()
                flagcommand = "convert \\"
                for i in eachcolor:
                    if i == "random":
                        i = "%06x" % random.randint(0, 0xFFFFFF)
                    if not i.startswith('#'):
                        i = "#" + i
                    flagcommand = flagcommand + '\n\( -size 100x100 xc:"{}" \) \\'.format(i)
                flagcommand = flagcommand + '\n-append -scale 500x500! {}/cflag.png'.format(out)
                os.system(flagcommand)
                barcol = discord.Colour.greyple()
                embed = await embuilder(ename="Brand New Pride Flag!", eimage="attachment://cflag.png", edesc=None, ecolor=barcol)
                await channel.send(embed=embed, file=discord.File(out + "/cflag.png"))
                print_timey("Flag generated!")

            if message.content.startswith(pre + 'say'): #% Creates an image with the message's text 

                target = messageUnchanged.split(" ",1)
                subprocess.check_output(sh + "/ssay.sh " + "\"" + target[1] + "\"", shell=True)
                await channel.send(file=discord.File(out + '/ssay.png'))
                print_timey("Phrase (ssay) uploaded!\n'{}'".format(messageUnchanged))

            if message.content.startswith(pre + 'fam'): #% Creates an image with the message's text 

                target = messageUnchanged.split(" ",1)
                subprocess.check_output(sh + "/cfam.sh " + "\"" + target[1] + "\"", shell=True)
                await channel.send(file=discord.File(out + '/cfam.png'))
                print_timey("Phrase (cfam) uploaded!\n'{}'".format(messageUnchanged))

            if message.content.startswith(pre + 'fort'): #% Creates an image with the message's text 

                target = messageUnchanged.split(" ",1)
                subprocess.check_output(sh + "/cfort.sh " + "\"" + target[1] + "\"", shell=True)
                await channel.send(file=discord.File(out + '/cfort.png'))
                print_timey("Phrase (cfort) uploaded!\n'{}'".format(messageUnchanged))

            if message.content.startswith(pre + 'halo'): #% Creates an image with the message's text 

                target = messageUnchanged.split(" ",1)
                subprocess.check_output(sh + "/chalo.sh " + "\"" + target[1] + "\"", shell=True)
                await channel.send(file=discord.File(out + '/chalo.png'))
                print_timey("Phrase (chalo) uploaded!\n'{}'".format(messageUnchanged))

            if message.content.startswith(pre + 'craft'): #% Creates an image with the message's text 

                target = messageUnchanged.split(" ",1)
                subprocess.check_output(sh + "/ccraft.sh " + "\"" + target[1] + "\"", shell=True)
                await channel.send(file=discord.File(out + '/ccraft.png'))
                print_timey("Phrase (ccraft) uploaded!\n'{}'".format(messageUnchanged))

            if message.content.startswith(pre + 'food') or message.content.startswith(pre + 'plate') or message.content.startswith(pre + 'redd'): #% Random Reddit post viewer

                exts = [".png",".jp","gfycat","imgur"]
                if message.content.startswith(pre + 'redd'):
                    specsub = message.content.replace(pre + 'redd ','')
                elif message.content.startswith(pre + 'plate'):
                    specsub = 'wewantplates'
                else:
                    specsub = 'shittyfoodporn'
                try:
                    if specsub == "massive":
                        specsub = "mastiff"
                    if reddit.subreddit(specsub).over18:
                        await channel.send("This subreddit is NSFW; please try again!")
                        return
                    ransub = reddit.subreddit(specsub).random()
                    ransub.posturl = "https://reddit.com" + ransub.permalink
                    if ransub.over_18 is True:
                        await channel.send("The random post was NSFW; please try again!")
                        return
                    if ransub.is_self is True:
                        embed = await embuilder("**\"" + ransub.selftext + "\"**\n\n[(by /u/" + ransub.author.name + ")](" + ransub.posturl + ")",ransub.title)
                    else:
                        if any(x in ransub.url for x in exts):
                            embed = await embuilder("[by /u/" + ransub.author.name + "](" + ransub.posturl + ")",ransub.title,ransub.url)
                        else:
                            embed = await embuilder("[by /u/" + ransub.author.name + "](" + ransub.posturl + ")",ransub.title)
                except AttributeError:
                    await channel.send("Error: This subreddit might not support random submissions!")
                    print_timey("Random Reddit post grab (credd) failed!")
                    return
                print("Post ID (in case of failure): " + str(ransub.id))
                await channel.send(embed=embed)
                if ransub.is_self is False:
                    if not any(x in ransub.url for x in exts):
                        await channel.send("`Post content:` " + ransub.url)
                print_timey("Random Reddit post grab (credd) succeeded!")

    # YouTube Commands
            if message.content.startswith(pre + "yt"): # YouTube-related commands

                if message.content.startswith(pre + "ytdl"): #% Finds and downloads a YouTube video
                    preq = message.content.replace(pre + "ytdl ","")
                    target = preq.replace(preq, "\"" + preq + "\"")
                    subprocess.call(sh + '/cdlyt.sh ' + target, shell=True)
                    with open (txt + '/ytitle.txt', 'r') as titlefile:
                        title = titlefile.read()
                    await channel.send("Your download for `" + preq + "` is below! (Title: `" + title.replace("\n","") + "`) (unless the file's too big...)")
                    await channel.send(file=discord.File(out + '/ytgrab.mp3'))
                    print_timey("YouTube mp3 posted!")

                elif message.content.startswith(pre + "yts"): #% Searches for a YouTube video; choose from a list of titles
                    preq = message.content.replace(pre + "yts ","")
                    if preq == pre + "yts":
                        await channel.send("Please type an argument!")
                        print_timey("YouTube search attempted without a query!")
                        return
                    formo = preq.replace(" ","+")
                    target = formo.replace(preq, "\"" + preq + "\"")
                    subprocess.call(sh + '/yts.sh ' + target, shell=True, stderr=subprocess.DEVNULL)
                    with open (txt + '/ytsout.txt', 'r') as ytfile:
                        ytout = ytfile.readlines()
                    embed = await embuilder(None,"Centipeetle YouTube Search")
                    embed.add_field(name="Type in the number of the video you want, or type anything else to cancel.",value="`1.` **" + ytout[6] + "**`2.` **" + ytout[7] + "**`3.` **" + ytout[8] + "**`4.` **" + ytout[9] + "**`5.` **" + ytout[10] + "**", inline=True)
                    embmsg = await channel.send(embed=embed)
                    msg = await client.wait_for('message', check=lambda message: message.author == author)
                    try:
                        if not 1 <= int(msg.content) <= 5:
                            raise ValueError("Invalid number!")
                        else:
                            await embmsg.delete()
                            await channel.send("Your URL for `" + preq + "` is here! (Title: `" + ytout[(int(msg.content) + 5)].strip("\n") + "`): https://youtu.be/" + ytout[int(msg.content)])
                            print_timey("YouTube search for " + preq + " successful! (Option: " + ytout[(int(msg.content) + 5)].strip("\n") + ")")
                    except ValueError:
                        await embmsg.delete()
                        await channel.send("Search cancelled.")
                        print_timey("YouTube search for '" + preq + "' cancelled.")

                elif message.content.startswith(pre + "ytplay"): #% Finds and downloads a YouTube video, then plays it in your current voice chat 
                    if author.voice is not None:
                        preq = message.content.replace(pre + "ytdl ","")
                        target = preq.replace(preq, "'" + preq + "'")
                        subprocess.call(sh + '/cdlyt.sh ' + target, shell=True)
                        with open (txt + '/ytitle.txt', 'r') as titlefile:
                            title = titlefile.read()
                        vcid = author.voice.channel
                        vid = "ytgrab.mp3"
                        vidfile = sf.SoundFile(cwd + "/out/ytgrab.ogg")
                        vidlength = '{}'.format(len(vidfile) / vidfile.samplerate)
                        voice = await vcid.connect()
                        await channel.send("Now Playing: `" + title + "`")
                        player = voice.play(discord.FFmpegPCMAudio(cwd + "/out/ytgrab.ogg"))
                        await asyncio.sleep(float(vidlength))
                        await voice.disconnect()
                        print_timey("Played YouTube audio in voice chat!")

                else: #% (pre + "yt") Finds a YouTube video matching the given search term
                    preq = message.content.replace(pre + "yt ","")
                    formo = preq.replace(" ","+")
                    pretarget = formo.replace(preq, "\"" + preq + "\"")
                    target = pretarget.replace("'","")
                    subprocess.call(sh + '/yt.sh ' + target, shell=True)
                    with open (txt + '/ytout.txt', 'r') as ytfile:
                        ytout = ytfile.readlines()
                    await channel.send("Your URL for `" + preq + "` is here! (Title: `" + ytout[1].strip("\n") + "`): https://youtu.be/" + ytout[0])
                    print_timey("YouTube URL posted!")

    # Audio Commands
            if message.content.startswith(pre + 'play'): #% Plays a specified sound from the sound folder, or gnomes your current voice chat
                rest = message.content.replace(pre + 'play ','')
                mp3file = Path(aud + "/sound/" + rest + ".mp3")
                oggfile = Path(aud + "/sound/" + rest + ".ogg")
                if mp3file.exists():
                    playfile = aud + '/sound/' + rest + '.mp3'
                    sfplayed = MP3(playfile)
                    sflength = sfplayed.info.length
                elif oggfile.exists():
                    playfile = aud + '/sound/' + rest + '.ogg'
                    sfplayed = sf.SoundFile(playfile)
                    sflength = '{}'.format(len(sfplayed) / sfplayed.samplerate)
                else:
                    playfile = aud + '/sound/gnome.mp3'
                    sflength = 1
                print("Playing file: " + playfile)
                await playvoice(playfile, float(sflength))
                print_timey("Audio played!: `{}`".format(rest))

            if message.content.startswith(pre + 'hellgnome'): #% Gnomes voice participants as many times as one specifies
                gnomeamt = message.content.replace(pre + 'hellgnome ','')
                if author.voice is not None:
                    vcid = author.voice.channel
                    voice = await vcid.connect()
                    for i in range(int(gnomeamt)):
                        player = voice.play(discord.FFmpegPCMAudio(aud + "/sound/gnome.mp3"))
                        await asyncio.sleep(1)
                    await voice.disconnect()

            if message.content.startswith(pre + 'noise'): #% Plays a Centipeetle-Brand:tm: Sound Effect
                noiseno = str(random.randint(1, 16))
                noisefile = noiseno + ".wav"
                centisounds = aud + "/centisounds/"
                cenfile = sf.SoundFile(centisounds + noisefile)
                cenlength = '{}'.format(len(cenfile) / cenfile.samplerate)
                await playvoice(centisounds + noisefile, float(cenlength))
                print_timey("Centipeetle noise given!")

            if message.content.startswith(pre + 'query'): #% Okay Google, 
                noiseno = str(random.randint(1, 7))
                noisefile = noiseno + ".wav"
                queries = aud + "/queries/"
                queryfile = sf.SoundFile(queries + noisefile)
                querylength = '{}'.format(len(queryfile) / queryfile.samplerate)
                await playvoice(queries + noisefile, float(querylength))
                print_timey("Okay Google!")
                
            if message.content.startswith(pre + 'vox'): #% Text-to-speech using WillFromAfar from Acapela Group (using Acapyla)
                if message.content.startswith(pre + 'voxplay'): #% Plays the text-to-speech result in your voice chat
                    quote = message.content.replace(pre + "voxplay ","")
                else:
                    quote = message.content.replace(pre + "vox ","")
                quotepts = quote.rpartition('\" ')
                quoteslist = list(quotepts)
                saystr = quoteslist[0] + "\""
                if saystr == "\"":
                    saystr = quoteslist[2]
                if quoteslist[2] == "yoda":
                    quoteslist[2] = "willlittlecreature"
                try:
                    acapyla(saystr,quoteslist[2])
                except:
                    acapyla(saystr)
                if message.content.startswith(pre + 'voxplay'):
                    subprocess.check_output('ffmpeg -y -i ' + out + "/acapyla.mp3 " + out + "/acapyla.ogg", shell=True)
                    voxfile = sf.SoundFile(out + "/acapyla.ogg")
                    voxlength = '{}'.format(len(voxfile) / voxfile.samplerate)
                    await playvoice(out + "/acapyla.ogg", float(voxlength))
                    print_timey("Acapyla Will played! \"{}\"".format(quote))
                else:
                    await channel.send("Your Acapyla file for `" + quote + "` is here!", file=discord.File(out + "/acapyla.mp3"))
                    print_timey("Acapyla Will generated! \"{}\"".format(quote))

    # Reminder Utilities
            if message.content.startswith(pre + 'reminder'): #% Add, edit, list, remove and strike reminders from a user-tailored list

                restUnchanged = messageUnchanged.split(" ", 2)
                try:
                    resttype = restUnchanged[1]
                    try:
                        restcont = restUnchanged[2]
                    except:
                        restcont = "content"
                except:
                    resttype = "help"
                resttype = resttype.lower()
                remfile = rems + "/" + str(author.id) + ".txt"
                if resttype == 'add': # Adds a reminder to a user's list

                    with open(remfile, 'a+') as reminds:
                        reminds.write("**" + remtimey + "**" + " - " + restcont + "\n")
                    await channel.send("Reminder added: `{}`".format(restcont))
                    print_timey("Reminder added!")

                elif resttype == 'edit':

                    rests = restcont.split(" ",1)
                    editno = int(rests[0]) - 1
                    with open(remfile, 'r') as reminds:
                        remlist = reminds.readlines()
                    try:
                        remlist[editno] = rests[1] + "\n"
                        with open(remfile, 'w') as reminds:
                            reminds.writelines( remlist )
                        await channel.send("Reminder {} edited!".format(rests[0]))
                    except ValueError:
                        await channel.send("Invalid reminder number!")
                        print_timey("Invalid reminder number listed for edit.")
                        return
                    print_timey("Reminder {} edited!".format(rests[0]))
                    
                elif resttype == 'remove':

                    if "," in restcont:
                        removenos = restcont.split(",")
                    else:
                        removenos = restcont.split(" ",1)
                    with open(remfile, 'r') as reminds:
                        rem = reminds.readlines()
                    for i in removenos:
                        i = int(i) - 1
                        rem[i] = ""
                    with open(remfile, 'w') as reminds:
                        reminds.writelines( rem )
                    await channel.send("Reminder " + restcont + " removed.")
                    print_timey("Reminder removed!")

                elif resttype == 'strike':

                    if "," in restcont:
                        removenos = restcont.split(",")
                    else:
                        removenos = restcont.split(" ",1)
                    with open(remfile, 'r') as reminds:
                        rem = reminds.readlines()
                    for i in removenos:
                        i = int(i) - 1
                        rem[i] = rem[i].strip("\n")
                        rem[i] = "~~" + rem[i] + "~~\n"
                    with open(remfile, 'w') as reminds:
                        reminds.writelines( rem )
                    await channel.send("Reminder " + restcont + " struck!.")
                    print_timey("Reminder struck!")

                elif resttype == 'clear':

                    try:
                        usrid = str(author.id)
                        os.remove(remfile)
                        await channel.send("Reminders cleared for user `{}` (ID: `{}`)!".format(author.name, usrid))
                        print_timey("Reminders cleared for user `{}` (ID: `{}`)!".format(author.name, usrid))
                    except FileNotFoundError:
                        await channel.send("You have no reminders to clear! (File for user `{}` does not exist)".format(author.name))
                        print_timey("Reminder file for user `{}` does not exist!".format(author.name))

                elif resttype == 'list':

                    with open(remfile, 'r') as reminds:
                        remlist = reminds.readlines()
                    eachrem = []
                    remno = 1
                    for rem in remlist:
                        specrem = remno - 1
                        eachrem.append(str(remno) + ". " + remlist[specrem])
                        remno += 1
                    if 'plaintext' in restcont:
                        await channel.send("Reminders:\n" + ''.join(eachrem))
                        print_timey("Plaintext reminders listed!")
                    else:
                        embed = await embuilder(''.join(eachrem),"Reminders")
                        await channel.send(embed=embed)
                        print_timey("Reminders listed!")

                else:
                    embed = await embuilder(None,"Reminder Commands")
                    embed.add_field(name="All commands are prefixed with `" + pre + "`", value="**reminder list** - View your reminders\n**reminder add** - Add a reminder to your list\n**reminder clear** - Clear your reminders\n**reminder remove** - Remove a single reminder from your list", inline=True)
                    await channel.send(embed=embed)
                    print_timey("Reminder command list given!")

            if message.content.startswith(pre + "alarm"): #% Sets an alarm for a given amount of time with an optional message

                rest = message.content.replace(pre + "alarm ","")
                rests = rest.split(" ", 1)
                elemamt = len(rests)
                alarmtime = rests[0]
                if elemamt == 1:
                    alarmsg = "Alarm!"
                else:
                    alarmsg = rests[1]
                try:
                    if alarmtime.endswith("h") or alarmtime.endswith("m") or alarmtime.endswith("s"):
                        if alarmtime.endswith("h"):
                            time = alarmtime.replace("h","")
                            waittime = int(time) * 3600
                        elif alarmtime.endswith("m"):
                            time = alarmtime.replace("m","")
                            waittime = int(time) * 60
                        elif alarmtime.endswith("s"):
                            waittime = int(alarmtime.replace("s",""))
                        else:
                            waittime = alarmtime
                        endtime = datetime.now() + timedelta(seconds = waittime)
                        finaltime = endtime.strftime("%I:%M%p")
                        notifbed = await embuilder("I'll DM you **\"" + alarmsg + "\"** in **" + str(waittime) + " seconds**! (at " + str(finaltime) + ")", "⏰ Alarm")
                        alarmbed = await embuilder("**\"" + alarmsg + "\"**\nYour timer for **" + str(waittime) + " seconds** ends now!","⏰ Time's up!")
                        with open(txt + '/alarmbed.json', 'w') as alarmfile:
                            alarmfile.write(json.dumps(alarmbed.to_dict()))
                        await channel.send(embed=notifbed)
                        print_timey("Alarm set for {} seconds!".format(str(waittime)))
                        await asyncio.sleep(waittime)
                        await author.send(embed=alarmbed)

                except ValueError:
                    await channel.send("`" + str(alarmtime) + "` isn't an amount of time. How am I supposed to DM you in `" + str(alarmtime) + "` seconds?")
                    await asyncio.sleep(1)
                    await channel.send("`" + pre + "alarm 5s` will DM you in 5 seconds.\n`" + pre + "alarm 5m` will DM you in 5 minutes.\n`" + pre + "alarm 5h` will DM you in 5 hours.")

    # Help
            if message.content.startswith(pre + 'credits'): #% Displays credits for Centi

                embed = await embuilder(edesc="**Dominae** -- a Discord screengrab bot by Robin Universe\n**Centipeetle** -- a fork of Dominae by maddoxdragon\n\n❤️❤️❤️",ename="Credits",ethumb='https://i.imgur.com/FHrpeLd.png')
                await channel.send(embed=embed)
                print_timey("Credits displayed!")

            if message.content.startswith(pre + 'help'): #% Displays help documents for Centi

                with open(txt + "/bighelp.txt",'r') as helpfile:
                    helpdesc = helpfile.readlines()
                embed=discord.Embed(title="**Centipeetle**", url="https://github.com/madgeraccoon/Centipeetle", description="*world's cutest bot*", color=embedcolor)
                embed.set_thumbnail(url="https://i.imgur.com/GcdZl7c.png")
                embed.add_field(name="**Utility/Fun**", value=helpdesc[0].replace("^","\n"), inline=True)
                embed.add_field(name="**Chatting**", value=helpdesc[1].replace("^","\n"), inline=True)
                embed.add_field(name="**Media**", value=helpdesc[2].replace("^","\n"), inline=True)
                embed.add_field(name="**Video**", value=helpdesc[3].replace("^","\n"), inline=True)
                embed.add_field(name="**Voice Chat**", value=helpdesc[4].replace("^","\n"), inline=True)
                embed.add_field(name="**Reminders**", value=helpdesc[5].replace("^","\n"), inline=True)
                embed.add_field(name="**Help**", value=helpdesc[6].replace("^","\n"), inline=True)
                embed.add_field(name="**Host**", value=helpdesc[7].replace("^","\n"), inline=True)
                embed.add_field(name="**Admin**", value=helpdesc[8].replace("^","\n"), inline=True)
                embed.set_footer(text="this help list is currently incomplete; i promise i'll fix it later!!!")
                await channel.send(embed=embed)
                print_timey("Help disambiguation shown!")

    # Admin
            if '$$' in message.content: #% Parrots the message without the command for easy bot-talking

                if str(author.id) in permallow:
                    try:
                        getlink = search("(?P<url>https?://[^\s]+)", messageUnchanged).group("url")
                        if urltyper(getlink) == "image" or urltyper(getlink) == "audio":
                            os.system('wget -O {}/simonfile{} "{}" -q'.format(out, linkext, getlink))
                            simonfile = discord.File(out + "/simonfile{}".format(linkext))
                        else:
                            raise AttributeError
                        simonmsg = messageUnchanged.replace('$$','').replace(getlink,'')
                        await message.delete()
                        await channel.send(simonmsg, file=simonfile)
                    except AttributeError:
                        simonmsg = messageUnchanged.replace('$$','')
                        await message.delete()
                        await channel.send(simonmsg)
                    
                    print_timey("Simon said!:\n'{}'".format(simonmsg))

            if message.content.startswith(adm + 'file'): #% Grabs an image from the .centipeetle/img/ folder

                if str(author.id) in permallow:
                    rest = message.content.replace(adm + 'file ','')
                    cf = discord.File(cwd + "/" + rest, filename=rest)
                    embed = await embuilder(None,"Custom Image",'attachment://' + rest)
                    await channel.send(embed=embed, file=cf)
                    print_timey("Specified image given!")

            if message.content.startswith(adm + 'cons'): #% Runs a command through the host computer

                target = message.content.replace(adm + 'cons ','')
                if str(author.id) in permallow:
                    subprocess.check_output(target + " > ~/.centipeetle/txt/cons.txt",shell=True)
                    with open(txt + "/cons.txt",'r') as cons:
                        term = cons.read()
                    await channel.send(term)
                    print_timey("Terminal command run! ({})".format(target))

            if message.content.startswith(adm + 'exp'): #% Runs a command through Python 

                if str(author.id) in permallow:
                    if message.content.startswith(adm + 'exp+'):
                        quieres = messageUnchanged.replace(adm + 'exp+ ','')
                        maths = await eval(quieres)
                    else:
                        quieres = messageUnchanged.replace(adm + 'exp ','')
                        maths = eval(quieres)
                    await channel.send(maths)

            if message.content.startswith(adm + 'pacman'): #% Updates the host computer

                if str(author.id) in permallow:
                    await channel.send("Running sudo pacman -Syu...")
                    subprocess.check_output("sudo pacman -Syu --noconfirm",shell=True)
                    await channel.send("Pacman complete!")
                    print_timey("Sudo pacman -Syu run!")

            if message.content.startswith(adm + 'reboot'): #% Reboots the host computer

                if str(author.id) in permallow:
                    await channel.send("Rebooting...")
                    print_timey("Rebooting...")
                    subprocess.check_output("sudo reboot",shell=True)

            if message.content.startswith(adm + 'pacreb'): #% Updates and reboots the host computer

                if str(author.id) in permallow:
                    await channel.send("Running sudo pacman -Syu...")
                    subprocess.check_output("sudo pacman -Syu --noconfirm",shell=True)
                    await channel.send("Pacman complete. Rebooting...")
                    print_timey("Sudo pacman -Syu run! Rebooting now...")
                    subprocess.check_output("sudo reboot",shell=True)

        except Exception as e:
            print(traceback.format_exc())
            if hasattr(e, 'message'):
                await channel.send("```python\nError on line " + str(sys.exc_info()[-1].tb_lineno) + "\n" + str(e.message) + "```")
            else:
                await channel.send("```python\nError on line " + str(sys.exc_info()[-1].tb_lineno) + "\n" + str(e) + "```")

    @client.event
    async def on_message_edit(oldmsg, newmsg):
        if "reddit.com" in newmsg.content:
            pass
        elif newmsg.content == oldmsg.content:
            pass
        else:
            await on_message(newmsg)

client.run(token.strip())
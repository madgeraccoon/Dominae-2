# Modules
from datetime import datetime, timedelta # Screengrabbot by Ewi OwO
from discord.ext.commands import Bot ##### Centipeetle Revisions by Madison "Maddie" Adger Badger Raccoon, Gay Dragon Extraordinare
from discord.ext import commands ######### Screenplay by Ray William Johnson
from random import randint ############### Associate Producer: Dick Wolf
from pathlib import Path ################# Date of last update: 09/06/2019
import soundfile as sf
from os import path
import subprocess
import youtube_dl
import discord
import asyncio
import random
import time
import sys
import os

# File Paths
cwd = str(Path.home()) + "/.dominae" # The following are just filepath ease-of-access variables
aud = cwd + "/audio"
img = cwd + "/img"
sh = cwd + "/sh"
txt = cwd + "/txt"
out = cwd + "/out"
rems = cwd + "/rems"

# Pre-Load Bot Variables
client = commands.Bot(command_prefix='>>')
with open(txt + '/token.txt','r') as tokenfile: # Centipeetle bot token
    token = tokenfile.read()
with open(txt + '/version.txt','r') as versfile: # Centipeetle version
    centiversion = versfile.read()

embedicon = 'https://cdn.discordapp.com/attachments/437821201461805066/552014178521710612/Centepeetle_GemPNG.webp' #Replace link to change embed icon
embedcolor = 0x7900CE # Replace "0x7900CE" with "0x{HEX CODE}" to change embed color

badlist = ("owo", "uwu", "ahegao", "my back")
nicelist = ("thank you", "thanks", "love you", "good")
disabledlist = ("web", "mov", "full", "window", "fetch")

# Client Events
@client.event
async def on_ready(): # Run/Defined when Centi is loaded
    now = datetime.now()
    print ("Squaw! Centipeetle " + centiversion + " Loaded and Connected!\n(Bot Core Ready)")
    print ('Ready at {} \n'.format(now.strftime("%I:%M%p on %A, %B %d, %Y")))
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="True Kinda Love (feat Estelle & Zach Callison)"))
    
@client.event
async def on_message(message): # Run/Defined whenever a message is sent
    if message.author == client.user:
        return
    if message.guild is None and author != client.user:
        print("Direct message from " + author.name + ": " + message.content)

    await client.process_commands(message)

# Per-Message Bot Variables (Cont)
    channel = message.channel
    author  = message.author

    now = datetime.now() # Gets the current time when a command is run
    justtimey = 'at {} \n'.format(now.strftime("%I:%M%p on %A, %B %d, %Y")) # "at 06:00AM on Wednesday, January 2, 2019"
    embedtimey = '{}'.format(now.strftime("%a at %I:%M%p")) # "Wed at 06:00AM"
    timeydate = 'User: {}\nTime: {} \n'.format(author, now.strftime("%I:%M:%S%p on %A, %B %d, %Y")) # "by madgeraccoon#1983 at 06:00:00AM on Wednesday, January 2, 2019"

    with open(txt + '/toggle.txt','r') as tfile: # Reads the current toggle state
        toggle = tfile.read()
    with open(txt + '/pre.txt','r') as prefile: # Centipeetle command prefix
        pre = prefile.read().strip()
    rpre = "r" + pre
    adm = "$"

    if author.discriminator != "0000": # Checks the roles of the message author, given they're in a server and they're not a webhook
        role_names = [role.name for role in author.roles]

# Special Case Rules
    if message.content.startswith(pre + "say"): # Ignores the lowercase rule to maintain your csay capitalization
        pass
    elif message.content.startswith(pre + "addresp"): # Ignores the lowercase rule to maintain your response's capitalization
        pass
    elif message.content.startswith(pre + "reminder add"): # Ignores the lowercase rule to maintain your reminder's capitalization
        pass
    elif message.content.startswith(adm + "cons"): # Ignores the lowercase rule for case-sensitive console commands
        pass
    else: # Lowers the case of your message, for the sake of detecting uppercase messages
        message.content = message.content.lower()

# Bot Toggles
    if message.content.startswith(adm + 'off'): # Disables Centi
        with open(txt + '/toggle.txt','w') as p:
            p.write("True")

        await channel.send("Centipeetle is away.")

        await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Crying Breakfast Friends with Steven"))
        print ("Centi toggled: " + toggle + "\n" + timeydate)

    if message.content.startswith(adm + 'on'): # Re-enables Centi from an OFF state
        with open(txt + '/toggle.txt','w') as n:
            n.write("False")

        await channel.send("Centipeetle is back!")
        
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="True Kinda Love (feat Estelle & Zach Callison)"))
        print ("Centi toggled: " + toggle + "\n" + timeydate)

    if toggle == "False":

# Utility/Fun
        if message.content.startswith(pre + 'd'): # Rolls a specified die

            try:
                dicey = int(message.content.replace(pre + "d",""))
                roll = str(randint(1, int(dicey)))
                if str(dicey) == "1":
                    await channel.send("This is going to take a while...")
                    await asyncio.sleep(5)
                    await channel.send("**Almost there...**")
                    await asyncio.sleep(3)
                    await channel.send("Your number is " + roll + ". What did you hope to accomplish?")
                elif roll == str(dicey):
                    await channel.send("Rolling the **D" + str(dicey) + "**, **you rolled a natural " + str(dicey) + "!!!** Congratulations!")
                elif str(dicey) != "1" and roll == "1":
                    await channel.send("Rolling the **D" + str(dicey) + "**, you rolled a natural **one**. Congratulations, your roll sucks!")
                else:
                    await channel.send("Rolling the **D" + str(dicey) + "**, your number is **" + roll + "**!")
                print ("The Dicepeetle has been cast! Roll = " + roll + "\n" + timeydate)
            except:
                await channel.send("The Dicepeetle wasn't cast. Use natural numbers.")
                print ("The Dicepeetle wasn't cast. Use natural numbers." + "\n" + timeydate)

        if message.content.startswith(pre + 'rate'): # Gives the user their gay rating

            roll = str(randint(0, 100))
            await channel.send("You are " + roll + "% gay! :gay_pride_flag:")
            print("Gay rated! (" + roll + ")" + "\n" + timeydate)

        if message.content.startswith(pre + 'fetch'): # Grabs a screenfetch of the host computer

            subprocess.check_output(sh + "/cfetch.sh")
            with open(txt + '/screenfetch.txt', 'r') as fetchfile:
                fetch = fetchfile.read()
            embed = discord.Embed(description=fetch, color=embedcolor)
            embed.set_author(name="Screenfetch", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Screenfetch posted!" + "\n" + timeydate)

        if message.content.startswith(pre + "choose"): # Chooses from a specified set of options, separated by commas

            rest = message.content.replace(pre + "choose ","")
            opts = rest.split(", ")
            optamt = len(opts)
            newoptamt = int(optamt) - 1
            chosen = randint(0, newoptamt)
            await channel.send("I choose option `" + opts[chosen] + "`!")
            if optamt == 1:
                await asyncio.sleep(1)
                await channel.send("Tip: Use commas to separate different choice options!")
            print("Random choice! \n(" + opts[chosen] + ")\n" + timeydate)

        if message.content.startswith(pre + 'video'): # Grabs the video chat link for the user's current voice channel

            try:
                servid = str(message.guild.id)
                vcid = str(author.voice.channel.id)
                await channel.send("Here's the video chat link for your current voice chat, `" + str(author.voice.channel) + "`!\n<https://www.discordapp.com/channels/" + servid + "/" + vcid + ">")
                print ("Video chat link given!")
            except:
                await channel.send("You're not currently in a voice channel!")
                print ("Video chat link not given!")
            print (timeydate)

        if '$$' in message.content: # Parrots the message without the command for easy bot-talking

            simonmsg = message.content.replace('$$','')
            await message.delete()
            await channel.send(simonmsg)
            print ("Simon said!:\n'" + simonmsg + "'\n" + timeydate)

# Chatting
        if 'centi' in message.content and 'how' in message.content and 'day' in message.content: # Centipeetle, how was your day?

            with open(txt + "/responses.txt", 'r') as resps:
                response = resps.readlines()
                await channel.send(random.choice(response))
                print ("How was my day?")
                print (timeydate)

        if message.content.startswith(pre + 'addresp'): # Adds a response to Centi's pool of responses

            with open(txt + "/responses.txt", 'a') as resps:
                preless = message.content.replace(pre + 'addresp ','')
                resps.write(preless + "\n")
                await channel.send("Response added: `" + preless + "`")
                print ("'" + preless + "' added to the response pool!")
                print (timeydate)

        if any(x in message.content.lower() for x in badlist): # Gets angry at Alexa for saying bad things

            if str(author) == "Alexa#0369":
                await asyncio.sleep(1)
                await channel.send("Alexa.")
                print("what the hell alexa")
                print(timeydate)
            else:
                pass

        if 'wasd' in message.content: # When you are walkin'

            outcome = randint(1, 3)
            if str(outcome) == "1": # Bada bing
                await channel.send("I'm walkin\' here!")
            elif str(outcome) == "2": # Walkin' by grayfruit
                await channel.send("https://youtu.be/d_dLIy2gQGU")
            elif str(outcome) == "3": # When you are dancin'
                await channel.send(file=discord.File(img + "/h.gif"))
            print ("WASD")
            print (timeydate)

        if 'hi centi' in message.content or 'hello centi' in message.content: # Greetle the 'Peetle
            
            await channel.send("hi!!!")
            print ("hello!!!")
            print (timeydate)

        if 'chaps' in message.content or 'chips' in message.content: # Reacts to the mention of chips, specifically Chaps

            await message.add_reaction('🥔')
            await channel.send(file=discord.File(img + "/cchaps.gif"))
            print ("Squaw! (chaps detected)" + "\n" + timeydate)

        if 'steven' in message.content: # Reacts to the word 'Steven'
            
            await message.add_reaction('⭐')
            print ("Squaw! (Steven detected)")
            print (timeydate)

# Media
        if message.content.startswith(pre + 'web'): # Grabs an image from the webcam attached to the host computer

            await message.add_reaction('✋')
            try:
                subprocess.check_output(sh + "/web.sh")
                sweb = discord.File(out + "/sweb.png", filename="sweb.png")
                embed = discord.Embed(color=embedcolor)
                embed.set_author(name="Trashbox Cam", icon_url=embedicon)
                embed.set_image(url="attachment://sweb.png")
                embed.set_footer(text=embedtimey)
                await channel.send(embed=embed, file=sweb)
                print ("Webcam image (sweb) uploaded!")
            except subprocess.CalledProcessError as e:
                await channel.send("`" + pre + "web` has failed! (Perhaps the camera is in use or disconnected?)")
                print ("Webcam image (sweb) failed! (in use?)")
            await message.remove_reaction('✋',client.user)
            print (timeydate)

        if message.content.startswith(pre + 'full'): # Grabs an image of the host computer's screen

            subprocess.check_output(sh + "/full.sh")
            await channel.send(file=discord.File(out + "/sfull.png"))
            print ("Screenshot (sfull) uploaded! ")
            print (timeydate)

        if message.content.startswith(pre + 'window'): # Grabs an image of the host computer's currently focused window

            subprocess.check_output(sh + "/window.sh")
            await channel.send(file=discord.File(out + "/swindow.png"))
            print ("Screenshot (swindow) uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'say'): # Creates an image with the message's text 

            target = message.content.replace(pre + 'say','')
            subprocess.check_output(sh + "/ssay.sh " + "\"" + target + "\"", shell=True)
            await channel.send(file=discord.File(out + '/ssay.png'))
            print ("Phrase (ssay) uploaded!")
            print ("'" + message.content.replace(pre + "say ","") + "'")
            print (timeydate)

        if message.content.startswith(pre + 'mov'): # Grabs a video from the webcam attached to the host computer

            await channel.send("Recording...Please wait forever. (it takes a while.)")
            subprocess.check_output(sh + "/smov.sh")
            await channel.send(file=discord.File(out + "/smov.webm"))
            print ("Webcam (smov) somehow uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'give'): # Grabs an image from a specified repository (or a folder, in the case of cursedcat)

            givetype = message.content.replace(pre + 'give ', '')
            if givetype == pre + "give":
                subprocess.check_output(sh + "/give.sh")
            elif givetype == "cat":
                subprocess.check_output(sh + "/cat.sh")
            elif givetype == "dog":
                subprocess.check_output(sh + "/dog.sh")
            elif givetype == "cursedcat":
                catnumber = str(randint(1, 11))
                subprocess.check_output(sh + "/cursedcat.sh " + catnumber, shell=True)
            else:
                subprocess.check_output(sh + "/give.sh " + givetype, shell=True)
            with open(txt + "/give.txt", 'r') as givefile:
                giveurl = givefile.read()
            await channel.send("Here's your image result for `" + givetype + "`!:\n" + giveurl)
            print("Image given! (cgive)" + "\n" + timeydate)

        if "centi" in message.content and any(x in message.content.lower() for x in nicelist): # Centipeetle love response
        
            squawchance = randint(1, 200)
            if str(squawchance) == "69":
                await channel.send("Squaw! (this message is extremely rare)")
            if "dummy" in message.content:
                await channel.send(file=discord.File(img + '/angry.gif'))
            else:
                await channel.send(file=discord.File(img + '/lovepeetle.gif'))
                print ("Love given!")
                print (timeydate)

        if message.content.startswith(pre + 'file'): # Grabs an image from the .dominae/img/ folder

            rest = message.content.replace(pre + 'file ','')
            try:
                cf = discord.File(img + "/" + rest, filename=rest)
                embed = discord.Embed(color=embedcolor)
                embed.set_author(name="Custom Image", icon_url=embedicon)
                embed.set_image(url='attachment://' + rest)
                embed.set_footer(text=embedtimey)
                await channel.send(embed=embed, file=cf)
                print ("Specified image given!" + "\n" + timeydate)
            except:
                await channel.send("`" + rest + "` is an invalid file, or isn't in the .dominae/img/ folder!")
                print("Specified image not found!\n" + timeydate)

        if 'cute connie bot' in message.content:
            await channel.send(file=discord.File(img + '/howareyou.png'))
            print ("CUTE CONNIE BOT\n" + timeydate)

# YouTube Commands
        if message.content.startswith(pre + "yt"): # YouTube-related commands

            if message.content.startswith(pre + "ytdl"): # Finds and downloads a YouTube video
                preq = message.content.replace(pre + "ytdl ","")
                target = preq.replace(preq, "'" + preq + "'")
                subprocess.call(sh + '/cdlyt.sh ' + target, shell=True)
                with open (txt + '/ytitle.txt', 'r') as titlefile:
                    title = titlefile.read()
                await channel.send("Your download for `" + preq + "` is below! (Title: `" + title.replace("\n","") + "`) (unless the file's too big...)")
                await channel.send(file=discord.File(out + '/ytgrab.ogg'))
                print ("YouTube mp3 posted!")

            elif message.content.startswith(pre + "ytplay"): # Finds and downloads a YouTube video, then plays it in the user's current voice chat 
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
                    print ("Played YouTube audio in voice chat!")

            else: # Finds a YouTube video matching the given search term
                preq = message.content.replace(pre + "yt ","")
                formo = preq.replace(" ","+")
                target = formo.replace(preq, "\"" + preq + "\"")
                print(target)
                subprocess.call(sh + '/cyt.sh ' + target, shell=True)
                with open (txt + '/ytout.txt', 'r') as ytfile:
                    ytout = ytfile.readlines()
                await channel.send("Your URL for `" + preq + "` is here! (Title: `" + ytout[1].strip("\n") + "`): https://youtu.be/" + ytout[0])
                print ("YouTube URL posted!" + "\n" + timeydate)

# Voice Chat Audio Commands
        async def playvoice(audiofile = aud + "/sound/gnome.mp3", length = 1): # Function for easy voice chat file playing, given a filepath and a length
            if author.voice is not None:
                vcid = author.voice.channel
                voice = await vcid.connect()
                player = voice.play(discord.FFmpegPCMAudio(audiofile))
                await asyncio.sleep(float(length))
                await voice.disconnect()

        if message.content.startswith(pre + 'play'): # Plays a specified sound from the sound folder, or gnomes voice participants
            rest = message.content.replace(pre + 'play','')
            if 'bonk' in rest:
                await playvoice(aud + '/sound/bonk.mp3', 1.1)
            elif 'mmm' in rest:
                await playvoice(aud + '/sound/mmm.mp3', 1.7)
            elif 'sans' in rest:
                await playvoice(aud + '/sound/sans.mp3', 0.17)
            elif 'gnome' in rest:
                await playvoice()
            else:
                await playvoice()
            print("Audio played!: `" + rest + "`" + "\n" + timeydate)

        if message.content.startswith(pre + 'hellgnome'): # Gnomes voice participants as many times as one specifies
            gnomeamt = message.content.replace(pre + 'hellgnome ','')
            if author.voice is not None:
                vcid = author.voice.channel
                voice = await vcid.connect()
                for i in range(int(gnomeamt)):
                    player = voice.play(discord.FFmpegPCMAudio(aud + "/sound/gnome.mp3"))
                    await asyncio.sleep(1)
                await voice.disconnect()

        if message.content.startswith(pre + 'noise'): # Plays a Centipeetle-Brand:tm: Sound Effect
            noiseno = str(randint(1, 16))
            noisefile = noiseno + ".wav"
            centisounds = aud + "/centisounds/"
            cenfile = sf.SoundFile(centisounds + noisefile)
            cenlength = '{}'.format(len(cenfile) / cenfile.samplerate)
            await playvoice(centisounds + noisefile, float(cenlength))
            print("Centipeetle noise given!" + "\n" + timeydate)

        if message.content.startswith(pre + 'query'): # Okay Google, 
            noiseno = str(randint(1, 7))
            noisefile = noiseno + ".wav"
            queries = aud + "/queries/"
            queryfile = sf.SoundFile(queries + noisefile)
            querylength = '{}'.format(len(queryfile) / queryfile.samplerate)
            await playvoice(queries + noisefile, float(querylength))
            print("Okay Google!" + "\n" + timeydate)

# File Audio Commands
        if message.content.startswith(pre + 'vox'): # Generates a WillFromAfar announcement from the author's message, corresponding to a list of available keywords

            if message.content.startswith(pre + 'voxplay'):
                voxs = message.content.replace(pre + "voxplay ","")

            else:
                voxs = message.content.replace(pre + "vox ","")
            voxfn = voxs.replace(" ",".wav \n") + ".wav"
            voxfn += " svox.wav\n"
            voxfn = voxfn.lower()
            with open(aud + '/VOX/voxfn.txt','w') as f:
                f.write(voxfn)
            subprocess.check_output(aud + "/VOX/svox.sh")
            if message.content.startswith(pre + 'voxplay'):
                voxfile = sf.SoundFile(aud + "/VOX/svox.wav")
                voxlength = '{}'.format(len(voxfile) / voxfile.samplerate)
                await playvoice(aud + "/VOX/svox.wav", float(voxlength))
                print ("VOX Phrase (svox) played!")
            else:
                await channel.send(file=discord.File(aud + '/VOX/svox.wav'))
                print ("VOX Phrase (svox) uploaded!")
            print ("Message: ""'" + message.content.replace(pre + "vox ","") + "'")
            print (timeydate)

        if message.content.startswith(pre + 'animal'): # This command is broken, but it was supposed to generate an Animalese voice clip from text
            voxs = message.content.replace(pre + "animal ","")
            voxfn = [os.path.splitext(x)[0] for x in voxs]
            voxlist = list(voxfn)
            with open(aud + '/animalese/voxfn.txt','w') as f:
                for item in voxlist:
                    if item == " ":
                        voxword = "space"
                    else:
                        voxword = item.lower()
                    voxfile = voxword + ".wav"
                    print(voxfile)
                    f.write("{0} ".format(voxfile))
                f.close()
            subprocess.check_output(aud + "/animalese/canimal.sh")
            await channel.send("`" + pre + "animal` is currently broken, so pay no mind to this file!", file=discord.File(aud + '/animalese/canimal.wav'))
            print ("Animalese (canimal) uploaded!")
            print ("Message: `" + voxs + "`")
            print (timeydate)
 
# Reminders
        if message.content.startswith(pre + 'reminder'): # creminder

            remfile = rems + "/" + str(author.id) + ".txt"
            if message.content.startswith(pre + 'reminder add'): # Adds a reminder to a user's list

                with open(remfile, 'a+') as reminds:
                    reminds.write("**" + embedtimey + "**" + " - " + message.content.replace(pre + 'reminder add ','') + "\n")
                await channel.send("Reminder added: `" + message.content.replace(pre + 'reminder add ','') + "`")
                print ("Reminder added!")

            elif message.content.startswith(pre + 'reminder clear'): # Clears a user's list of reminders

                try:
                    usrid = str(author.id)
                    os.remove(remfile)
                    await channel.send("Reminders cleared for user `" + author.name + "` (ID: `" + usrid + "`)!")
                    print ("Reminders cleared for user `" + author.name + "` (ID: `" + usrid + "`)!")
                except FileNotFoundError:
                    await channel.send("You have no reminders to clear! (File for user `" + author.name + "` does not exist)")
                    print ("Reminder file for user `" + author.name + "` does not exist!")

            elif message.content.startswith(pre + 'reminder remove'): # Removes a specific reminder from a user's list

                rest = message.content.replace(pre + "reminder remove ","")
                subprocess.check_output("sed -i -e \"" + rest + "d\" " + remfile,shell=True)
                await channel.send("Reminder " + rest + " removed.")
                print("Reminder removed!")

            elif message.content.startswith(pre + 'reminder list'): # Lists user's reminders

                if 'plaintext' in message.content:
                    with open(remfile, 'r') as reminds:
                        remlist = reminds.read()
                    await channel.send("Reminders:\n" + remlist)
                    print ("Plaintext reminders listed!")
                else:
                    with open(remfile, 'r') as reminds:
                        remlist = reminds.read()
                    embed = discord.Embed(description=remlist, color=embedcolor)
                    embed.set_author(name="Reminders", icon_url=embedicon)
                    embed.set_footer(text=embedtimey)
                    await channel.send(embed=embed)
                    print ("Reminders listed!")

            else:

                embed=discord.Embed(color=embedcolor)
                embed.set_author(name="Reminder Commands", icon_url=embedicon)
                embed.add_field(name="All commands are prefixed with `" + pre + "`", value="**reminder list** - View your reminders\n**reminder add** - Add a reminder to your list\n**reminder clear** - Clear your reminders\n**reminder remove** - Remove a single reminder from your list", inline=True)
                embed.set_footer(text=embedtimey)
                await channel.send(embed=embed)
                print ("Reminder command list given!")
            print (timeydate)

# Alarms
        if message.content.startswith(pre + "alarm"): # Sets an alarm for a given amount of time with an optional message

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
                    alarmbed = discord.Embed(description="**\"" + alarmsg + "\"**\nYour timer for **" + str(waittime) + " seconds** ends now!", color=embedcolor)
                    alarmbed.set_author(name="⏰ Time's up!")
                    alarmbed.set_footer(text=embedtimey)
                    notifbed = discord.Embed(description="I'll DM you **\"" + alarmsg + "\"** in **" + str(waittime) + " seconds**! (at " + str(finaltime) + ")", color=embedcolor)
                    notifbed.set_author(name="⏰ Alarm")
                    notifbed.set_footer(text=embedtimey)
                    await channel.send(embed=notifbed)
                    print ("Alarm set for " + str(waittime) + " seconds!\n" + timeydate)
                    await asyncio.sleep(waittime)
                    await author.send(embed=alarmbed)
                    print ("Alarm complete for past alarm!\n" + timeydate)

            except ValueError:
                await channel.send("`" + str(alarmtime) + "` isn't an amount of time. How am I supposed to DM you in `" + str(alarmtime) + "` seconds?")
                await asyncio.sleep(1)
                await channel.send("`" + pre + "alarm 5s` will DM you in 5 seconds.\n`" + pre + "alarm 5m` will DM you in 5 minutes.\n`" + pre + "alarm 5h` will DM you in 5 hours.")

        if message.content.startswith(pre + "dinner"): # Alarm with a built-in preheating period

            timeamt = message.content.replace(pre + "dinner ","")
            oventemp, oventime = timeamt.split(' ', 1)
            waittime = int(oventime) * 60
            ovenbedpre = discord.Embed(color=embedcolor)
            ovenbedpre.set_author(name="⏰ preheating oven to `" + oventemp + "` degrees!")
            ovenbedpost = discord.Embed(description="put your food in the oven!", color=embedcolor)
            ovenbedpost.set_author(name="⏰ oven preheated to `" + oventemp + "` degrees!")
            inoven = discord.Embed(description="check the oven in " + oventime + " minutes!", color=embedcolor)
            inoven.set_author(name="⏰ your dinner is cooking")
            outoven = discord.Embed(description="check the oven", color=embedcolor)
            outoven.set_author(name="⏰ your dinner is ready!")
            await channel.send(embed=ovenbedpre)
            print ("Oven is preheating!\n" + timeydate)
            await asyncio.sleep(600)
            await author.send(embed=ovenbedpost)
            print ("Oven is ready for past alarm!\n" + timeydate)
            await asyncio.sleep(60)
            await author.send(embed=inoven)
            print ("Food is now cooking for past alarm!\n" + timeydate)
            await asyncio.sleep(waittime)
            await author.send(embed=outoven)
            print ("Food has been cooked for past alarm!\n" + timeydate)

# Help Commands
        if message.content.startswith(pre + 'credits'): # Displays credits for Centi

            embed = discord.Embed(description="**Dominae** -- a Discord screengrab bot by Elisha Shaddock\n**Centipeetle** -- a fork of Dominae by madgeraccoon\n\n**Less than Three**", color=embedcolor)
            embed.set_author(name="Credits", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Credits displayed!\n" + timeydate)

        if message.content.startswith(pre + 'help'): # Displays help documents for Centi

            if message.content.startswith(pre + 'help ' + pre + 'vox'):
                await channel.send("Here are the current VOX keywords.")
                await channel.send(file=discord.File(img + "/svox.png"))
                print ("Black Mesa Tech Support notified! (help svox)")
                
            elif message.content.startswith(pre + 'help domi'):
                with open(txt + '/domhelp.txt', 'r') as domhelp:
                    help = domhelp.read().replace("PREFIX",pre)
                embed = discord.Embed(description=help, color=embedcolor)
                embed.set_author(name="Dominae Help", icon_url=embedicon)
                embed.set_footer(text=embedtimey)
                await channel.send(embed=embed)
                print ("Dominae Help Shown")

            elif message.content.startswith(pre + 'help centi'):
                with open(txt + '/centihelp.txt', 'r') as centihelp:
                    help = centihelp.read().replace("PREFIX",pre)
                embed2 = discord.Embed(description=help, color=embedcolor)
                embed2.set_author(name="Centi Help", icon_url=embedicon)
                embed2.set_footer(text=embedtimey)
                await channel.send(embed=embed2)
                print ("Centipeetle Help Shown")

            else:
                helpbed = discord.Embed(description="**For Centipeetle commands** — `" + pre + "help centi`\n**For Dominae commands** — `" + pre + "help domi`", color=embedcolor)
                helpbed.set_author(name="Help Disambiguation", icon_url=embedicon)
                helpbed.set_footer(text=embedtimey)
                await channel.send(embed=helpbed)
                print ("Help disambiguation shown!")
            print (timeydate)

# Computer-Related Admin Commands
        if message.content.startswith(adm + 'cons'): # Runs a command through the host computer

            target = message.content.replace(adm + 'cons ','')
            if 'centipeetle wrangler' in role_names:
                subprocess.check_output(target + " > ~/.dominae/txt/cons.txt",shell=True)
                with open(txt + "/cons.txt",'r') as cons:
                    term = cons.read()
                await channel.send(term)
                print("Terminal command run! (" + target + ")" + "\n" + timeydate)

        if message.content.startswith(adm + 'pacman'): # Updates the host computer

            if 'centipeetle wrangler' in role_names:
                await channel.send("Running sudo pacman -Syu...")
                subprocess.check_output("sudo pacman -Syu --noconfirm",shell=True)
                await channel.send("Pacman complete!")
                print ("Sudo pacman -Syu run!" + "\n" + timeydate)

        if message.content.startswith(adm + 'reboot'): # Reboots the host computer

            if 'centipeetle wrangler' in role_names:
                await channel.send("Rebooting...")
                print ("Rebooting..." + "\n" + timeydate)
                subprocess.check_output("sudo reboot",shell=True)

        if message.content.startswith(adm + 'pacreb'): # Updates and reboots the host computer

            if 'centipeetle wrangler' in role_names:   
                await channel.send("Running sudo pacman -Syu...")
                subprocess.check_output("sudo pacman -Syu --noconfirm",shell=True)
                await channel.send("Pacman complete. Rebooting...")
                print ("Sudo pacman -Syu run! Rebooting now..." + "\n" + timeydate)
                subprocess.check_output("sudo reboot",shell=True)

# Bot-Related Admin Commands
        if message.content.startswith(adm + 'restart'): # Restarts Centi

            if 'centipeetle wrangler' in role_names:
                await channel.send("Restarting Centi...")
                print("Restarting..." + "\n" + timeydate)
                os.execl(sys.executable, sys.executable, *sys.argv)

        if message.content.startswith(adm + 'prefix'): # Changes the prefix Centi responds to
            
            if 'centipeetle wrangler' in role_names:
                rest = message.content.replace(adm + "prefix ","")
                with open(txt + '/pre.txt','w') as f:
                    with open(txt + '/pre.txt','r') as myfile:
                        pre = myfile.read()
                    f.write(rest)
                await channel.send("Prefix has been changed to `" + rest + "`!")
                print ("Prefix Changed to: " + rest + "\n" + timeydate)

        if message.content.startswith(adm + 'setvers'): # Changes the current Centipeetle version number (Current format: X.X.X)

            if 'centipeetle wrangler' in role_names:
                rest = message.content.replace(adm + 'setvers ','')
                with open(txt + '/version.txt','w') as versfile: # Centipeetle version
                    versfile.write(rest)
                await channel.send("Centipeetle is now version `" + rest + "`.")
                print ("Centipeetle version updated to " + rest + "!\n" + timeydate)

client.run(token.strip())
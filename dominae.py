#Screengrabbot by Ewi OwO
# code revisions by Maddie oo-woo

### Prerequisites and Setup

from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime
from random import randint
from pathlib import Path
from os import path
import subprocess
import discord
import asyncio
import random
import time
import os

client = commands.Bot(command_prefix='>')

cwd = str(Path.home()) + "/.dominae"
img = cwd + "/img"
sh = cwd + "/sh"
txt = cwd + "/txt"
out = cwd + "/out"
rems = cwd + "/rems"

tokenfile = open(txt + '/token.txt','r')
token = tokenfile.read()
tokenfile.close()

embedicon = 'https://cdn.discordapp.com/attachments/437821201461805066/552014178521710612/Centepeetle_GemPNG.webp' #Replace link to change embed icon
embedcolor = 0x7900CE # Replace "0x7900CE" with "0x{HEX CODE}" to change embed color

@client.event
async def on_ready():
    now = datetime.now()
    print ("Squaw! (Bot Core Ready)")
    print ('at {} \n'.format(now.strftime("%I:%M%p on %A, %B %d, %Y")))
    activity = discord.Game(name="with Steven")
    await client.change_presence(status=discord.Status.online, activity=activity)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

    channel = message.channel
    author  = message.author

# Date and Time Variables

    now = datetime.now() # Get time of command
    justtimey = 'at {} \n'.format(now.strftime("%I:%M%p on %A, %B %d, %Y")) # "at 06:00AM on Tuesday, January 1, 2019"
    embedtimey = '{}'.format(now.strftime("%a at %I:%M%p")) # "Tue at 06:00AM"
    timeydate = 'by {} at {} \n'.format(author, now.strftime("%I:%M:%S%p on %A, %B %d, %Y")) # "by madgeraccoon#1983 at 06:00:00AM on Tuesday, January 1, 2019"

    prefile = open(txt + '/pre.txt','r') 
    pre = prefile.read().strip()
    rpre = "r" + pre

    tfile = open(txt + '/toggle.txt','r') 
    toggle = tfile.read()

# Special Case and Space Rules

    if message.content.startswith(pre + "say"):
        pass
    elif message.content.startswith(pre + "addresp"):
        pass
    elif message.content.startswith(pre + "reaminder"):
        pass
    else:
        message.content = message.content.lower()

# Bot Toggles
    
    if message.content.startswith('$off'): # Off
        p = open(txt + '/toggle.txt','w')
        p.write("True")
        p.close

        await channel.send("Centipeetle is now poofed.\n(Dominae is now OFF.)")
        await channel.send(file=discord.File(img + "/off.gif"))

        activity = discord.Game(name="in a bubble")
        await client.change_presence(status=discord.Status.idle, activity=activity)
        print ("Centi enabled: " + toggle)
        print (timeydate)

    if message.content.startswith('$on'): # On
        n = open(txt + '/toggle.txt','w')
        n.write("False")
        n.close

        await channel.send("You've unbubbled Centipeetle.\n(Dominae is now ON.)")
        await channel.send(file=discord.File(img + "/on.gif"))
        
        activity = discord.Game(name="with Steven")
        await client.change_presence(status=discord.Status.online, activity=activity)
        print ("Centi enabled: " + toggle)
        print (timeydate)

    if toggle == "False":

### Centipeetle Commands

        if message.content.startswith(pre + 'fetch'): # cfetch

            subprocess.check_output(sh + "/cfetch.sh")
            with open(txt + '/screenfetch.txt', 'r') as fetchfile:
                fetch = fetchfile.read()
            embed = discord.Embed(description=fetch, color=embedcolor)
            embed.set_author(name="Screenfetch", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Screenfetch posted! \n{}".format(timeydate))

        if message.content.startswith(pre + "yt"): # cyt
            
            preq = message.content.replace(pre + "yt ","")
            target = preq.replace(preq, "'" + preq + "'")
            subprocess.call(sh + '/cytsearch.sh ' + target, shell=True)
            with open (txt + '/ytout.txt', 'r') as ytfile:
                ytout = ytfile.read()
            await channel.send("Your URL for `" + preq + "` is here!: https://youtu.be/" + ytout.replace("\n",""))
            print ("Youtube URL posted!")
            print (timeydate)

        if message.content.startswith(pre + "dlyt"): # cdlyt
            
            preq = message.content.replace(pre + "dlyt ","")
            target = preq.replace(preq, "'" + preq + "'")
            subprocess.call(sh + '/cdlyt.sh ' + target, shell=True)
            await channel.send("Your download for `" + preq + "` is below! (unless the file's too big...)")
            await channel.send(file=discord.File(out + '/ytgrab.mp3'))
            print ("Youtube mp3 posted!")
            print (timeydate)

        if message.content.startswith(pre + 'pacreb'): # cpacreb

            role_names = [role.name for role in author.roles]
            if "centipeetle wrangler" in role_names:   
                await channel.send("Running sudo pacman -Syu...")
                subprocess.check_output(sh + "/pac.sh")
                await channel.send("Pacman complete. Rebooting...")
                print ("Sudo pacman -Syu run! Rebooting now...")
                print (timeydate)
                
                subprocess.check_output(sh + "/reb.sh")

        if message.content.startswith(pre + 'pacman'): # cpacman

            role_names = [role.name for role in author.roles]
            if "centipeetle wrangler" in role_names:
                await channel.send("Running sudo pacman -Syu...")
                subprocess.check_output(sh + "/pac.sh")
                await channel.send("Pacman complete!")
                print ("Sudo pacman -Syu run!")
                print (timeydate)
            else:
                print ("Sudo pacman -Syu attempted???")
                print (timeydate)

        if message.content.startswith(pre + 'reboot'): # creboot

            role_names = [role.name for role in author.roles]
            if "centipeetle wrangler" in role_names:
                await channel.send("Rebooting...")
                print ("Rebooting...")
                print (timeydate)
                
                subprocess.check_output(sh + "/reb.sh")
            else:
                print ("Reboot attempted???")
                print (timeydate)

        if message.content.startswith(pre + 'cbook'): # ccbook

            await channel.send(file=discord.File(img + "/cbook.png"))
            print ("Special image uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'd'): # cd (Dice)

            try:
                dicey = int(message.content.replace(pre + "d",""))
                await channel.send("Rolling the **D" + str(dicey) + "**, your number is **" + str(randint(1, int(dicey))) + "**!")
                print ("The Dicepeetle has been cast!")
                print (timeydate)
            except:
                await channel.send("The Dicepeetle wasn't cast. Use natural numbers.")
                print ("The Dicepeetle wasn't cast. Use natural numbers.")
                print (timeydate)

        if 'chaps' in message.content: # Chaps

            await channel.send(file=discord.File(img + "/cchaps.gif"))
            print ("Squaw! (chaps detected)")
            print (timeydate)

        if 'hungry bandit' and "your food's ours now" and "your food's" in message.content:
            
            await channel.send(file=discord.File(img + '/angry.gif'))
            print ("Hungry bandit.")
            print (timeydate)

        if 'csimon' in message.content: # csimon

            sez = message.content.replace("csimon","")
            await channel.send(sez)
            print ("Simon said!")
            print (timeydate)

        if 'i love you centi' in message.content: # Give Love

            if "dummy" in message.content:
                await channel.send(file=discord.File(img + '/angry.gif'))
            else:
                await channel.send(file=discord.File(img + '/lovepeetle.gif'))
                print ("Love given!")
                print (timeydate)
 
# Responses

        if 'centi' in message.content and 'how' in message.content and 'day' in message.content: # Centipeetle, how was your day?

            with open(txt + "/responses.txt", 'r') as resps:
                response = resps.readlines()
                await channel.send(random.choice(response))
                print ("How was my day?")
                print (timeydate)

        if message.content.startswith(pre + 'addresp'): # caddresp

            with open(txt + "/responses.txt", 'a') as resps:
                preless = message.content.replace(pre + 'addresp ','')
                resps.write(preless + "\n")
                await channel.send("Response added: `" + preless + "`")
                print ("'" + preless + "' added to the response pool!")
                print (timeydate)

# Reminders

        if message.content.startswith(pre + 'reaminder'): # creaminder
        
            with open(rems + "/" + str(message.author.id) + ".txt", 'a+') as reminds:
                reminds.write("**" + embedtimey + "**" + " - " + message.content.replace(pre + 'reaminder ','') + "\n")
            await channel.send("Reminder added: `" + message.content.replace(pre + 'reaminder ','') + "`")
            print ("Reminder added!")
            print (timeydate)

        if 'centi' in message.content and 'reminders' in message.content: # centi reminders

            if 'plaintext' in message.content:
                with open(rems + "/" + str(message.author.id) + ".txt", 'r') as reminds:
                    remlist = reminds.read()
                await channel.send("Reminders:\n" + remlist)
                print ("Plaintext reminders listed!")
                print (timeydate)
            else:
                with open(rems + "/" + str(message.author.id) + ".txt", 'r') as reminds:
                    remlist = reminds.read()
                embed = discord.Embed(description=remlist, color=embedcolor)
                embed.set_author(name="Reminders", icon_url=embedicon)
                embed.set_footer(text=embedtimey)
                await channel.send(embed=embed)
                print ("Reminders listed!")
                print (timeydate)

        if message.content.startswith('cleareminder'): # clear reminders

            try:
                usrid = str(message.author.id)
                os.remove(rems + "/" + str(message.author.id) + ".txt")
                await channel.send("Reminders cleared for user `" + message.author.name + "` (ID: `" + usrid + "`)!")
                print ("Reminders cleared for user `" + message.author.name + "` (ID: `" + usrid + "`)!")
                print (timeydate)
            except FileNotFoundError:
                await channel.send("You have no reminders to clear! (File for user `" + message.author.name + "` does not exist)")
                print ("Reminders NOT cleared for user `" + message.author.name + "`! (File for user `" + message.author.name + "` does not exist)")
                print (timeydate)

# Remote Commands

        if message.content.startswith(rpre + "web"): # rcweb

            subprocess.check_output(sh + "/cremweb.sh")
            await channel.send(file=discord.File(out + "/cremweb.png"))
            print("Remote image (rcweb) uploaded!")
            print(timeydate)

        if message.content.startswith(rpre + "mov"): # rcmov (WIP or discontinued)

            await channel.send("This will take forever.")
            time.sleep(10)
            await channel.send("Mainly because " + pre + "remov is disabled. Sorry!")
            #subprocess.check_output(sh + "/cremov.sh")
            #await channel.send(file=discord.File(out + "/cremov.webm"))
            print("Remote video (rcmov) attempted, but is disabled.")
            print(timeydate)

        if message.content.startswith(rpre + 'full'): # rcfull

            subprocess.check_output(sh + "/cremfull.sh")
            await channel.send(file=discord.File(out + "/cremfull.png"))
            print ("Remote desktop screenshot (rcfull) uploaded!")
            print (timeydate)

        if message.content.startswith(rpre + 'window'): # rcwindow

            subprocess.check_output(sh + "/cremwindow.sh")
            await channel.send(file=discord.File(out + "/cremwindow.png"))
            print ("Remote window screenshot (rcwindow) uploaded!")
            print (timeydate)

        if message.content.startswith(rpre + 'fetch'): # rcfetch

            subprocess.check_output(sh + "/crem.sh")
            with open(txt + '/cremfetch.txt', 'r') as fetchfile:
                fetch = fetchfile.read()
            embed = discord.Embed(description=fetch, color=embedcolor)
            embed.set_author(name="Remote (Hellbox) Screenfetch", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Remote Screenfetch (rcfetch) posted!")
            print (timeydate)

# Disabled Command List and Help Commands

        if any([keyword in message.content for keyword in (pre + 'pi', pre + 'server', pre + 'servecam', pre + 'pibm', pre + 'remote', pre + 'remotecam', pre + 'combo', pre + 'select')]):

            await channel.send("Squaw! (This command is disabled!)") #Disabled command list ^
            print ("Disabled command attempted!")
            print (timeydate)
            
        if message.content.startswith(pre + 'credits'): # ccredits

            embed = discord.Embed(description="**Dominae** -- a Discord screengrab bot by Elisha Shaddock\n**Centipeetle** -- a fork of Dominae by madgeraccoon\n\n**Less than Three**", color=embedcolor)
            embed.set_author(name="Credits", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Credits displayed!")
            print (timeydate)

        if message.content.startswith(pre + 'help'): # chelp

            if message.content.startswith(pre + 'help ' + pre + 'vox'):
                await channel.send("Here are the current VOX keywords.")
                await channel.send(file=discord.File(img + "/svox.png"))
                print ("Black Mesa Tech Support notified! (help svox)")
                print (timeydate)
            else:
                helpbed = discord.Embed(description="**Dominae Commands** — `" + pre + "domhelp`\n\n**Centipeetle Commands** — `" + "centihelp`")
                helpbed.set_author(name="Help Disambiguation", icon_url=embedicon)
                helpbed.set_footer(text=embedtimey)
                await channel.send(embed=helpbed)
                print ("Help disambiguation shown!")
                print (timeydate)

        if message.content.startswith(pre + 'domhelp'): # cdomhelp

            with open(txt + '/domhelp.txt', 'r') as domhelp:
                help = domhelp.read().replace("PREFIX",pre)
            embed = discord.Embed(description=help, color=embedcolor)
            embed.set_author(name="Dominae Help", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Dominae Help Shown")
            print (timeydate)

        if message.content.startswith('centihelp'): # centihelp

            with open(txt + '/centihelp.txt', 'r') as centihelp:
                help = centihelp.read().replace("PREFIX",pre)
            embed2 = discord.Embed(description=help, color=embedcolor)
            embed2.set_author(name="Centi Help", icon_url=embedicon)
            embed2.set_footer(text=embedtimey)
            await channel.send(embed=embed2)
            print ("Dominae Help Shown")
            print (timeydate)

### Dominae Commands

        if message.content.startswith(pre + 'full'): # cfull

            subprocess.check_output(sh + "/sfull.sh")
            await channel.send(file=discord.File(out + "/sfull.png"))
            print ("Screenshot (sfull) uploaded! ")
            print (timeydate)

        if message.content.startswith(pre + 'window'): # cwindow

            subprocess.check_output(sh + "/swindow.sh")
            await channel.send(file=discord.File(out + "/swindow.png"))
            print ("Screenshot (swindow) uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'web'): # cweb

            subprocess.check_output(sh + "/sweb.sh")
            sweb = discord.File(out + "/sweb.png", filename="sweb.png")
            embed = discord.Embed(color=embedcolor)
            embed.set_author(name="Trashbox Cam", icon_url=embedicon)
            embed.set_image(url="attachment://sweb.png")
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed, file=sweb)
            print ("Webcam (sweb) uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'mov'): # cmov

            await channel.send("Recording...Please wait forever. (it takes a while.)")
            subprocess.check_output(sh + "/smov.sh")
            await channel.send(file=discord.File(out + "/smov.webm"))
            print ("Webcam (smov) somehow uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'say'): # csay

            with open(txt + '/ssay.txt','w') as f:
                f.write(message.content.replace(pre + "say ",""))
            subprocess.check_output(sh + "/ssay.sh")
            await channel.send(file=discord.File(out + '/ssay.png'))
            print ("Phrase (ssay) uploaded!")
            print ("'" + message.content.replace(pre + "say ","") + "'")
            print (timeydate)

        if message.content.startswith(pre + 'vox'): # cvox

            voxs = message.content.replace(pre + "vox ","")
            voxfn = voxs.replace(" ",".wav \n") + ".wav"
            voxfn += " svox.wav\n"
            voxfn = voxfn.lower()
            with open(cwd + '/VOX/voxfn.txt','w') as f:
                f.write(voxfn)
                f.close()
            subprocess.check_output(cwd + "/VOX/svox.sh")
            await channel.send(file=discord.File(cwd + '/VOX/svox.wav'))
            print ("VOX Phrase (svox) uploaded!")
            print ("Message: ""'" + message.content.replace(pre + "vox ","") + "'")
            print (timeydate)

        if message.content.startswith('$prefix'): # change bot prefix

            with open(txt + '/pre.txt','w') as f:
                with open(txt + '/pre.txt','r') as myfile:
                    pre = myfile.read()
                f.write(message.content.replace("$prefix ",""))
            await channel.send("Prefix has been changed to " + "`" + message.content.replace("$prefix ","") + "`.")
            print ("Prefix Changed to: " + "'" + message.content.replace("$prefix ","") + "'")
            print (timeydate)

 # Disabled Commands

        '''
        if message.content.startswith(pre + 'remote'): # cremote

            subprocess.check_output(sh + "/sremote.sh")
            await channel.send(file=discord.File(out + '/serversync.png'))
            print ("Server Scrot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'select'): # cselect

            subprocess.check_output(sh + "/sselect.sh")
            await channel.send(file=discord.File(out + "/sselect.png"))
            print ("Screenshot (sselect) uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'servecam'): # cservecam

            subprocess.check_output(sh + "/sremotecam.sh")
            await channel.send(file=discord.File(out + '/camsync.png'))
            print ("Server Webshot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'ping'): # cping

            subprocess.check_output(sh + "/sping.sh")
            print ("Pi Shot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'ibm'): # cibm

            subprocess.check_output(sh + "/spibm.sh")
            await channel.send(file=discord.File(out + '/ibmsync.png'))
            print ("IBM Shot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'combo'): # ccombo

            await channel.send("This will take a while...")
            subprocess.check_output(sh + "/scombo.sh")
            await channel.send(file=discord.File(out + '/result.png'))
            print ("Combo Shot Uploaded")
            print (timeydate)

        '''

client.run(token.strip())

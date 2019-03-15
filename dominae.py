#Screengrabbot by Ewi OwO
#Code revisions by Maddie oo-woo

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

client = commands.Bot(command_prefix='>')

cwd = str(Path.home()) + "/.dominae"
img = cwd + "/img"
sh = cwd + "/sh"
txt = cwd + "/txt"
out = cwd + "/out"

tokenfile = open(txt + '/token.txt','r')
token = tokenfile.read()
tokenfile.close()

embedicon = 'https://cdn.discordapp.com/attachments/437821201461805066/552014178521710612/Centepeetle_GemPNG.webp' #Replace this link to change the embed icon!
embedcolor = 0x7900CE #Replace the value after '0x' with a hex color code to change the embed color

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

    now = datetime.now()
    justtimey = 'at {} \n'.format(now.strftime("%I:%M%p on %A, %B %d, %Y")) #Variable for showing verbose time and date
    embedtimey = '{}'.format(now.strftime("%a at %I:%M%p")) #Variable for simple time and date in embeds
    timeydate = 'by {} at {} \n'.format(author, now.strftime("%I:%M:%S%p on %A, %B %d, %Y")) #Variable for user activator followed by time and date

    prefile = open(txt + '/pre.txt','r') #Checks the bot prefix
    pre = prefile.read().strip()

    tfile = open(txt + '/toggle.txt','r') #Checks the toggle status
    toggle = tfile.read()

    if message.content.startswith(pre + "say"): #Special command prerequisites to prevent conflict between the commands and the case insensitivity
        pass
    elif message.content.startswith(pre + "addresp"):
        pass
    elif message.content.startswith(pre):
        message.content = message.content.lower()
    else:
        message.content = message.content.lower()
    
    if message.content.startswith('$off'): #Bot toggle off
        p = open(txt + '/toggle.txt','w')
        p.write("True")
        p.close

        await channel.send("Centipeetle is now poofed.\n(Dominae is now OFF.)")
        await channel.send(file=discord.File(img + "/off.gif"))

        activity = discord.Game(name="in a bubble")
        await client.change_presence(status=discord.Status.idle, activity=activity)
        print ("Centi enabled: " + toggle)
        print (timeydate)

    if message.content.startswith('$on'): #Bot toggle on
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

#centipeetle original commands

        if message.content.startswith(pre + 'fetch'): #cfetch

            subprocess.check_output(sh + "/cfetch.sh")
            with open(txt + '/screenfetch.txt', 'r') as fetchfile:
                fetch = fetchfile.read()
            embed = discord.Embed(description=fetch, color=embedcolor)
            embed.set_author(name="Screenfetch", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Screenfetch posted! ")
            print (timeydate)

        if message.content.startswith(pre + 'remfetch'): #cremfetch

            subprocess.check_output(sh + "/crem.sh")
            with open(txt + '/cremfetch.txt', 'r') as fetchfile:
                fetch = fetchfile.read()
            embed = discord.Embed(description=fetch, color=embedcolor)
            embed.set_author(name="Remote (Hellbox) Screenfetch", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Remote Screenfetch posted! ")
            print (timeydate)

        if 'i love you centi' in message.content:

            await channel.send(file=discord.File(img + '/lovepeetle.gif'))
            print ("Love given!")
            print (timeydate)

        if 'hungry bandit' and "your food's ours now" and "your food's" in message.content:
            
            await channel.send(file=discord.File(img + '/angry.gif'))
            print ("Hungry bandit.")
            print (timeydate)

        if 'csimon' in message.content:
            
            sez = message.content.replace("csimon","")
            await channel.send(sez)
            print ("Simon said!")
            print (timeydate)

        if message.content.startswith(pre + 'pacreb'): #cpacreb
            role_names = [role.name for role in author.roles]
            if "centipeetle wrangler" in role_names:   
                await channel.send("Running sudo pacman -Syu...")
                subprocess.check_output(sh + "/pac.sh")
                await channel.send("Pacman complete. Rebooting...")
                print ("Sudo pacman -Syu run! Rebooting now...")
                print (timeydate)
                
                subprocess.check_output(sh + "/reb.sh")

        if message.content.startswith(pre + 'pacman'): #cpacman
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

        if message.content.startswith(pre + 'reboot'): #creboot
            role_names = [role.name for role in author.roles]
            if "centipeetle wrangler" in role_names:
                await channel.send("Rebooting...")
                print ("Rebooting...")
                print (timeydate)
                
                subprocess.check_output(sh + "/reb.sh")
            else:
                print ("Reboot attempted???")
                print (timeydate)

        if 'chaps' in message.content:

            await channel.send("Squaw!")
            await channel.send(file=discord.File(img + "/cchaps.gif"))
            print ("Squaw! (chaps detected)")
            print (timeydate)
            
        if 'centipeetle' in message.content and 'how' in message.content and 'day' in message.content: #Centipeetle, how was your day?
            with open(txt + "/responses.txt", 'r') as resps:
                response = resps.readlines()
                await channel.send(random.choice(response))
                print ("How was my day?")
                print (timeydate)

        if message.content.startswith(pre + 'addresp'): #caddresp
            with open(txt + "/responses.txt", 'a') as resps:
                resps.write(message.content.replace(pre + 'addresp ','') + "\n")
                await channel.send("Response added: `" + message.content + "`")

        if message.content.startswith(pre + 'cbook'): #ccbook
            await channel.send(file=discord.File(img + "cbook.png"))
            print ("Special image uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'd420'): #cd420
            await channel.send("Rolling the **D420**, your number is **" + str(randint(1, 420)) + "**!")
            print ("The D420 has been cast!")
            print (timeydate)

        if any([keyword in message.content for keyword in (pre + 'pi', pre + 'server', pre + 'servecam', pre + 'pibm', pre + 'remote', pre + 'remotecam', pre + 'combo', pre + 'select')]):
            await channel.send("Squaw! (This command is disabled!)") #Disabled command list
            print ("Disabled command attempted!")
            print (timeydate)
            
        if message.content.startswith(pre + 'credits'): #ccredits
            embed = discord.Embed(description="**Dominae** -- a Discord screengrab bot by Elisha Shaddock\n**Centipeetle** -- a fork of Dominae by madgeraccoon\n\n**Less than Three**", color=embedcolor)
            embed.set_author(name="Credits", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Credits displayed!")
            print (timeydate)

        if message.content.startswith(pre + 'help'):
            helpbed = discord.Embed(description="**Dominae Commands** — `" + pre + "domhelp`\n\n**Centipeetle Commands** — `" + pre + "centihelp`")
            helpbed.set_author(name="Help Disambiguation", icon_url=embedicon)
            helpbed.set_footer(text=embedtimey)
            await channel.send(embed=helpbed)
            print ("Help disambiguation shown!")
            print (timeydate)

        if message.content.startswith(pre + 'domhelp'):

            embed = discord.Embed(description="**Dominae** — a Discord screengrab bot by Elisha Shaddock \n" + 
                                                     "`Dominae Commands` \n \n" +
                                                     "`" + pre + "help` shows this message. Who'd have thought? \n" + 
                                                     "`" + pre + "web` Takes a picture through my webcam \n" + 
                                                     "`" + pre + "mov` Takes a short clip through my webcam \n" + 
                                                     "`" + pre + "full` Takes a full screenshot of my monitors \n" + 
                                                     "`" + pre + "window` Takes a screenshot of the current window I'm using \n" + 
                                                     "`" + pre + "select` Forces me to select an area to screenshot \n" + 
                                                     "`" + pre + "server` Legacy command from Dominae; disabled \n" + 
                                                     "`" + pre + "servecam` Legacy command from Dominae; disabled \n" + 
                                                     "`" + pre + "say` Generates a text image out of some text \n" + 
                                                     "`" + pre + "vox` Generates an audio VOX sound. Use `" + pre + "vox help` for more info  \n" + 
                                                     "`$prefix` Sets the bot prefix. Default is s \n" + 
                                                     "`$on / $off` Enables or Disables all bot functions \n", color=embedcolor)
            embed.set_author(name="Dominae Help", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Dominae Help Shown")
            print (timeydate)

        if message.content.startswith(pre + 'centihelp'):

            embed2 = discord.Embed(description="**Centipeetle** — a fork of Dominae by madgeraccoon \n" + 
                                                     "`Centi Commands` \n \n" +
                                                     "`" + pre + "fetch`: Grab a simplistic text screenfetch from the host device \n" +
                                                     "`" + pre + "remfetch`: Grab a simplistic text screenfetch from a remote device \n" +
                                                     "`" + pre + "pacreb`: Runs `sudo pacman -Syu` to fully update your system and reboot \n" +
                                                     "`" + pre + "pacman`: Runs `sudo pacman -Syu` to fully update your system \n" +
                                                     "`" + pre + "reboot`: Reboots your system \n" +
                                                     "`" + pre + "cbook`: Personal command; uploads ~/Documents/cbook.png to the channel \n" +
                                                     "`" + pre + "d420`: Rolls the D420 \n" +
                                                     "`" + pre + "credits`: Displays credits for the bot \n" +
                                                     "`" + pre + "simon`: Has the bot repeat the containing message with `csimon` removed \n" +
                                                     "`i love you centipeetle`: Show affection \n" +
                                                     "`centipeetle, how was your day` or similar: Has the bot print a random response \n" +
                                                     "`" + pre + "addresp {RESPONSE}`: Add a response to the response pool \n" +
                                                     "`chaps` in message: Causes a Centipeetle response\n\n" +
                                                     "Less Than Three", color=embedcolor)
            embed2.set_author(name="Centi Help", icon_url=embedicon)
            embed2.set_footer(text=embedtimey)
            await channel.send(embed=embed2)
            print ("Dominae Help Shown")
            print (timeydate)

#dominae original commands

        if message.content.startswith(pre + 'full'): #cfull

            subprocess.check_output(sh + "/sfull.sh")
            await channel.send(file=discord.File(out + "/sfull.png"))
            print ("Screenshot (sfull) uploaded! ")
            print (timeydate)

        if message.content.startswith(pre + 'window'): #cfull

            subprocess.check_output(sh + "/swindow.sh")
            await channel.send(file=discord.File(out + "/swindow.png"))
            print ("Screenshot (swindow) uploaded!")
            print (timeydate)
        '''
        if message.content.startswith(pre + 'select'): #cselect

            subprocess.check_output(sh + "/sselect.sh")
            await channel.send(file=discord.File(out + "/sselect.png"))
            print ("Screenshot (sselect) uploaded!")
            print (timeydate)
        '''
        if message.content.startswith(pre + 'web'): #cweb

            subprocess.check_output(sh + "/sweb.sh")
            sweb = discord.File(out + "/sweb.png", filename="sweb.png")
            embed = discord.Embed(color=embedcolor)
            embed.set_author(name="Trashbox Cam", icon_url=embedicon)
            embed.set_image(url="attachment://sweb.png")
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed, file=sweb)
            print ("Webcam (sweb) uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'mov'): #cmov

            await channel.send("Recording...Please wait forever. (it takes a while.)")
            subprocess.check_output(sh + "/smov.sh")
            await channel.send(file=discord.File(out + "/smov.webm"))
            print ("Webcam (smov) somehow uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'say'): #csay

            f = open(txt + '/ssay.txt','w')
            f.write(message.content.replace(pre + "say ",""))
            f.close()

            subprocess.check_output(sh + "/ssay.sh")
            await channel.send(file=discord.File(out + '/ssay.png'))
            print ("Phrase (ssay) uploaded!")
            print ("'" + message.content.replace(pre + "say ","") + "'")
            print (timeydate)

        if message.content.startswith(pre + 'vox'): #cvox

            voxs = message.content.replace(pre + "vox ","")
            voxfn = voxs.replace(" ",".wav \n") + ".wav"
            voxfn += " svox.wav\n"
            voxfn = voxfn.lower()
            f = open(cwd + '/VOX/voxfn.txt','w')
            f.write(voxfn)
            f.close()

            subprocess.check_output(cwd + "/VOX/svox.sh")
            await channel.send(file=discord.File(cwd + '/VOX/svox.wav'))
            print ("Ass Naut Evacuation (svox) uploaded!")
            print ("Message: ""'" + message.content.replace(pre + "vox ","") + "'")
            print (timeydate)

        if message.content.startswith('$prefix'): #Change bot prefix

            f = open(txt + '/pre.txt','w')
            f.write(message.content.replace("$prefix ",""))
            with open(txt + '/pre.txt','r') as myfile:
                pre = myfile.read()
            f.close()
            print ("Prefix Changed to: " + "'" + message.content.replace("$prefix ","") + "'")
            print (timeydate)

        if message.content.startswith(pre + 'help svox'): #Help for svox

            await channel.send("Here are the current VOX keywords.")
            await channel.send(file=discord.File(img + "/svox.png"))
            print ("Black Mesa Tech Support notified! (help svox)")
            print (timeydate)

 #disabled commands

        '''
        if message.content.startswith(pre + 'remote'):

            subprocess.check_output(sh + "/sremote.sh")
            await channel.send(file=discord.File(out + '/serversync.png'))
            print ("Server Scrot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'servecam'):

            subprocess.check_output(sh + "/sremotecam.sh")
            await channel.send(file=discord.File(out + '/camsync.png'))
            print ("Server Webshot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'ping'):

            subprocess.check_output(sh + "/sping.sh")
            print ("Pi Shot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'ibm'):

            subprocess.check_output(sh + "/spibm.sh")
            await channel.send(file=discord.File(out + '/ibmsync.png'))
            print ("IBM Shot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'combo'):

            await channel.send("This will take a while...")
            subprocess.check_output(sh + "/scombo.sh")
            await channel.send(file=discord.File(out + '/result.png'))
            print ("Combo Shot Uploaded")
            print (timeydate)

        '''

client.run(token.strip())

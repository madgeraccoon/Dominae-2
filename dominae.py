#Screengrabbot by Ewi OwO

from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime
from random import randint
from pathlib import Path
from os import path
import random
import subprocess
import discord
import asyncio

client = commands.Bot(command_prefix='>')

cwd = str(Path.home()) + "/.dominae"
img = cwd + "/img"
sh = cwd + "/sh"
txt = cwd + "/txt"

tokenfile = open(txt + '/token.txt','r')
token = tokenfile.read()
tokenfile.close()

embedicon = 'https://cdn.discordapp.com/attachments/437821201461805066/552014178521710612/Centepeetle_GemPNG.webp'
embedcolor = 0x7900CE

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
    justtimey = 'at {} \n'.format(now.strftime("%I:%M%p on %A, %B %d, %Y"))
    embedtimey = '{}'.format(now.strftime("%a at %I:%M%p"))
    timeydate = 'by {} at {} \n'.format(author, now.strftime("%I:%M:%S%p on %A, %B %d, %Y"))

    prefile = open(txt + '/pre.txt','r')
    pre = prefile.read().strip()

    tfile = open(txt + '/toggle.txt','r')
    toggle = tfile.read()

    if message.content.startswith(pre + "say"):
        pass
    elif message.content.startswith(pre + "addresp"):
        pass
    elif message.content.startswith(pre):
        message.content = message.content.lower()
    else:
        message.content = message.content.lower()
    
    if message.content.startswith('$off'):
        p = open(txt + '/toggle.txt','w')
        p.write("True")
        p.close

        await channel.send("Centipeetle is now poofed.\n(Dominae is now OFF.)")
        await channel.send(file=discord.File(img + "/off.gif"))

        activity = discord.Game(name="in a bubble")
        await client.change_presence(status=discord.Status.idle, activity=activity)
        print ("Centi enabled: " + toggle)
        print (timeydate)

    if message.content.startswith('$on'):
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

        if message.content.startswith(pre + 'fetch'):

            subprocess.check_output(sh + "/cfetch.sh")
            with open(txt + '/screenfetch.txt', 'r') as fetchfile:
                fetch = fetchfile.read()
            embed = discord.Embed(description=fetch, color=embedcolor)
            embed.set_author(name="Screenfetch", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Screenfetch posted! ")
            print (timeydate)

        if message.content.startswith(pre + 'remfetch'):

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

        if 'csimon' in message.content:
            
            sez = message.content.replace("csimon","")
            await channel.send(sez)
            print ("Simon said!")
            print (timeydate)

        if message.content.startswith(pre + 'pacreb'):
            role_names = [role.name for role in author.roles]
            if "centipeetle wrangler" in role_names:   
                await channel.send("Running sudo pacman -Syu...")
                subprocess.check_output(sh + "/pac.sh")
                await channel.send("Pacman complete. Rebooting...")
                print ("Sudo pacman -Syu run! Rebooting now...")
                print (timeydate)
                
                subprocess.check_output(sh + "/reb.sh")

        if message.content.startswith(pre + 'pacman'):
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

        if message.content.startswith(pre + 'reboot'):
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
            
        if ['centipeetle', 'how', 'day'] in message.content:
            with open(txt + "/responses.txt", 'r') as resps:
                response = resps.readlines()
                await channel.send(random.choice(response))
                print ("How was my day?")
                print (timeydate)

        if message.content.startswith(pre + 'addresp'):
            with open(txt + "/responses.txt", 'a') as resps:
                resps.write(message.content.replace(pre + 'addresp ','') + "\n")
                await channel.send("Response added: `" + message.content + "`")

        if message.content.startswith(pre + 'cbook'):
            await channel.send(file=discord.File(str(Path.home()) + "/Documents/cbook.png"))
            print ("Chromebook screenshot uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'd420'):
            await channel.send("Rolling the **D420**, your number is **" + str(randint(1, 420)) + "**!")
            print ("The D420 has been cast!")
            print (timeydate)

        if any([keyword in message.content for keyword in (pre + 'pi', pre + 'server', pre + 'servecam', pre + 'pibm', pre + 'remote', pre + 'remotecam', pre + 'combo', pre + 'select')]):
            await channel.send("Squaw! (This command is disabled!)")
            print ("Disabled command attempted!")
            print (timeydate)
            
        if message.content.startswith(pre + 'credits'):
            embed = discord.Embed(description="**Dominae** -- a Discord screengrab bot by Elisha Shaddock\n**Centipeetle** -- a fork of Dominae by madgeraccoon\n\n**Less than Three**", color=embedcolor)
            embed.set_author(name="Credits", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Credits displayed!")
            print (timeydate)

#dominae original commands

        if message.content.startswith(pre + 'full'):

            subprocess.check_output(sh + "/sfull.sh")
            await channel.send(file=discord.File(img + "/sfull.png"))
            print ("Screenshot (sfull) uploaded! ")
            print (timeydate)

        if message.content.startswith(pre + 'window'):

            subprocess.check_output(sh + "/swindow.sh")
            await channel.send(file=discord.File(img + "/swindow.png"))
            print ("Screenshot (swindow) uploaded!")
            print (timeydate)
        '''
        if message.content.startswith(pre + 'select'):

            subprocess.check_output(sh + "/sselect.sh")
            await channel.send(file=discord.File(img + "/sselect.png"))
            print ("Screenshot (sselect) uploaded!")
            print (timeydate)
        '''
        if message.content.startswith(pre + 'web'):

            subprocess.check_output(sh + "/sweb.sh")
            sweb = discord.File(img + "/sweb.png", filename="sweb.png")
            embed = discord.Embed(color=embedcolor)
            embed.set_author(name="Trashbox Cam", icon_url=embedicon)
            embed.set_image(url="attachment://sweb.png")
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed, file=sweb)
            print ("Webcam (sweb) uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'mov'):

            await channel.send("Recording...Please wait forever. (it takes a while.)")
            subprocess.check_output(sh + "/smov.sh")
            await channel.send(file=discord.File(img + "/smov.webm"))
            print ("Webcam (smov) somehow uploaded!")
            print (timeydate)

        if message.content.startswith(pre + 'say'):

            f = open(txt + '/ssay.txt','w')
            f.write(message.content.replace(pre + "say ",""))
            f.close()

            subprocess.check_output(sh + "/ssay.sh")
            await channel.send(file=discord.File(img + '/ssay.png'))
            print ("Phrase (ssay) uploaded!")
            print ("'" + message.content.replace(pre + "say ","") + "'")
            print (timeydate)

        if message.content.startswith(pre + 'vox'):

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

        if message.content.startswith('$prefix'):

            f = open(txt + '/pre.txt','w')
            f.write(message.content.replace("$prefix ",""))
            with open(txt + '/pre.txt','r') as myfile:
                pre = myfile.read()
            f.close()
            print ("Prefix Changed to: " + "'" + message.content.replace("$prefix ","") + "'")
            print (timeydate)

        if message.content.startswith(pre + 'help svox'):

            await channel.send("Here are the current VOX keywords.")
            await channel.send(file=discord.File(img + "/svox.png"))
            print ("Black Mesa Tech Support notified! (help svox)")
            print (timeydate)

        if message.content.startswith(pre + 'help'):

            embed = discord.Embed(description="**Dominae** — a Discord screengrab bot by Elisha Shaddock\n**Centipeetle** — a fork of Dominae by madgeraccoon \n" + 
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
                                                     "`$on / $off` Enables or Disables all bot functions \n\n" +
                                                     "Less Than Three", color=embedcolor)
            embed.set_author(name="Dominae Help", icon_url=embedicon)
            embed.set_footer(text=embedtimey)
            await channel.send(embed=embed)
            print ("Help Shown")
            print (timeydate)

 #disabled commands

        '''
        if message.content.startswith(pre + 'sremote'):

            subprocess.check_output(sh + "/sremote.sh")
            await channel.send(file=discord.File(img + '/serversync.png'))
            print ("Server Scrot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'servecam'):

            subprocess.check_output(sh + "/sremotecam.sh")
            await channel.send(file=discord.File(img + '/camsync.png'))
            print ("Server Webshot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'ping'):

            subprocess.check_output(sh + "/sping.sh")
            print ("Pi Shot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'ibm'):

            subprocess.check_output(sh + "/spibm.sh")
            await channel.send(file=discord.File(img + '/ibmsync.png'))
            print ("IBM Shot Uploaded")
            print (timeydate)

        if message.content.startswith(pre + 'combo'):

            await channel.send("This will take a while...")
            subprocess.check_output(sh + "/scombo.sh")
            await channel.send(file=discord.File(img + '/result.png'))
            print ("Combo Shot Uploaded")
            print (timeydate)

        '''

client.run(token.strip())

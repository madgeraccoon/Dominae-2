hey! it actually worked!
# Centipeetle
Centipeetle is a discord.py bot forked from and heavily based on https://github.com/Evshaddock/Dominae-2 with several additions of varying magnitude, such as a command that rolls a d420, or a complete reorganization of 90% of the code. This is my first real project and I like to think I've learned a lot from it. The prerequisites are the same as the prerequisites for Dominae, with the addition of `fswebcam` in order for `sweb` to work. Anyways, enjoy!

## Centipeetle exclusives
(assumed prefix of 'c')
`cfetch`: Grab a simplistic text screenfetch from the host device detailing system information

`cremfetch`: Grab a simplistic text screenfetch from a remote device (needs additional setup in the crem.sh and cremfetch.sh files!!)

`cpacreb`: With sudo passwording disabled, runs `sudo pacman -Syu` to fully update your system followed by a reboot, provided you have a role named 'centipeetle wrangler'

`cpacman`: With sudo passwording disabled, runs `sudo pacman -Syu` to fully update your system, provided you have a role named 'centipeetle wrangler'

`creboot`: With sudo passwording disabled, reboots your system, provided you have a role named 'centipeetle wrangler'

`ccbook`: Personal command; uploads an image placed as ~/Documents/cbook.png to the channel activated from

`cd420`: Novelty; rolls the D420

`ccredits`: Displays credits for the bot

`{MESSAGE} csimon {MESSAGE}`: Has the bot repeat the containing message with `csimon` removed, as a simon says-esque command

`i love you centipeetle`: Novelty; shw affection

`centipeetle, how was your day` or any variation containing "centipeetle", "how" and "day": Novelty; has the bot read a random line from `txt/responses.txt` and print it to chat

`caddresp {RESPONSE}`: Novelty; add a response to the previous command's response pool.

`chaps` in message: Novelty; causes a Centipeetle response

## Disabled commands
Some commands from Dominae were disabled due to being Dominae-specific remote commands. These commands have no manuals or documentations, so enable and configure them at your own risk! To enable a disabled command, remove it from the triple apostrophe and remove its entry from the list of disabled commands (line ~196 at last revision).

## Issues and suggestions
If you stumble upon this bot and find an issue, feel free to report it to me and I'll try my best to fix or improve the bot!

# Dominae

A BASH and Discord.py Rewrite based Discord bot (Linux only!)
Main use is for taking pictures through the webcam of the system running the bot, along with other fun bits and bobs

## Getting Started

To get started, you need to have .dominae in your home directory and you need to run the install script to get all the prerequisites installed and the scripts in the right places, then you can run `dominae -t <token>` to set your bot token. then just run dominae and you should up up and running!

```
git clone https://github.com/Evshaddock/Dominae-2.git
cp -r /Dominae-2/.dominae/ ~
cd ~/.dominae/sh
./install.sh
dominae -t <bot token>
dominae
```

To run the bot in logging mode (for example if you want to start it up with your machine) you need to run 
```
dominae -l
```
this will write all bot activity to ~/.dominae/txt/log.txt

### Prerequisites

If you'd rather install the prerequisites yourself, or the script isn't working on your system here are all the required packages

```
scrot
imagemagick
ffmpeg
libffi
sox
python3.5
```

You'll also need to install some python modules. you can do that by doing this

```
sudo python3.5 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
sudo python3.5 -m pip install -U aiohttp
sudo python3.5 -m pip install -U websockets
```

Once that's done you should copy my startup script to your bin to make launching easier, you can do that by running this

```
sudo cp ~/.dominae/sh/dominae /usr/bin
```

If you'd rather run it without the launch script, just remember to put your bot token in `~/.dominae/txt/token.txt`, if it doesn't exist, create it.
Run the bot with `python35 ~/.dominae/dominae.py`

### Bot Features

`shelp` shows this message. Who'd have thought? 

`sweb` Takes a picture through my webcam 

`smov` Takes a short clip through my webcam 

`sfull` Takes a full screenshot of my monitors 

`swindow` Takes a screenshot of the current window I'm using 

`sselect` Forces me to select an area to screenshot 

`sserver` Takes a screenshot of a remote system[Not working (for now!)]

`sservecam` Takes a picture from a remote systems camera [Not working (for now!)]

`ssay` Generates a text image out of some text 

`svox` Generates an audio VOX sound. Use svox help for more info

`#PREFIX` Sets the bot prefix. Default is `s`

`#ON` / `#OFF` Enables or Disables all bot functions

`scombo` This is meant to take every available image and stitch them together into one giant image to post. It's not functional without the new SSH system implemented so consider this a 'coming soon' type deal.

Note: You might notice there are some functions that connect to other machines. These use SSH and aren't ready to be implemented in my public release of this bot. I will have a system for setting this up eventually.


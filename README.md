

![CENTIPEETLE](https://i.imgur.com/CMAgKZs.png)

<p align="center"><a href="https://github.com/Evshaddock/Dominae-2">a fork of Dominae</a></p>

## Introduction

Centipeetle is a discord.py bot with over 60 commands of varied purpose and utility, such as weather reportsdice rolling, timers with messages, editable reminder lists, novelty chat commands, media commands and more!

## Centipeetle command examples

The default prefixes are `c` for user commands and `$` for admin commands, but both can be changed in `centi.json ` or with `$setval`.

##### Utility / Fun

- `cweather` or `cweather {LOCATION}` - Sends an embed with weather descriptions, wind speeds and temperatures for the user's default location, the given location, or the default location built into the bot; users can set a default location with `csetweather {LOCATION}`
- `cd {NUMBER}` or `cd{NUMBER}` - Rolls a number between 1 and the given number for the user
- `cchoice` or `cchoice {OPTION}, {OPTION}, {OPTION}` - Chooses between any amount of given options separated by commas/semicolons or chooses between yes and no
- `cfetch` - Posts a simplified screenfetch from the device running the bot
- `cpfp {USER ID}` - Grabs a user's profile picture given a user ID

##### Youtube Commands

- `cyt` - Searches for a YouTube video with the given search criteria
- `cyts` - Searches for a YouTube video, but gives the user a list of 5 videos with titles similar to the search criteria

##### Novelty Commands

- `centi, how is your day` or any combination of `centi`, `how` and `day` - Chooses a random response from `txt/responses.txt` for Centipeetle to respond with
- `caddresp {RESPONSE}` - Adds a response to the `centi how day` response pool

##### Media

- `cweb` - Takes a picture through a webcam attached to the host device (using fswebcam)
- `cfull` - Takes a picture of the host device's entire screen.
- `ccol` - Generates solid color images or multi-color gradients from specified hex codes, or "random" in the place of a hex code
- `cflag` - Generates flag designs with specified hex codes, or "random" in the place of a hex code
- `credd`, `cfood` and `cplate` - Posts a random submission from a specified subreddit OR based on the command. `credd {SUBREDDIT}` for specified subreddits, `cfood` for /r/shittyfoodporn, and `cplate` for /r/wewantplates
- `csay` - Generates a large text image of the specified message in the Crewniverse font. Alternatives include `cfam`, `cfort`, `chalo`, and `ccraft`
- `cvox "{MESSAGE}" {VOICE CHOICE}` - Generates a text-to-speech audio version of the specified message using one of several voices from acapela-group; a full list of voices are in the wiki ([Standalone terminal version of acapyla here](https://github.com/maddoxdragon/acapyla))
- `cplay {SOUND NAME}` - Plays a sound file from a pre-existing list of sound files in `audio/sound/` in the user's current voice chat. A full list of sounds are in the wiki

##### Reminders

- `creminder` - A suite of commands for users to create their own reminder lists. A list of subcommands are given by the bot or found in the wiki.
- `calarm` - An alarm command with a customizable message. When the alarm's time elapses, the bot messages the user

<p align="center"><a href="https://github.com/maddoxdragon/Centipeetle/wiki">A full list of commands in their proper categories can be found in the wiki.</a></p>

## Installation

#### Before installing:

- Create a Discord bot application and token ([This guide should do](https://www.writebots.com/discord-bot-token/))

- Sign up for OpenWeatherMap ([here](https://home.openweathermap.org/users/sign_up)) and get an API key (for weather functionality;  `cweather`) *

- Create a YouTube API project ([here](https://console.developers.google.com/apis/api/youtube.googleapis.com/credentials)) and get an API key (for video searching functionality; `cyt` and `cyts`) *

- Get an API key for the currconv API [here](https://free.currencyconverterapi.com/free-api-key) (for `cconv`) *

- Create a Reddit application ([here](https://www.reddit.com/prefs/apps)) and get an ID and secret key through the form [here](https://www.reddit.com/wiki/api) (for Reddit functionality; `credd`, `cfood`, `cplate`) *

- Invite the bot to your server with an invite link from the Discord developer portal (usually looks like `https://discord.com/api/oauth2/authorize?client_id={CLIENT ID HERE}&permissions=0&scope=bot`)

  <p align="center">* - Steps with an asterisk can be skipped at the cost of their listed commands; to prevent problems, comment out each listed command by putting a # at the beginning of each line in the command block.</p>

#### Installation

1. Clone the repo to your home directory (e.g. `~/.centipeetle/centi.py`)

2. Install the Python module requirements with `pip install -r ~/.centipeetle/txt/requirements.txt` (make sure to use the pip that corresponds to your Python installation, for example `pip3.5` for `python3.5`)

3. Install the package requirements by running `~/.centipeetle/sh/install.sh` (note: if the script doesn't run, run `sudo chmod +x ~/.centipeetle/sh/install.sh` and try again.)

   If the script doesn't work:

   - Install the packages from the list below with your package manager
   - Copy `~/.centipeetle/sh/centipeetle` to `/usr/bin/` for easy use from terminal

4. Edit `~/.centipeetle/txt/centi.json` to insert the Discord bot token and the API keys for OpenWeatherMap, currconv and Reddit (and add the YouTube API key to ``~/.centipeetle/txt/ytapi`)

5. Run the script with `centipeetle` or `python ~/.centipeetle/centi.py`!

## Packages and Modules

In case the requirements.txt file doesn't give you every module you need or install.sh misses something, a list of prerequisites are as follows:

#### Packages:

```
python35 (recommended; you can use any version of python over 3.5 as long as you use the pip that belongs with it)
scrot
imagemagick
screenfetch
youtube-dl
screen (OPTIONAL; very useful for running the bot in the background)
ffmpeg
libffi
sox
```

#### Modules (from requirements.txt):

```
aiohttp==3.6.2
async-timeout==3.0.1
attrs==19.3.0
certifi==2020.4.5.1
cffi==1.14.0
chardet==3.0.4
discord==1.0.1
discord.py==1.3.3
idna==2.9
idna-ssl==1.1.0
multidict==4.7.6
mutagen==1.44.0
praw==7.0.0
prawcore==1.4.0
pycparser==2.20
PyNaCl==1.3.0
python-dateutil==2.8.1
requests==2.23.0
six==1.15.0
SoundFile==0.10.3.post1
typing-extensions==3.7.4.2
update-checker==0.17
urllib3==1.25.9
websocket-client==0.57.0
websockets==6.0
yarl==1.4.2
```

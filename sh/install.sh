#!/bin/sh

# Installer script for Centipeetle. (Thanks Robin)

if grep ID /etc/os-release | grep -qE "fedora"; then
    echo "Fedora detected! Installing prerequisites..."
	sudo dnf install \
		scrot \
		imagemagick \
		epel-release \
		https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm \
		ffmpeg \
		ffmpeg-devel \
		libffi \
		sox \
		python35 
    sudo cp $HOME/.centipeetle/sh/centipeetle /usr/bin
    echo "Done. Don't forget to set up txt/centi.json with your token and API keys!"
    
elif grep ID /etc/os-release | grep -qE 'debian|ubuntu'; then
	DEBIAN_FRONTEND=noninteractive
	DEBCONF_NONINTERACTIVE_SEEN=true
        export DEBIAN_FRONTEND DEBCONF_NONINTERACTIVE_SEEN
    echo "Debian / Ubuntu detected. Installing prerequisites..."
    sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt-get update
	sudo apt-get install \
		scrot \
		imagemagick \
		ffmpeg \
		ffmpeg-devel \
		libffi \
		sox \
		python3.5 
    sudo cp $HOME/.centipeetle/sh/centipeetle /usr/bin
    echo "Done. Don't forget to set up txt/centi.json with your token and API keys!"
    
elif grep ID /etc/os-release | grep -q 'arch\|manjaro'; then
    echo "Arch / Manjaro detected. Installing prerequisites..."
	sudo pacman -S \
		scrot \
		imagemagick \
		ffmpeg \
		ffmpeg-devel \
		libffi \
		sox \
		python35 
    sudo cp $HOME/.centipeetle/sh/centipeetle /usr/bin
    echo "Done. Don't forget to set up txt/centi.json with your token and API keys!"
    
else
	echo "Sorry, I haven't added support for your OS's package manager yet. You can find the list of prerequisites at the bottom of the repo and install them manually, then copy ~/.centipeetle/sh/centipeetle to your /usr/bin"
fi

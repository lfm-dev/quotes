#!/bin/bash

if [ -L "/usr/local/bin/quotes" ]; then
    sudo rm "/usr/local/bin/quotes"
fi

if [ -d "/usr/local/bin/quotes_files" ]; then
    sudo rm -r "/usr/local/bin/quotes_files"
fi

if [ ! -d "$HOME/.config/quotes" ]; then
    mkdir "$HOME/.config/quotes"
    while : ; do
        echo -n "path to your quotes: "
        read pathToQuotes
        if [ -d "$pathToQuotes" ]; then
            echo "quotes_path,$pathToQuotes" > $HOME/.config/quotes/settings.csv
            break
        else
            echo "$pathToQuotes doesnt exists, try again."
        fi
    done
fi

sudo cp -r src /usr/local/bin/quotes_files
cd /usr/local/bin
sudo ln -s /usr/local/bin/quotes_files/quotes.py quotes
sudo chmod a+rx quotes

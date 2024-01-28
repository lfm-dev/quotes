#!/bin/bash

if [ -L "/usr/local/bin/quotes" ]; then
    sudo rm "/usr/local/bin/quotes"
fi

if [ -d "/usr/local/bin/quotes_files" ]; then
    sudo rm -r "/usr/local/bin/quotes_files"
fi

while : ; do
    echo -n "path to your quotes: "
    read pathToQuotes
    if [ -d "$pathToQuotes" ]; then
        break
    else
        echo "$pathToQuotes doesnt exists, try again."
    fi
done

wget http://github.com/lfm-dev/quotes/archive/master.zip -O quotes.zip
unzip quotes.zip
sed -i -e "s#QUOTES_PATH = '/path/to/your/quotes/folder'#QUOTES_PATH = '$pathToQuotes'#" quotes-main/src/quotes.py # add path to script
sudo cp -r quotes-main/src /usr/local/bin/quotes_files
rm -r quotes-main quotes.zip
cd /usr/local/bin
sudo ln -s /usr/local/bin/quotes_files/quotes.py quotes
sudo chmod a+rx quotes
#!/bin/bash
sudo ir-keytable -p unknown -p other -p lirc -p rc-5 -p jvc -p sony -p nec -p sanyo -p rc-6 -p sharp -p xmp
stdbuf -o L ir-keytable -t | python remote-gtts/remote2gtts.py

#!/bin/python
import sys
import vlc
import os
import re
from tempfile import *
from gtts import gTTS
from remote2text import RGBRemote2Text


parser = RGBRemote2Text(verbose=True)

while True:
    ir_out = input()
    response = parser.process(ir_out)

    if response:
        tts = gTTS(text=response, lang='pt')
        tmp = NamedTemporaryFile(delete=False)
        tts.write_to_fp(tmp)

        path = os.path.join(gettempdir(), str(tmp.name))
        vlc.MediaPlayer(path).play()

        tmp.close()

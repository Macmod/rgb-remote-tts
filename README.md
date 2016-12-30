# RGB-Remote-TTS

Turning a `Magic Lightning` RGB remote into a text-to-speech controller with a RTL2832U dongle.

# How?

1. Install [librtlsdr](https://github.com/librtlsdr/librtlsdr).
2. Run `pip install -r requirements.txt` to pull python dependencies.
3. Plug in your RTL2832U and make sure you have `rtl_ir` and `ir-keytable` working properly.
4. Run `rgb-remote-tts.sh` to begin listening for events.
5. Type something interesting in your RGB controller and hit SEND.

# Why?

Let me know if you find out.

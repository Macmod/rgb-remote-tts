#!/bin/python
from re import search


class Remote2Text:
    def __init__(self, table={}, actions={}, verbose=False):
        self.text = ''
        self.sent = False

        self.table = table
        self.actions = actions
        self.verbose = verbose

    def send(self, code):
        self.sent = True

        if self.verbose:
            print('> [SEND]')

        return self.text

    def write(self, code):
        if self.sent:
            self.text = ''
            self.sent = False

        self.text += self.table[code]

        if self.verbose:
            print(self.text)

        return None

    def process(self, raw):
        scan = search(r"scancode = 0x([0-9a-z]{2})", raw)

        if scan is not None:
            code = int(scan.group(1), 16)
            if self.verbose:
                print(">", code)

            if code in self.actions:
                handler = self.actions[code]
            elif code in self.table:
                handler = self.write
            else:
                handler = self.error

            return handler(code)

class RGBRemote2Text(Remote2Text):
    TABLE = {
        0x05: 'a', 0x04: 'b', 0x06: 'c',
        0x09: 'd', 0x08: 'e', 0x0a: 'f',
        0x0b: 'g', 0x0d: 'h', 0x0c: 'i',
        0x0e: 'j', 0x0f: 'l', 0x15: 'm',
        0x14: 'n', 0x16: 'o', 0x17: 'p',
        0x19: 'q', 0x18: 'r', 0x1a: 's',
        0x1b: 't', 0x11: 'u', 0x10: 'v',
        0x12: 'x', 0x13: 'z'
    }

    def __init__(self, verbose=False):
        actions = {
            0x07: self.send
        }

        super().__init__(table=RGBRemote2Text.TABLE,
                         actions=actions,
                         verbose=verbose)

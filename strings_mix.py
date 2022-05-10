"""
https://www.codewars.com/kata/5629db57620258aa9d000014
"""

import string
from collections import defaultdict
from dataclasses import dataclass


class CharData:
    def __init__(self, name="", origin="", count=-1) -> None:
        self.name = name
        self.origin = origin
        self.count = count


class Mixer:
    def __init__(self) -> None:
        self.charlist = []
        self.c = CharData()

    def mix(self, s1, s2):
        self.populate_list(s1, s2)
        self.charlist.sort(key=lambda x: (-x.count, x.origin, x.name))

        res = []

        for item in self.charlist:
            res.append(item.origin + item.count * item.name)

        return "/".join(res)

    def populate_list(self, s1, s2):
        for char in string.ascii_lowercase:
            count1 = s1.count(char)
            count2 = s2.count(char)

            c = CharData()
            if count1 > count2:
                c.name = char
                c.origin = "1:"
                c.count = count1
            if count1 < count2:
                c.name = char
                c.origin = "2:"
                c.count = count2
            if count1 == count2:
                c.name = char
                c.origin = "=:"
                c.count = count2

            if c.count > 1:
                self.charlist.append(c)


def mix(s1, s2):
    mixer = Mixer()
    return mixer.mix(s1, s2)


s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"

mix(s1, s2)

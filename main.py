# -*- coding: utf-8 -*-
import re
class Version:
    def __init__(self, s):
        self.partes = tuple(int(p) for p in str(s).split('.'))
    def __repr__(self):
        return f"Version({'.'.join(map(str,self.partes))})"
    def __eq__(self, other):
        return self.partes == other.partes
    def __lt__(self, other):
        return self.partes < other.partes


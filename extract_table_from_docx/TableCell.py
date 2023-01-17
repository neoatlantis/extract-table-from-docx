#!/usr/bin/env python3

from bs4 import BeautifulSoup

class TableCell:

    def __init__(self, parent, xml, id):
        self.cell_id = id
        self.parent = parent

        preamble = xml.find("w:tcPr")

        vMerge = preamble.find("w:vMerge")
        if vMerge:
            self.vMerge = vMerge["w:val"]
        else:
            self.vMerge = None
        
        gridSpan = preamble.find("w:gridSpan")
        if gridSpan:
            self.gridSpan = gridSpan["w:val"]
        else:
            self.gridSpan = None

        print(repr(self))

    def __repr__(self):
        return "<TableCell gridSpan=%s vMerge=%s>" % (
            self.gridSpan,
            self.vMerge
        )
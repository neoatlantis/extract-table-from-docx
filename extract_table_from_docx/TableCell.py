#!/usr/bin/env python3

from bs4 import BeautifulSoup

class TableCell:

    def __init__(self, parent, xml, id):
        self.parent = parent
        self.row_id = self.parent.row_id
        self.cell_id = id

        preamble = xml.find("w:tcPr")
        self.__p = xml.find("w:p")

        vMerge = preamble.find("w:vMerge")
        if vMerge:
            self.vMerge = vMerge["w:val"]
        else:
            self.vMerge = None
        
        gridSpan = preamble.find("w:gridSpan")
        if gridSpan:
            self.gridSpan = int(gridSpan["w:val"])
        else:
            self.gridSpan = None



    def __compute_value(self):
        # TODO return value for this cell
        return " ".join([e.getText() for e in self.__p.find_all("w:t")])




    @property
    def value(self):
        # if not merged vertically, return self value
        if not self.vMerge or self.vMerge == "restart":
            return self.__compute_value()
        # if vMerged, return self value, when self is restart, otherwise,
        # return value of last row
        return self.parent.parent.row(self.row_id-1).cell(self.cell_id).value

    @property 
    def colspan(self):
        if not self.gridSpan: return 1
        return self.gridSpan


    @property    
    def merged(self):
        return self.vMerge != None or self.gridSpan != None

    def __repr__(self):
        return "<TableCell gridSpan=%s vMerge=%s>" % (
            self.gridSpan,
            self.vMerge
        )
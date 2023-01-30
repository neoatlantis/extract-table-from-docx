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
            self.vMerge = vMerge["w:val"] if "w:val" in vMerge else "continue"
        else:
            self.vMerge = None
        #print("(%d,%d) vMerge=%s" % (self.row_id, self.cell_id, self.vMerge), self.__compute_value())
        
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
        # Returns cell value, when this cell is not merged, or is start point
        # of a vertical merge (restart)
        if not self.vMerge or self.vMerge == "restart":
            return self.__compute_value()
        # Dealing "continue" cells ---> Check above cell.
        # - If above cell is "continue", ask the value recursively.
        # - If it's restart, use its value.
        # - If above cell is None and we are still trying to "continue" from
        #   it, which is not expected, treat current cell as "restart", that is,
        #   return current cell value. 
        above_cell = self.parent.parent.row(self.row_id-1).cell(self.cell_id)
        if above_cell.vMerge in ["continue", "restart"]:
            return above_cell.value
        else:
            return self.__compute_value()

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
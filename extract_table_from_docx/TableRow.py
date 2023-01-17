#!/usr/bin/env python3

from bs4 import BeautifulSoup
from .TableCell import TableCell

class TableRow:

    def __init__(self, parent, xml, id):
        self.row_id = id
        self.parent = parent
        print("RRRRRRRRRRRRRRRRRRRRRRRR")

        all_cells = xml.find_all("w:tc")
        self.cells = []
        for i in range(0, len(all_cells)):
            self.cells.append(TableCell(self, all_cells[i], id=i))

    def cell(self, i):
        if i < len(self.cells):
            return self.cells[i]
        raise Exception("No cell #%s for row #%s." % (i, self.row_id))

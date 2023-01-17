#!/usr/bin/env python3

from bs4 import BeautifulSoup
from .TableCell import TableCell

class TableRow:

    def __init__(self, parent, xml, id):
        self.row_id = id
        self.parent = parent

        all_cells = xml.find_all("w:tc")
        self.cells = []
        cell_id = 0
        for i in range(0, len(all_cells)):
            tc = TableCell(self, all_cells[i], id=cell_id)
            cell_id += tc.colspan
            self.cells.append(tc)

        self.__length = cell_id

    def cell(self, i):
        for cell in self.cells:
            if cell.cell_id <= i < cell.cell_id + cell.colspan:
                return cell
        raise Exception("No cell #%s for row #%s." % (i, self.row_id))

    @property 
    def length(self):
        return self.__length
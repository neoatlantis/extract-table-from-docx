#!/usr/bin/env python3

from bs4 import BeautifulSoup
from .TableRow import TableRow

class Table:

    def __init__(self, xml):
        self.rows = []
        all_trs = xml.find_all("w:tr")

        for i in range(0, len(all_trs)):
            self.rows.append(TableRow(self, all_trs[i], id=i))
        self.__length = len(all_trs)

    def row(self, i):
        return self.rows[i]

    @property 
    def length(self):
        return self.__length
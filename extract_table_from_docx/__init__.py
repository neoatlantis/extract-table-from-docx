#!/usr/bin/env python3

import zipfile
from bs4 import BeautifulSoup
from .Table import Table

def extract_table_from_docx(filepath):

    docx = zipfile.ZipFile(filepath)
    xml = BeautifulSoup(docx.read("word/document.xml"), features="xml")

    tables = xml.find_all("w:tbl")

    for table in tables:
        yield Table(table)
        
    

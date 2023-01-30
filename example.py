#!/usr/bin/env python3

import sys
from extract_table_from_docx import extract_table_from_docx


tables = extract_table_from_docx(sys.argv[1])

i = 0

for table in tables:

    i += 1
    print("Extract table #%d.................." % i)

    for row_i in range(0, table.length):
        row = table.row(row_i)

        row_print = []
        for col_i in range(0, row.length):

            cell = row.cell(col_i)

            row_print.append(cell.value)
        
        print(("%2d #" % row_i) + "|".join([str(e)[:10].rjust(12) for e in row_print]))
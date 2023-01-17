Extract table from docx
=======================

This is a tiny library for extracting table(s) from a .docx Word document.

To use:

```python
from extract_table_from_docx import extract_table_from_docx

tables = extract_table_from_docx(sys.argv[1])
table = next(tables) # get the first table in file

for row_i in range(0, table.length):
    row = table.row(row_i)  # get a row using table.row()

    row_print = []
    for col_i in range(0, row.length):

        cell = row.cell(col_i)  # get a cell using row.cell()

        row_print.append(cell.value)
    
    print("|".join([str(e).rjust(10) for e in row_print]))
```

And output:

```
$ python3 example.py sample.docx  
       1,1|       1,2|       1,3|       1,4|       1,5
       2,1|       1,2|       2,3|       2,3|       2,5
       3,1|       3,2|       2,3|       2,3|       3,5
       4,1|       4,2|       4,3|       4,4|       4,5
       5,1|       5,2|       5,3|       5,3|       5,3
       6,1|       5,2|       6,3|       6,4|       6,5
       7,1|       7,2|       6,3|       7,4|       7,5
```

## With regards to cell merging

This library understands vertically and/or horizontally merged cells.

`table.row(row_id).cell(cell_id)` will return the content of cell located
at `(row_id, cell_id)`, where both IDs are numbers as if no cells were merged.

In above example, getting cell at (2,2) will return contents of cell (1,2), as
in `example.doc` both (2,2) and (1,2) are merged. Same holds for (2,4),(3,3),
(3,4), as all these 3 cells are merged as a 2x2 square with (2,3).

`table.length` and `row.length` are therefore both safe upper limits that can
be used when iterating over rows or columns.
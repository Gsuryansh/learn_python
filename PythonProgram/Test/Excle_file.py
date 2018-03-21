import os
from os import walk
import xlrd
workbook=xlrd.open_workbook("ArticleList.xls")
sheet=workbook.sheet_by_index(0)
print(workbook.nsheets)
print(workbook.sheet_names())
print(sheet.row_values(0))
print(sheet.ncols)
print(sheet.nrows)
print(os.path.abspath(os.curdir))
os.chdir(os.path.abspath(os.curdir))
print(os.path.abspath(os.curdir))
f = []
for (dirpath, dirnames, filenames) in walk(os.curdir):
    f.extend(filenames)
    break
print(f)
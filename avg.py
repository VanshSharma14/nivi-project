from openpyxl import load_workbook
import utils

workbook = load_workbook(filename='data.xlsx')
ws = workbook.active

# print(ws['A12'].value)
index = 0
inArr = []
valArr = []
closest = 0
for row in ws.iter_rows(min_row=58, min_col=3, max_col=7, max_row=97, values_only=True):
        for cell in row:
                index += 1
        print("Index: ", index)


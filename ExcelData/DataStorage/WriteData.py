from selenium import webdriver
import openpyxl

#Mention the location of Excel File
path = "D:\BlankExcel.xlsx"

workbook = openpyxl.load_workbook(path)
#if one sheet present active should be displayed
sheet = workbook.active

for r in range(1,5):
    for c in range(1,3):
#write data in rows and column
sheet.cell(row=r,column=c).value= "Automation"

#Save the Data
workbook.save(path)
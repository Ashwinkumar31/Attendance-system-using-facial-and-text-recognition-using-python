import pytesseract
import PIL.Image
import cv2
import xlsxwriter
import glob
import os.path,time
path = glob.glob("C:/Users/lambo/PycharmProjects/FORLOOP/*.png")
row = 0
workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()
M=['ASHWINKUMAR HEGDE KR','BHARATH JS','MAYANK K JAISWAL']
for j in path:
     print(j)
     myconfig = r"--psm 3 --oem 3"
     pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lambo\AppData\Local\tesseract.exe'
     text = pytesseract.image_to_string(PIL.Image.open(j), config=myconfig)
     T = (time.ctime(os.path.getmtime(j)))
     print(text)
     column = 0
     S = text.split('\n')
     print(S)
     for i in M:
          for k in S:
            if i==k:
              worksheet.write(row, 0, k)
     worksheet.write(row, 1, T)
     row+=1
workbook.close()
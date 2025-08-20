from tkinter import *
from tkinter import filedialog as fd
import os
from datetime import datetime

window = Tk()
window.withdraw() #hide window

dir_name = fd.askdirectory()

if dir_name:
   
    for file_name in os.listdir(dir_name):
        if file_name.lower().endswith((".doc", ".docx")):
            filepath = os.path.join(dir_name, file_name) #path to the file
            last_modified = os.path.getmtime(filepath) #last modified date of the file
            #convert to datetime object
            to_date = datetime.fromtimestamp(last_modified).strftime("%d.%m.%Y") 
            print("Выбранная вами папка содержит doc файл: ")
            print(file_name) #list all the doc & docx files in the directory
            print("Последнее изменение файла: ")
            print(to_date)
            
else:
    print("No directory selected")
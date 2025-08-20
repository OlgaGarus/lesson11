from tkinter import *
from tkinter import filedialog as fd
import os
import shutil
from datetime import datetime
from tkinter import messagebox as mb

window = Tk()
window.withdraw() #hide window

def choose_dir():
    dir_name = fd.askdirectory()
    if dir_name:
        organize_photos(dir_name)
    window.destroy()


def organize_photos(directory):
    try:
        for file_name in os.listdir(directory):
            if file_name.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
                filepath = os.path.join(directory, file_name)
                time_stamp = os.path.getmtime(filepath) 
                date = datetime.fromtimestamp(time_stamp)
                date_str = date.strftime("%Y-%m")
                new_filepath = os.path.join(directory, date_str)
                
                if not os.path.exists(new_filepath):
                    os.makedirs(new_filepath)
                shutil.move(filepath, os.path.join(new_filepath, file_name))
                
        mb.showinfo("Успех", "Фотографии успешно сортированы!")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")

# Вызываем функцию выбора папки
choose_dir()

# Запускаем главный цикл (но он быстро завершится после destroy)
window.mainloop()
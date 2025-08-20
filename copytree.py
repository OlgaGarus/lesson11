from tkinter import *
from tkinter import filedialog as fd
import os
import shutil

window = Tk()
window.withdraw() #hide window

dir_name = fd.askdirectory(title="Выберите папку с файлами .doc,.docx для перемещения.")
if dir_name:
    new_dir = dir_name + "_new"
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        for file_name in os.listdir(dir_name):
            if file_name.lower().endswith((".doc", ".docx")):
                filepath = os.path.join(dir_name, file_name)
                new_filepath = os.path.join(new_dir, file_name)
                try:
                    # Копируем файл
                    shutil.move(filepath, new_filepath)
                    print(f"Файл {file_name} был перемещен")
                    
                except Exception as e:
                    print(f"Ошибка при перемещении {file_name}: {e}")
        
        print("Перемещение завершено")
    else:
        print(f"Папка {new_dir} уже существует.")
else:
    print("Папка не выбрана")

window.destroy()
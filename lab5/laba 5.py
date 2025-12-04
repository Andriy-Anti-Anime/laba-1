import matplotlib
import time
import random
import pandas as pd
import json
import numbers
import os
import math
import requests
import numpy

#time
def lib_time():
    try:
        time.sleep(3)
        print("time")
    except Exception as e:
        print(e)

lib_time()

#pandas
student_data={
    'Ім\'я': ['Олег', 'Наталя', 'Ігор', 'Марія'],
    'Спеціальність': ['КН', 'Менеджмент', 'КН', 'Дизайн'],
    'Вік': [20, 21, 19, 20],
    'Середній_Бал': [4.5, 3.8, 4.9, 4.2]
}
df = pd.DataFrame(student_data)

# Виведення створеного DataFrame
print("--- Створений DataFrame ---")
print(df)

#random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(f"Перемішаний список: {my_list}")

#json
python_dict = {"name": "Іван", "age": 30}

# Серіалізація: Python -> JSON (рядок)
json_string = json.dumps(python_dict, ensure_ascii=False, indent=4)
print(json_string)

# Десеріалізація: JSON (рядок) -> Python
back_to_python = json.loads(json_string)
print(back_to_python['name'])

#os
print("--- Робота з каталогами ---")

# 1. Дізнатися, в якому каталозі ми зараз знаходимося (Подібно до команди 'pwd')
current_dir = os.getcwd()
print(f"1. Поточний робочий каталог: \n   {current_dir}\n")

# 2. Отримати список всіх файлів та папок у цьому каталозі (Подібно до команди 'ls')
contents = os.listdir(current_dir)
print(f"2. Вміст каталогу ({len(contents)} елементів):")

# Виведення перших 5 елементів для короткості
for item in contents[:5]:
    print(f"   - {item}")

# Якщо елементів більше, ніж 5
if len(contents) > 5:
    print("   ...")
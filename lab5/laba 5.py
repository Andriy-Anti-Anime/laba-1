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


# time
def lib_time():
    try:
        time.sleep(3)
        print("time")
    except Exception as e:
        print(e)



# pandas
def table():
    try:
        student_data = {
            'Ім\'я': ['Олег', 'Наталя', 'Ігор', 'Марія'],
            'Спеціальність': ['КН', 'Менеджмент', 'КН', 'Дизайн'],
            'Вік': [20, 21, 19, 20],
            'Середній_Бал': [4.5, 3.8, 4.9, 4.2]
        }
        df = pd.DataFrame(student_data)

        print("--- Створений DataFrame ---")
        print(df)
    except Exception as e:
        print(e)


# random
def list_fun():
    try:
        my_list = [1, 2, 3, 4, 5]
        random.shuffle(my_list)
        print(f"Перемішаний список: {my_list}")
    except Exception as e:
        print(e)

    # json


def list_dict():
    try:
        python_dict = {"name": "Іван", "age": 30}

        json_string = json.dumps(python_dict, ensure_ascii=False, indent=4)
        print(json_string)

        back_to_python = json.loads(json_string)
        print(back_to_python['name'])
    except Exception as e:
        print(e)




# os
def list_OS():
    try:
        print("--- Робота з каталогами ---")

        current_dir = os.getcwd()
        print(f"1. Поточний робочий каталог: \n   {current_dir}\n")

        contents = os.listdir(current_dir)
        print(f"2. Вміст каталогу ({len(contents)} елементів):")

        for item in contents[:5]:
            print(f"   - {item}")



        for item in contents[:5]:
            print(f"   - {item}")

        # Якщо елементів більше, ніж 5
        if len(contents) > 5:
            print("   ...")

    except Exception as e:
        print(e)

def main():
    lib_time()
    list_OS()
    list_dict()
    table()
    list_fun()

if __name__ == "__main__":
    main()

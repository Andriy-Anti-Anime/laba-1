grades = {}

print("Введіть ім'я студента та його оцінку (1–12). Щоб завершити — введіть 'стоп'.")

while True:
    name = input("Ім'я студента: ")
    if name.lower() == "стоп":
        break

    grade = int(input(f"Оцінка для {name}: "))
    if 1 <= grade <= 12:
        grades[name] = grade
    else:
        print("Оцінка має бути від 1 до 12!")

if not grades:
    print("Немає введених даних.")
else:
    print("\n--- Результати ---")
    for name, grade in grades.items():
        print(f"{name}: {grade}")

    # Обчислення середнього бала
    aver = sum(grades.values()) / len(grades)
    rounded_aver = round(aver, 1)
    print(f"Середній бал по групі: {rounded_aver}")

    # Категорії студентів
    excell = []
    good = []
    poor = []
    fail = []

    for name, grade in grades.items():
        if 10 <= grade <= 12:
            excell.append(name)
        elif 7 <= grade <= 9:
            good.append(name)
        elif 4 <= grade <= 6:
            poor.append(name)
        elif 1 <= grade <= 3:
            fail.append(name)

    print("\nВідмінники: ", end="")
    if len(excell) == 0:
        print("немає")
    else:
        for name in excell:
            print(name, end=" ")
        print()

    print("Хорошисти: ", end="")
    if len(good) == 0:
        print("немає")
    else:
        for name in good:
            print(name, end=" ")
        print()

    print("Відстаючі: ", end="")
    if len(poor) == 0:
        print("немає")
    else:
        for name in poor:
            print(name, end=" ")
        print()

    print("Не здали: ", end="")
    if len(fail) == 0:
        print("немає")
    else:
        for name in fail:
            print(name, end=" ")
        print()

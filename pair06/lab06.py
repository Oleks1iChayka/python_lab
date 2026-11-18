import math
import random
import statistics
from datetime import date

def task1():
    print("--- Завдання 1 ---")
    radius = float(input("Введіть радіус круга: "))
    circle_area = math.pi * (radius ** 2)
    print(f"Площа круга: {round(circle_area, 2)}")
    
    catet1 = float(input("Введіть перший катет: "))
    catet2 = float(input("Введіть другий катет: "))
    hypotenuse = math.sqrt(catet1**2 + catet2**2)
    print(f"Гіпотенуза: {round(hypotenuse, 2)}")
    
    items = int(input("Введіть кількість предметів N: "))
    capacity = int(input("Введіть ємність упаковки K: "))
    packages = math.ceil(items / capacity)
    print(f"Потрібно упаковок: {packages}")
    print()

def task2():
    print("--- Завдання 2 ---")
    n = int(input("Введіть кількість оцінок N: "))
    if n <= 0:
        print("Кількість має бути додатним числом.")
        return
    
    grades = []
    for _ in range(n):
        grades.append(random.randint(1, 12))
        
    print(f"Оцінки: {grades}")
    print(f"Min: {min(grades)}")
    print(f"Max: {max(grades)}")
    print(f"Середнє: {round(statistics.mean(grades), 2)}")
    print(f"Медіана: {statistics.median(grades)}")
    
    high_grades = sum(1 for g in grades if 10 <= g <= 12)
    print(f"Оцінок 10-12: {high_grades}")
    print()

def task3():
    print("--- Завдання 3 ---")
    year = int(input("Введіть рік події: "))
    month = int(input("Введіть місяць події: "))
    day = int(input("Введіть день події: "))
    
    event_date = date(year, month, day)
    current_date = date.today()
    
    difference = event_date - current_date
    days_diff = difference.days
    
    if days_diff > 0:
        print(f"До події залишилося: {days_diff} днів")
    elif days_diff < 0:
        print(f"Після події минуло: {abs(days_diff)} днів")
    else:
        print("Подія відбувається сьогодні!")
    print()

if __name__ == "__main__":
    task1()
    task2()
    task3()
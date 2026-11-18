import math
import random
import statistics
from datetime import date, datetime
import tkinter as tk

a = 6
b = 8
hypotenuse = math.sqrt(a ** 2 + b ** 2)
radius = 5
circle_area = math.pi * radius ** 2
print("Гіпотенуза:", hypotenuse)
print("Площа круга:", round(circle_area, 2))

items = 25
capacity = 6
print("Повних упаковок:", math.floor(items / capacity))
print("Упаковок потрібно:", math.ceil(items / capacity))

numbers_list = []
for i in range(10):
    numbers_list.append(random.randint(1, 100))
print(numbers_list)

students = ["Anna", "Ivan", "Olha", "Maksym"]
selected = random.choice(students)
print("Обрано:", selected)

questions = [1, 2, 3, 4, 5]
random.shuffle(questions)
print("Новий порядок:", questions)

grades_ex = [10, 8, 12, 9, 11, 10]
print("Середнє:", statistics.mean(grades_ex))
print("Медіана:", statistics.median(grades_ex))

print("Дата:", date.today())
print("Дата і час:", datetime.now())

date1 = date(2026, 10, 1)
date2 = date(2026, 12, 31)
difference = date2 - date1
print("Днів:", difference.days)

def square(number):
    return number ** 2

def is_even(number):
    return number % 2 == 0

def average_util(numbers):
    return sum(numbers) / len(numbers)

sample_nums = [4, 8, 10, 12]
print(square(5))
print(is_even(8))
print(average_util(sample_nums))

print(math.sqrt(100))
from math import sqrt
print(sqrt(100))

grades_proj = []
for i in range(20):
    grades_proj.append(random.randint(1, 12))
print("Оцінки:", grades_proj)
print("Min:", min(grades_proj))
print("Max:", max(grades_proj))
print("Середнє:", round(statistics.mean(grades_proj), 2))
print("Медіана:", statistics.median(grades_proj))
high_count = 0
for grade in grades_proj:
    if grade >= 10:
        high_count += 1
print("Оцінок 10-12:", high_count)
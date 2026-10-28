# 1
print("--- Завдання 1 ---")
numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]

positive = []
negative = []
even = []
divisible_by_3 = []

for num in numbers:
    if num > 0:
        positive.append(num)
    if num < 0:
        negative.append(num)
    if num % 2 == 0:
        even.append(num)
    if num % 3 == 0:
        divisible_by_3.append(num)

min_val = min(numbers)
max_val = max(numbers)
total_sum = sum(numbers)
average = total_sum / len(numbers)

print(f"Додатні: {positive}")
print(f"Від'ємні: {negative}")
print(f"Парні: {even}")
print(f"Кратні 3: {divisible_by_3}")
print(f"Min: {min_val}; Max: {max_val}; Sum: {total_sum}; Average: {round(average, 2)}")
print()


# 2
print("--- Завдання 2 ---")
group1 = {'Anna', 'Ivan', 'Olha'}
group2 = {'Ivan', 'Maksym', 'Olha'}

common = group1 & group2
only_group1 = group1 - group2
only_group2 = group2 - group1
all_members = group1 | group2

print(f"Спільні: {', '.join(common)}")
print(f"Тільки group1: {', '.join(only_group1)}")
print(f"Тільки group2: {', '.join(only_group2)}")
print(f"Усі: {', '.join(all_members)}")
print()


# 3
print("--- Завдання 3 ---")
prices = {
    "bread": 38,
    "milk": 48,
    "cheese": 120,
    "tea": 75
}


prices["butter"] = 65
prices["bread"] = 40

search_item = "milk"
print(f"Ціна товару '{search_item}': {prices.get(search_item, 'Товар не знайдено')} грн")

# Виведення товарів у заданому ціновому діапазоні (наприклад, 40..100 грн)
min_price, max_price = 40, 100
print(f"Ціновий діапазон: {min_price}..{max_price} грн")
for product, price in prices.items():
    if min_price <= price <= max_price:
        print(f"{product} - {price} грн")
print()


# 4
print("--- Завдання 4 ---")
group_info = ('10-IT', '2026/2027')
print(f"Група та навчальний рік: {group_info[0]}-{group_info[1]}")

students = {
    "Anna": [10, 11, 12, 9, 10],
    "Ivan": [8, 9, 10, 11, 9]
}

def add_student(name, grades_list):
    if len(grades_list) == 5 and all(1 <= g <= 12 for g in grades_list):
        students[name] = grades_list
    else:
        print(f"Помилка: учень {name} має невірну кількість оцінок або вони поза діапазоном 1-12.")

best_name = ""
best_average = 0

print("Середній бал учнів:")
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{name} - {round(avg, 2)}")
    if avg > best_average:
        best_average = avg
        best_name = name

print(f"Найкращий результат: {best_name} - {round(best_average, 2)}")
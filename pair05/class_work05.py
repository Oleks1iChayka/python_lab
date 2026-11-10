#1
print("1")
def say_hello():
    print("Привіт, Python!")

say_hello()
print()


# 2
print("2")
def greet(name):
    print(f"Привіт, {name}!")

greet("Ivan")
print()


# 3
print("3")
def area_rectangle(a, b):
    return a * b

area = area_rectangle(7, 4)
print("Площа:", area)
print()


# 4
print("4")
def square_print(x):
    print(x * x)

def square_return(x):
    return x * x

square_print(5)
result = square_return(5)
print("Результат можна використати:", result + 10)
print()


#5
print("5")
def greet_default(name, message="Привіт"):
    print(f"{message}, {name}!")

greet_default("Anna")
greet_default("Ivan", "Добрий день")
print()


#6
print("6")
def student_info(name, group, grade):
    print(f"{name}: група {group}, оцінка {grade}")

student_info(grade=11, name="Anna", group="10-IT")
print()


# 7
print("")
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([7, 2, 15, 4, 9])
print("Min:", minimum)
print("Max:", maximum)
print()


# 8
print("8")
def is_valid_grade(grade):
    return 1 <= grade <= 12

test_grade = 10
if is_valid_grade(test_grade):
    print(f"Оцінка {test_grade}: Коректна оцінка")
else:
    print("Помилка")
print()


# 9. 
print("9")
def average(numbers):
    return sum(numbers) / len(numbers)

def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count

numbers = [4, -2, 8, 0, 5]
print("Середнє:", average(numbers))
print("Додатних:", count_positive(numbers))
print()


# 10
print("10")
def total_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(total_sum(5, 10))
print(total_sum(1, 2, 3, 4, 5))
print()


# 11.
print("11")
def area_rectangle_main(a, b):
    return a * b

def main_demo11():
    width = 5.0
    height = 4.0
    result = area_rectangle_main(width, height)
    print("Площа (main):", result)

main_demo11()
print()


# 12.
print("12")
def input_grades():
    return [10, 8, 12, 9, 11]

def average_val(grades):
    return sum(grades) / len(grades)

def best_grade(grades):
    return max(grades)

def print_report(grades):
    print("Оцінки:", grades)
    print("Середній бал:", round(average_val(grades), 2))
    print("Найкраща оцінка:", best_grade(grades))

def main_demo12():
    grades = input_grades()
    print_report(grades)

main_demo12()
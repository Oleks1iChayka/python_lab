import math
# Завдання 1

def area_circle(radius):
    return math.pi * (radius ** 2)

def area_rectangle(width, height):
    return width * height

def area_triangle(base, height):
    return 0.5 * base * height

def task1_main():
    print("--- Завдання 1 ---")
    print("Оберіть фігуру: 1 - круг, 2 - прямокутник, 3 - трикутник")
    choice = input("Введіть номер фігури (1/2/3): ")
    
    if choice == '1':
        r = float(input("Радіус: "))
        print(f"Площа круга: {round(area_circle(r), 2)}")
    elif choice == '2':
        w = float(input("Ширина: "))
        h = float(input("Висота: "))
        print(f"Площа прямокутника: {area_rectangle(w, h)}")
    elif choice == '3':
        b = float(input("Основа: "))
        h = float(input("Висота: "))
        print(f"Площа трикутника: {area_triangle(b, h)}")
    else:
        print("Невірний вибір.")
    print()



# Завдання 2

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def digit_sum(n):
    total = 0
    for digit in str(abs(n)):
        total += int(digit)
    return total

def task2_main():
    print("--- Завдання 2 ---")
    n = int(input("Введіть натуральне число N: "))
    
    prime_status = "так" if is_prime(n) else "ні"
    print(f"Просте число: {prime_status}")
    print(f"Дільники: {divisors(n)}")
    print(f"Сума цифр: {digit_sum(n)}")
    print()



# Завдання 3

def average_score(grades):
    return sum(grades) / len(grades) if grades else 0

def minimum_score(grades):
    return min(grades) if grades else 0

def maximum_score(grades):
    return max(grades) if grades else 0

def count_above(grades, value):
    count = 0
    for g in grades:
        if g > value:
            count += 1
    return count

def task3_main():
    print("--- Завдання 3 ---")
    grades = [10, 8, 12, 9, 11]
    threshold = 9
    
    print(f"Оцінки: {grades}")
    print(f"Поріг: {threshold}")
    print(f"Середній бал: {round(average_score(grades), 2)}")
    print(f"Мінімальна: {minimum_score(grades)}")
    print(f"Максимальна: {maximum_score(grades)}")
    print(f"Вище {threshold}: {count_above(grades, threshold)}")
    print()



# Завдання 4

def check_length(password):
    return len(password) >= 8

def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def check_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False

def check_lower(password):
    for char in password:
        if char.islower():
            return True
    return False

def check_special(password):
    for char in password:
        if not char.isalnum():
            return True
    return False

def validate_password(password):
    errors = []
    if not check_length(password):
        errors.append("мінімальна довжина менше 8 символів")
    if not check_digit(password):
        errors.append("немає жодної цифри")
    if not check_upper(password):
        errors.append("немає великої літери")
    if not check_lower(password):
        errors.append("немає малої літери")
    if not check_special(password):
        errors.append("немає спеціального символу")
        
    if len(errors) == 0:
        return True, []
    else:
        return False, errors

def task4_main():
    print("--- Завдання 4 ---")
    password = input("Введіть пароль: ")
    is_valid, errors = validate_password(password)
    
    if is_valid:
        print("Пароль надійний і відповідає всім вимогам.")
    else:
        print("Пароль не відповідає вимогам.")
        print(f"Не виконано: {', '.join(errors)}")
    print()



# Головна функція main() для керування програмою

def main():
    task1_main()
    task2_main()
    task3_main()
    task4_main()

if __name__ == "__main__":
    main()
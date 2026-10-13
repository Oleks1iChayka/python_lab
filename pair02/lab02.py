N = int(input("Введіть натуральне число N: "))

count = 0
total_sum = 0

for i in range(1, N + 1):
    if i % 3 == 0 or i % 5 == 0:
        count += 1
        total_sum += i

if count > 0:
    average = total_sum / count
else:
    average = 0

print(f"Кількість: {count}")
print(f"Сума: {total_sum}")
print(f"Середнє: {average:.2f}")

#2

N1 = int(input("Введіть натуральне число N: "))

if N1 == 0:
    print("Кількість цифр: 1")
    print("Сума цифр: 0")
    print("Найбільша цифра: 0")
    print("Найменша цифра: 0")
else:
    temp = N1
    count = 0
    total_sum = 0
    max_digit = 0
    min_digit = 9

    while temp > 0:
        digit = temp % 10
        count += 1
        total_sum += digit
        
        if digit > max_digit:
            max_digit = digit
        if digit < min_digit:
            min_digit = digit
            
        temp //= 10

    print(f"Кількість цифр: {count}")
    print(f"Сума цифр: {total_sum}")
    print(f"Найбільша цифра: {max_digit}")
    print(f"Найменша цифра: {min_digit}")

#3

N2 = int(input("Введіть натуральне число N: "))
result = []

for i in range(1, N2 + 1):
    # Числа від 1 до 9 за визначенням діляться на власні цифри
    if i < 10:
        result.append(str(i))
        continue
        
    temp = i
    is_valid = True
    has_zero = False
    

    while temp > 0:
        digit = temp % 10
        if digit == 0:
            has_zero = True
            break
        if i % digit != 0:
            is_valid = False
            break
        temp //= 10
        
    if not has_zero and is_valid:
        result.append(str(i))

print("Результат:", " ".join(result))

#4


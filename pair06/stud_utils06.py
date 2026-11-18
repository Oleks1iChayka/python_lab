import random
import statistics

def generate_grades(count):
    return [random.randint(1, 12) for _ in range(count)]

def average_grade(grades):
    return statistics.mean(grades) if grades else 0

def get_level(average):
    if 10 <= average <= 12:
        return "високий"
    elif 7 <= average < 10:
        return "достатній"
    elif 4 <= average < 7:
        return "середній"
    else:
        return "початковий"
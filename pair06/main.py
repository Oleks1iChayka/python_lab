import tkinter as tk
import stud_utils06

students = ["Anna", "Ivan", "Olha"]

def generate_report():
    value = count_entry.get().strip()
    if not value.isdecimal():
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Помилка: введіть ціле число від 1 до 20")
        return
    
    count = int(value)
    if count < 1 or count > 20:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Помилка: кількість має бути від 1 до 20")
        return
    
    report = ""
    print("--- Звіт у консолі ---")
    for student in students:
        grades = stud_utils06.generate_grades(count)
        avg = stud_utils06.average_grade(grades)
        level = stud_utils06.get_level(avg)
        
        line = f"{student}: {grades} → {round(avg, 2)} → {level}\n"
        report += line
        print(line.strip())
        
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, report)

window = tk.Tk()
window.title("Статистика учнів")
window.geometry("500x400")

tk.Label(window, text="Введіть кількість оцінок (1-20):").pack(pady=5)
count_entry = tk.Entry(window, width=20)
count_entry.pack(pady=5)

tk.Button(window, text="Сформувати звіт", command=generate_report).pack(pady=10)

result_text = tk.Text(window, width=55, height=15)
result_text.pack(pady=10)

window.mainloop()
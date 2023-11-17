import tkinter as tk
from datetime import date

root = tk.Tk()
root.geometry("350x350")
root.title("Age Calculator")

label_font = ("ariel", 12, "bold")
entry_font = ("ariel", 10)

name_label = tk.Label(root, text="Name:", font=label_font)
name_entry = tk.Entry(root, font=entry_font)

year_label = tk.Label(root, text="Year:", font=label_font)
year_entry = tk.Entry(root, font=entry_font)

month_label = tk.Label(root, text="Month:", font=label_font)
month_entry = tk.Entry(root, font=entry_font)

date_label = tk.Label(root, text="Date:", font=label_font)
date_entry = tk.Entry(root, font=entry_font)

def calculate_age():
    today = date.today()
    birth_date = date(int(year_entry.get()), int(month_entry.get()), int(date_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    result_label1.config(text = f"Hi {name_entry.get()}!", font=entry_font)
    result_label2.config(text = f"You are {age} years old", font=entry_font)

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age, font=entry_font, fg="white", bg="#21130d")

name_label.grid(row=0, column=0, padx=50, pady=5)
name_entry.grid(row=0, column=1)

year_label.grid(row=1, column=0, padx=50, pady=5)
year_entry.grid(row=1, column=1)

month_label.grid(row=2, column=0, padx=50, pady=5)
month_entry.grid(row=2, column=1)

date_label.grid(row=3, column=0, padx=50, pady=5)
date_entry.grid(row=3, column=1)

calculate_button.grid(row=4, column=1, pady=5)

result_label1 = tk.Label(root, text="")
result_label1.grid(row=5, column=1, pady=5)

result_label2 = tk.Label(root, text="")
result_label2.grid(row=6, column=1, pady=5)

root.mainloop()


# Age Calculator App

Welcome to the Age Calculator app! This simple Python application allows users to input their date of birth, and it magically calculates and displays their age. 🎉

## Getting Started

### Step 1: Import Libraries

To kick things off, we need to import two essential libraries into our code: `tkinter` for the graphical user interface and `datetime` for working with dates.

```python
import tkinter as tk
from datetime import date
```

### Step 2: Create the App Window

Let's set up a sleek window for our app and give it the catchy name of *Age Calculator*.

```python
root = tk.Tk()
root.geometry("350x350")
root.title("Age Calculator")
```
And also, variables for fonts of labels and entry
```python
label_font = ("ariel", 12, "bold")
entry_font = ("ariel", 10)
```

### Step 3: User Input Section

Now, we're going to create labels for the name, year, month, and date. Users will input their information into corresponding entry fields.

```python
name_label = tk.Label(root, text="Name:", font=label_font)
name_entry = tk.Entry(root, font=entry_font)

year_label = tk.Label(root, text="Year:", font=label_font)
year_entry = tk.Entry(root, font=entry_font)

month_label = tk.Label(root, text="Month:", font=label_font)
month_entry = tk.Entry(root, font=entry_font)

date_label = tk.Label(root, text="Date:", font=label_font)
date_entry = tk.Entry(root, font=entry_font)
```

### Step 4: Age Calculation Function

Time to crunch the numbers! We'll define a function, `calculate_age()`, to calculate the user's age by subtracting their birth date from today's date.

```python
def calculate_age():
    today = date.today()
    birth_date = date(int(year_entry.get()), int(month_entry.get()), int(date_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    result_label1.config(text = f"Hi {name_entry.get()}!", font=entry_font)
    result_label2.config(text = f"You are {age} years old", font=entry_font)
```

### Step 5: Submit Button

Create a button for users to submit their input values, linking it to the `calculate_age` function.

```python
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age, font=entry_font, fg="white", bg="#21130d")
```
### Step 6: Layout

Nothing, looks perfect untill it has a proper layout. So we create a layout for Lables, entry fields, button and the result label.

```python
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
```

### Step 7: Run the App

Lastly, let's run everything inside the window using the `mainloop()` method.

```python
root.mainloop()
```

And there you have it! Run this script, enter your details, and discover your age in a flash. Enjoy calculating! 🎂📆
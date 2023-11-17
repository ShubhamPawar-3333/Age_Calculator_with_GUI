# Age Calculator App

Welcome to the Age Calculator app! This simple Python application allows users to input their date of birth, and it magically calculates and displays their age. 🎉

## Getting Started

### Step 1: Import Libraries

To kick things off, we need to import two essential libraries into our code: `tkinter` for the graphical user interface and `datetime` for working with dates.

```python
import tkinter as tk
from datetime import datetime
```

### Step 2: Create the App Window

Let's set up a sleek window for our app and give it the catchy name of *Age Calculator*.

```python
root = tk.Tk()
root.title("Age Calculator")
```

### Step 3: User Input Section

Now, we're going to create labels for the name, year, month, and date. Users will input their information into corresponding entry fields.

```python
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

year_label = tk.Label(root, text="Year:")
year_entry = tk.Entry(root)

month_label = tk.Label(root, text="Month:")
month_entry = tk.Entry(root)

date_label = tk.Label(root, text="Date:")
date_entry = tk.Entry(root)
```

### Step 4: Age Calculation Function

Time to crunch the numbers! We'll define a function, `ageCalc()`, to calculate the user's age by subtracting their birth date from today's date.

```python
def ageCalc():
    today = date.today()
    birth_date = datetime(int(year_entry.get()), int(month_entry.get()), int(date_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    result_label.config(text=f"Your Age: {age} years")
```

### Step 5: Submit Button

Create a button for users to submit their input values, linking it to the `ageCalc` function.

```python
calculate_button = tk.Button(root, text="Calculate Age", command=ageCalc)
```

### Step 6: Run the App

Lastly, let's run everything inside the window using the `mainloop()` method.

```python
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

year_label.grid(row=1, column=0)
year_entry.grid(row=1, column=1)

month_label.grid(row=2, column=0)
month_entry.grid(row=2, column=1)

date_label.grid(row=3, column=0)
date_entry.grid(row=3, column=1)

calculate_button.grid(row=4, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
```

And there you have it! Run this script, enter your details, and discover your age in a flash. Enjoy calculating! 🎂📆
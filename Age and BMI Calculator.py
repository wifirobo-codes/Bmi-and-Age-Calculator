import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import time

def calculate():
    try:
        # Get values from input fields
        name = entry_name.get()
        age = int(entry_age.get())
        dob_text = entry_dob.get()
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        # Validation
        if age < 0:
            raise ValueError("Age must be non-negative")
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive")

        # Age logic
        dob = datetime.strptime(dob_text, "%Y-%m-%d")
        today = datetime.today()
        age_years = today.year - dob.year
        age_months = today.month - dob.month
        age_days = today.day - dob.day
        if age_days < 0:
            age_months -= 1
            age_days += 30
        if age_months < 0:
            age_years -= 1
            age_months += 12

        # BMI logic
        bmi = weight / ((height / 100) ** 2)
        
        # Classification
        if bmi < 18.5: status = "Underweight"
        elif bmi < 25: status = "Normal weight"
        elif bmi < 30: status = "Overweight"
        else: status = "Obese"

        # Show result
        result_text = (f"Name: {name}\n"
                       f"Age: {age_years} years, {age_months} months, {age_days} days\n"
                       f"BMI: {bmi:.2f} ({status})")
        messagebox.showinfo("Result", result_text)

        # Save data
        data = {
            "name": name, "age": age, "date_of_birth": dob_text,
            "height": height, "weight": weight,
            "bmi": round(bmi, 2), "timestamp": time.ctime()
        }
        with open(f"data_{int(time.time())}.json", "w") as f:
            json.dump(data, f, indent=2)

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Setup Window
root = tk.Tk()
root.title("Age & BMI Calculator")

# Labels and Entries
labels = ["Name", "Age", "DOB (YYYY-MM-DD)", "Height (cm)", "Weight (kg)"]
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_name, entry_age, entry_dob, entry_height, entry_weight = entries

# Button
tk.Button(root, text="Calculate & Save", command=calculate).grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()

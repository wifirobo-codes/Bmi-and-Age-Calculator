from datetime import datetime
import json
import time

print("Welcome to the Age and BMI Calculator!")
print("Please enter the following information:")
print("Note: Age must be a positive integer, and height and weight must be positive numbers.")
print("Let's get started!")

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    dob_text = input("Enter your date of birth (YYYY-MM-DD): ")
    height = float(input("Enter your height in centimeters: "))
    weight = float(input("Enter your weight in kilograms: "))

    if age < 0:
        raise ValueError("age must be non-negative")
    if height <= 0 or weight <= 0:
        raise ValueError("height and weight must be positive")

    print(name)

    # Age classification
    if age < 7:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    else:
        print("You are an adult.")

    # exact age in years, months, and days
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

    print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

    # BMI calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    print(f"Your BMI is: {bmi:.2f}")
    print("BMI Classification:")
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")

    print("Thank you for using the program!")
    print("Goodbye!")
    print("Have a nice day!")
    print("Stay healthy!")

    data = {
        "name": name,
        "age": age,
        "date_of_birth": dob.strftime('%Y-%m-%d'),
        "height": height,
        "weight": weight,
        "bmi": round(bmi, 2),
        "timestamp": time.ctime()
    }

    with open(f"age_bmi_data_{time.strftime('%Y-%m-%d_%H-%M-%S')}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
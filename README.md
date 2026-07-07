# Age and BMI Calculator

A small interactive Python script that calculates a user's exact age (years, months, days) from their date of birth and computes BMI (Body Mass Index) from height and weight. The script prints classifications (child/teenager/adult and BMI category), displays friendly messages, and writes the collected data plus BMI to a timestamped JSON file.

---

## Features

- Interactive CLI prompts for:
  - Name
  - Age (integer)
  - Date of birth (YYYY-MM-DD)
  - Height (centimeters)
  - Weight (kilograms)
- Calculates exact age in years, months, and days.
- Computes BMI and prints BMI classification:
  - Underweight
  - Normal weight
  - Overweight
  - Obese
- Saves input and results to a timestamped JSON file:
  - `age_bmi_data_YYYY-MM-DD_HH-MM-SS.json`

---

## Requirements

- Python 3.x (3.7+ recommended)
- No external packages required (uses only stdlib: `datetime`, `json`, `time`)

---

## Installation / Setup

1. Clone the repository (if not already done):
   git clone https://github.com/wifirobo-codes/Bmi-and-Age-Calculator.git

2. Change into the project directory:
   cd Bmi-and-Age-Calculator

3. Run the script with Python. Note: the filename contains spaces — use quotes or escape the space:
   python "Age and BMI Calculator.py"

---

## Usage

Run the script and follow the prompts:

Example:
$ python "Age and BMI Calculator.py"

Interactive prompts (example input shown after each prompt):
- Enter your name: Alice
- Enter your age: 33
- Enter your date of birth (YYYY-MM-DD): 1992-03-14
- Enter your height in centimeters: 170
- Enter your weight in kilograms: 65

Example output (approximate):
- You are an adult.
- You are 34 years, 3 months, and 24 days old.
- Your BMI is: 22.49
- BMI Classification:
  - Normal weight
- Thank you for using the program!
- JSON data saved to: age_bmi_data_2026-07-07_12-34-56.json

---

## JSON output

The program saves a JSON file with the following structure:

{
  "name": "Alice",
  "age": 33,
  "date_of_birth": "1992-03-14",
  "height": 170.0,
  "weight": 65.0,
  "bmi": 22.49,
  "timestamp": "Wed Jul  7 12:34:56 2026"
}

Filename format: `age_bmi_data_{YYYY-MM-DD_HH-MM-SS}.json`.

---

## BMI Classification (used by the script)

- Underweight: BMI < 18.5  
- Normal weight: 18.5 ≤ BMI < 25  
- Overweight: 25 ≤ BMI < 30  
- Obese: BMI ≥ 30

BMI is calculated as:
BMI = weight_kg / (height_m ** 2)  
(where height_m = height_cm / 100)

---

## Age calculation details and known limitation

- The script computes years, months, and days by subtracting the parsed date-of-birth from today's date and adjusting months/days when negative.
- Note: The script adds 30 days when day difference is negative (simple approximation). For perfect day counts you may want to use calendar-aware logic or 3rd-party libraries like `dateutil` to get exact day/month differences spanning varying month lengths.

---

## Validation & Error Handling

- Age must be a non-negative integer.
- Height and weight must be positive numbers.
- Date of birth must match `YYYY-MM-DD` format.
- The script prints an "Invalid input" message for ValueError and a general message for other exceptions.

---

## Running from Windows / macOS / Linux

- Use Python 3 and run:
  - Windows / macOS / Linux:
    python "Age and BMI Calculator.py"
- If your shell treats spaces specially, keep the filename in quotes or rename the file to remove spaces (recommended):
  - Rename:
    mv "Age and BMI Calculator.py" age_and_bmi_calculator.py
  - Run:
    python age_and_bmi_calculator.py

---

## Suggested improvements (optional)

- Validate that the entered numeric `age` matches the computed age from `date_of_birth` (or remove the `age` prompt and compute it exclusively from DOB).
- Use `calendar` or `dateutil.relativedelta` for precise months/days computation.
- Add command-line flags for non-interactive usage: `--name`, `--dob`, `--height`, `--weight` and a `--output` file option.
- Add unit tests for BMI and age calculation functions.
- Add a small README badge and a license file (e.g., MIT) if desired.

---

## Contributing

Contributions are welcome. Open an issue or a pull request. Suggested workflow:
1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Make changes, commit, and push
4. Open a pull request describing your change

---

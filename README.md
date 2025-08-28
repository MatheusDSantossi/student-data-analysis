# Student Data Analysis Project

This repository contains a personal project focused on exploring data analysis, data cleaning, and processing techniques using a dataset of student information.

## 📁 Repository Structure

```

.
├── .gitignore              # Ignores all .csv files except input.csv
├── checking\_format.py      # Script for checking data format and consistency
├── data\_cleaning.py        # Script for cleaning and preprocessing the data
├── input.csv               # Input dataset used for analysis (not ignored)
├── students\_sql\_code.sql   # SQL queries for working with the dataset
└── utils/                  # Utility functions used across scripts

````

## 📊 Project Goals

- Load and understand student data from `input.csv`
- Perform format validation and consistency checks (`checking_format.py`)
- Clean and preprocess the data (`data_cleaning.py`)
- Use SQL (`students_sql_code.sql`) for further exploration or database integration

## 🛠 Requirements

Make sure you have Python 3.7+ installed. To install common dependencies:

```bash
pip install pandas
````

(Additional dependencies may be added later.)

## 🚀 How to Run

1. Place your student data in `input.csv`.
2. Run the format checking script:

```bash
python checking_format.py
```

3. Run the cleaning script:

```bash
python data_cleaning.py
```

4. Explore or execute SQL queries from `students_sql_code.sql` using your preferred SQL tool.

## 📌 Notes

* All other `.csv` files are ignored by Git for cleanliness, except for `input.csv`.
* Utility functions are organized in the `utils/` folder to promote code reusability.

## 📄 License

This project is for personal and educational purposes. No license is currently applied.

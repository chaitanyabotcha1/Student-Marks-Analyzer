# Student Marks Analyzer

A Python project to analyze student marks from a CSV file, save the data to a SQLite database, and generate a report of average marks and top students per subject.

## Features

- Load student marks from a CSV file.
- Save data into a SQLite database.
- Calculate average marks for each subject.
- Find the highest and lowest marks.
- Identify the top student in each subject.
- Export a final report as a CSV file.

## Technologies Used

- Python 3.x
- Pandas
- SQLite3

## Project Structure
```
Student-Marks-Analyzer/
│
├── analyzer.py # Main script to run
├── data.csv # Sample student data
├── report.csv # Generated report
├── students.db # SQLite database
└── README.md # Project documentation
```


## How to Run

1. Make sure you have Python 3 installed.
2. Install required libraries (if not already):
pip install pandas
Run the analysis:
python analyzer.py
The report will be saved as report.csv.

Example Output:

Average marks per subject:
English: 80.67
Math: 84.75
Science: 92.00

Top students per subject:
English: Ravi (83)
Math: Lakshmi (90)
Science: Arjun (95)

✅ Steps to add this README:

1. Save this content as `README.md` in your project folder.  
2. In PowerShell, run:

```powershell
git add README.md
git commit -m "Add clean README for Student Marks Analyzer"
git push

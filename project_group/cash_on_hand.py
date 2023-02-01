import csv
from pathlib import Path

file_path = Path.cwd()/'project_group'/'summary_report.txt'
coh_csv = Path.cwd()/'project_group'/'csv_reports'/'cash-on-hand-usd.csv'

def cash_on_hand():
    if coh_csv.exists():
        with coh_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile:
            reader = csv.reader(csvfile)
            day = []
            coh = []
            next(reader)
            for row in reader:
                day.append(float(row[0]))
                coh.append(float(row[1]))
    count = 0
    for amount in range(len(coh) - 1):
        diff = coh[amount] - coh[amount + 1]
        if diff > 0:
            if file_path.exists():
                with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                  file.write(f'\n[CASH DEFICIT] DAY: {day[amount + 1]}, AMOUNT: USD{diff:.2f}')
            count += 1
    if count == 0:
            with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                file.write(f'\n[CASH SURPLUS] CASH ON HAND ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')  

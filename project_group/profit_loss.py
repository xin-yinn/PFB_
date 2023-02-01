import csv
from pathlib import Path

file_path = Path.cwd()/'project_group'/'summary_report.txt'
pl_csv = Path.cwd()/'project_group'/'csv_reports'/'profit-and-loss-usd.csv'

def profit_and_loss():
    if pl_csv.exists():
        with pl_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile:
            reader = csv.reader(csvfile)
            day = []
            netprofit = []
            next(reader)
            for row in reader:
                day.append(float(row[0]))
                netprofit.append(float(row[4]))
    count = 0
    for amount in range(len(netprofit) - 1):
        diff = netprofit[amount] - netprofit[amount + 1]
        if diff > 0:
            if file_path.exists():
                with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                  file.write(f'\n[PROFIT DEFICIT] DAY: {day[amount + 1]}, AMOUNT: USD{diff:.2f}')
            count += 1
    if count == 0:
            with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                file.write(f'\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')



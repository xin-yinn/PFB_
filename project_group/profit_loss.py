# import modules
import csv
from pathlib import Path

file_path = Path.cwd()/'project_group'/'summary_report.txt'
pl_csv = Path.cwd()/'project_group'/'csv_reports'/'profit-and-loss-usd.csv'

def profit_and_loss():
    """
    function computes the difference in net profit if net profit on current day is lower than previous day
    no parameters required
    """
    # check if file exists
    if pl_csv.exists():
        # if true, open file with mode 'r' to read
        with pl_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile:
            reader = csv.reader(csvfile)
            # use next to skip header row in csv file
            next(reader)
            # create 2 empty lists to nest 'day' and 'net profit'
            day = []
            netprofit = []
            # for loop to append 'day' and 'net profit' into their respective lists
            for row in reader:
                day.append(float(row[0]))
                netprofit.append(float(row[4]))
    # inititalise counter
    count = 0
    for amount in range(len(netprofit) - 1):
        # difference = net profit on current day - net profit on next day
        diff = netprofit[amount] - netprofit[amount + 1]
        # if difference more than 0, means that there is a profit deficit as current day net profit is higher than next day 
        if diff > 0:
            if file_path.exists():
                # open file with mode 'a' to append output into txt file
                with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                  file.write(f'\n[PROFIT DEFICIT] DAY: {day[amount + 1]}, AMOUNT: USD{diff:.2f}')
            count += 1
    if count == 0:
            # open file with mode 'a' to append output into txt file
            with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                file.write(f'\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

# import modules
import csv
from pathlib import Path

file_path = Path.cwd()/'project_group'/'summary_report.txt'
coh_csv = Path.cwd()/'project_group'/'csv_reports'/'cash-on-hand-usd.csv'

def cash_on_hand():
    """
    function computes the difference in cash-on-hand to see if there are any cash deficits or surplus
    no parameters required
    """
    # check if csv file exists
    if coh_csv.exists():
        # open file and use mode 'r' to read
        with coh_csv.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as csvfile:
            reader = csv.reader(csvfile)
            # use next to skip header row in csv file
            next(reader)

            #create 2 empty lists the nest data for 'day' and 'cash-on-hand'
            day = []
            coh = []
            # create for loop to loop function in every row of the csv file
            for row in reader:
                # append day and cash on hand into their respective lists
                day.append(float(row[0]))
                coh.append(float(row[1]))
    # initialise counter 
    count = 0
    for amount in range(len(coh) - 1):
        # difference = coh on current day - coh on next day
        diff = coh[amount] - coh[amount + 1]
        # if difference more than 0, means there is a cash deficit as current day is more than next day.
        if diff > 0:
            if file_path.exists():
                # open file and use mode 'a' to append output into txt file
                with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                  file.write(f'\n[CASH DEFICIT] DAY: {day[amount + 1]}, AMOUNT: USD{diff:.0f}')
            count += 1
    #if count remains 0, means that there are no cash deficits in any day, and there is cash surplus
    if count == 0:
            # open file and use mode 'a' to append output into txt file
            with file_path.open(mode = 'a', encoding = 'UTF-8', errors = 'ignore') as file:
                file.write(f'\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')                         

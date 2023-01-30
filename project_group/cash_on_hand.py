# importing built-in functions from python
import csv, re
from pathlib import Path

# creating function for cash on hand
def cash_on_hand():
    # reading of csv file extracted from game
    fp_read = Path.cwd()/"project_group"/"csv_reports"/"cash-on-hand-usd.csv"
    # creating variable to write to summary text file
    fp_write = Path.cwd()/"project_group"/"summary_report.txt"
    # creating empty lists
    coh_empty_list = []
    days_empty_list = []
    amt_empty_list = []
    diff_empty_list = []

    with fp_read.open(mode= "r", encoding= "UTF-8") as file:
        coh_reader = csv.reader(file)
        next(coh_reader)
        
        # creating for loop 
        for line in coh_reader:
            # appending to empty list
            coh_empty_list.append(line)
            # line[0] is the days column
            day = line[0]
            # line[1] is the cash on hand amount column
            amt = line[1]
            # appending to empty lists
            days_empty_list.append(int(day))
            amt_empty_list.append(amt)

            for items in range(len(amt_empty_list)):
                #create a string to minus the 2 numbers
                diff = float(amt_empty_list[items]) - float(amt_empty_list[items-1])
                #put the difference between the numbers into an empty list and append the list
                diff_empty_list.append(diff)

        with fp_write.open(mode= "a", encoding= "UTF-8", newline= "") as file:    
            #create for loop to create a zip for 2 appened list creates previousely as category
            for category in zip(days_empty_list, diff_empty_list):
                #using if funcion, if the catergory is less than 0,
                if category[1] <= 0:
                    #the file will print this
                    file.write("\n[CASH DEFICIT]" " "f"DAY: {category[0]}, AMOUNT: SGD{category[1]*-1}")
                else:
                    #else if the category is more than 0, it will print this
                    file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

# import modules
import csv
from pathlib import Path

#output to be written on a txt file
#Get data/input from the specific file: overheads.csv
fp_write = Path.cwd()/"project_group"/"summary_report.txt"
fp_read = Path.cwd()/"project_group"/"csv_reports"/"overheads.csv"

def overheads():
    """
    function finds the highest overhead category
    no parameters required
    """
    #Create 3 empty lists to nest data 
    overheads_empty_list = []
    oh_cat = []
    oh_usd = []
    
    # Open file and use mode 'r' to read
    with fp_read.open(mode= "r", encoding= "UTF-8") as file:
        oh_reader = csv.reader(file)
        # Use next to skip first header row in csv file
        next(oh_reader)
    
        for line in oh_reader:
            # append to empty list
            overheads_empty_list.append(line)
            # for loop to loop steps in each row of csv file
            for sublist in overheads_empty_list:
                # append sublist[0] which is the catergory column into oh_cat list
                oh_cat.append(sublist[0])
                # append sublist[1] which is overheads column into oh_usd list
                oh_usd.append(float(sublist[1]))
        
        # assign variable for max value
        max_value = max(oh_usd)
        # assign variable for max value category
        max_value_cat = oh_usd.index(max_value)
        # assign variable for category name
        category = oh_cat[max_value_cat]
        
    #Open file and use mode 'w' to write output into txt file
        with fp_write.open(mode= "w", encoding= "UTF-8", newline= "") as file:    
            file.write("[HIGHEST OVERHEADS] "f"{category.upper()}: {max_value}%")



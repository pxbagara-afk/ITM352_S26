# writes out a local “sales_data_test.csv” file from the first 
#  Use this file as you develop the dashboard for faster testing

#Code for importing pandas into file
from time import time

from numpy import number, shape
import pandas as pd

# Set pandas display options to show all data
#Used A.I since it was only showing frist two columns and last two columns without this





#Used A.I to organize a loop and logic statements (wrote codes and functions)
#Ask User to enter number of rows wanted to print out 
# Accepts specific inputs:
# A number to display that many rows.
# The word "all" to display all rows.
# An empty input to skip the preview.

display_initial_rows = df_sales
while True:
    user_input = input("Enter the number of initial rows to display (or 'all' to display all rows, or press Enter to skip): ").strip().lower()
    
    if user_input == "":
        print("Preview skipped.")
        break
    elif user_input == "all":
        print(display_initial_rows)
        break
    elif user_input.isdigit():
        num_rows = int(user_input)
        if num_rows > 0:
            print(display_initial_rows.head(num_rows))
            break
        else:
            print("Please enter a positive integer for the number of rows or 'all' for all rows.")
    else:
        print("Invalid input. Please enter a positive integer, 'all', or press Enter to skip.")

#Interacts with sales_data.csv file and prints first 10 rows of data
df_sales = pd.read_csv("sales_data.csv")
print(df_sales.head((int(user_input))))

#Indicates file being loaded and on succession will load time to load
#Prints the number of rows and list of columns of dataframe
#Used AI for organizing logic statements and accounting for handling error
#Used AI to calculate time taken to load the CSV file and print it in seconds with 2 decimal places

try:
    start_time = time()
    load_csv = pd.read_csv("sales_data.csv")

    if load_csv is not None:
        shape = df_sales.shape
        print(f"The sales data has {shape[0]} rows and {shape[1]} columns.")
        end_time = time()
        load_time = end_time - start_time
        print("CSV file loaded successfully.")
        print(f"Time taken to load the CSV file: {load_time:.2f} seconds.")
except FileNotFoundError:
    print("Error: sales_data.csv file not found.")

#Empty rows or missing data to be converted to 0
#Also warns user of any missing data and that it will be filled with 0
df_sales = df_sales.fillna(0)
print("Missing data has been filled with 0.")
    
#Prompts the user to specify how many initial rows of the DataFrame they would like to see.
# Accepts specific inputs:
# A number to display that many rows.
# The word "all" to display all rows.
# An empty input to skip the preview.
# Validates user input and handles invalid entries gracefully.



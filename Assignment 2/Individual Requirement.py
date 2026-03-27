#Combination of Ex3a and Ex4 with some edits to make it more organized such as adding a option to create custom pivot table
import pandas as pd
import sys
from time import time

# Requirement #9: Empty dictionary to store pivot table results for tracking
session_results = {}


# This is used to load the CSV file data, time calcualtion, printing the inforamtion of the CSV file, and cleaning out mssing data with 0
# Used AI to calculate time taken to load the CSV file and print it in seconds with 2 decimal places (prompt A.I with "Calculate time taken to load the CSV file and print it in seconds with 2 decimal places")
# Used A.I to organize a loop and logic statements (wrote codes and functions) (promtpt A.I with "Organize a loop and logic statements for loading the CSV file, calculating time, printing info, and cleaning missing data")
def sales_data():
    """Loads the CSV, tracks time, and handles initial data cleaning."""
    try:
        #Start the timer and read the file
        start_time = time()
        df_sales = pd.read_csv("sales_data.csv")

        # requirement 7: makes sure order_date is datetime - Updated for DD/MM/YYYY
        df_sales['order_date'] = pd.to_datetime(df_sales['order_date'], dayfirst=True, errors='coerce')

        #Calculate shape and timing
        current_shape = df_sales.shape
        end_time = time()
        load_time = end_time - start_time

        print(f"The sales data has {current_shape[0]} rows and {current_shape[1]} columns.")
        print("CSV file loaded successfully.")
        print(f"Time taken to load the CSV file: {load_time:.2f} seconds.")

        #Clean missing data
        # Change missing numbers to mean instead of 0
        numeric_cols = df_sales.select_dtypes(include=['number']).columns
        df_sales[numeric_cols] = df_sales[numeric_cols].fillna(df_sales[numeric_cols].mean())
        print("Missing data has been filled with the mean.")

        # Calculate sales column for pivot tables
        #Use A.I for calculating sales column by multiplying quantity and unit price (A.I prompt: How do I create a new column in pandas that multiplies two existing columns together?)
        df_sales['sales'] = df_sales['quantity'] * df_sales['unit_price']

        #Return the dataframe so main() can use it
        return df_sales
    #Accounts for errors when can't find CSV file
    except FileNotFoundError:
        print("Error: sales_data.csv file not found.")
        return None

# requirement 7: function to filter by date range
#Use A.I to create a function that filters the data frame by a user specified date range (A.I prompt: How do I create a function that filters a pandas data frame by a user specified date range?)
def filter_by_date_range(pivot_table):
    print("\nPlease select a date range to filter the data. Use proper date format (DD/MM/YYYY)")

    while True:
        try:
            start_date = input("Start date (DD/MM/YYYY): ").strip()
            end_date = input("End date (DD/MM/YYYY): ").strip()
            # Convert to datetime with exact date format - Updated for DD/MM/YYYY
            start = pd.to_datetime(start_date, format='%d/%m/%Y')
            end = pd.to_datetime(end_date, format='%d/%m/%Y')
            if start > end:
                print("Start date cannot be after end date. Try again.")
                continue
            filtered_df = pivot_table[(pivot_table['order_date'] >= start) & # filter data start and end date
                                      (pivot_table['order_date'] <= end)]
            if filtered_df.empty: # check if filtered data frame is empty
                print(" No data found in that date range. Try again.")
                continue
            print(f"Data filtered to {len(filtered_df)} rows between {start_date} and {end_date}.") # inform user of result
            return filtered_df
        except ValueError: # catch invalid date format
            print("Invalid date format. Please use DD/MM/YYYY.")

# requirement 1: function to handle Excel export (Applied globally to all analysis functions)
#Used A.I to make template of function to handle exporting any pivot table to Excel with user input for filename and error handling (A.I prompt: How do I create a function that handles exporting any pandas data frame to Excel with user input for filename and error handling?)
def ask_to_export(pivot_table):
    while True:
        #Ask question if you want to export
        export_choice = input("\nWould you like to export these results to an Excel file? (y/n): ").strip().lower()
        #If answer is y then it will ask user to name file and export as .xlsx
        if export_choice == 'y':
            filename = input("Enter a filename (without extension): ").strip() #asks user to input filename
            if not filename: 
                print("Invalid filename. Export cancelled.")
                return
            try:
                filename = f"{filename}.xlsx" # add .xlsx extension
                pivot_table.to_excel(filename, index=True)
                print(f"Results successfully exported to '{filename}':)") 
            except Exception as e: # catch any errors during export
                print(f"Error exporting to Excel: {e} :(")
            break
        elif export_choice == 'n': # If no then not export and break loop
            print("Okay, not exporting.")
            break
        else:
            print("Please enter 'y' or 'n'.") # invalid input, ask again

#Custom Pivot Builder Requirements

# These lists define what the user can choose from 
Row_Options = ['sales_region', 'product_category', 'employee_id']
Column_Options = ['order_type', 'customer_type']
Value_Options = ['quantity', 'unit_price', 'sales']
Agg_Options = ['sum', 'mean','count']

#  Prints a list and returns the string value of the user's numeric choice.
#Use A.I to create a function that prints a list of options and returns the string value of the user's numeric choice (A.I prompt: How do I create a function that prints a list of options and returns the string value of the user's numeric choice?)
#Also Used A.I for logical argument
def User_choice(options, label):
    print(f"\nSelect {label} ---")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        choice = input(f"Enter choice (1-{len(options)}): ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]
        print(f"Invalid input. Please enter a number between 1 and {len(options)}.")

#Dashboard Task Functions

#First function "Show the first n rows of sales data"
def show_rows(df_sales):
    #Ask user for number of rows to display, or "all" to display all rows, or Enter to skip
    """Prompts the user to view a specific number of rows."""
    while True:
        print("\nEnter rows to display ('all', a number, or Enter to skip): ")
        user_input = input("Your choice: ").strip().lower()
        
        if user_input == "":
            print("Preview skipped.")
            break
        elif user_input == "all":
            result = df_sales
            print(result)
            break
        elif user_input.isdigit():
            num_rows = int(user_input)
            if num_rows > 0:
                result = df_sales.head(num_rows)
                print(result)
                break
            else:
                #Accounts for 0 and negative numbers
                print("Please enter a number greater than 0.")
        else:
            print("Invalid input. Please enter a positive integer, 'all', or press Enter.")
    
    # Global Export Prompt
    if 'result' in locals():
        ask_to_export(result)

#Start of reorganized table for sales by region and order type
def total_sales_by_region_order_type(df_sales):
    # REQUIREMENT 7: Filtering applied here
    filtered_data = filter_by_date_range(df_sales)
    
    print("Total sales by region and order_type:")
    #reorgnizes data into sales by region and order type with total sales as summed values, also accounts for missing data with 0 and adds totals for rows and columns
    #used A.I to organize the pivot table code and logic statements (prompt A.I with "Organize the code and logic statements for a pivot table that shows total sales by region and order type, with totals for rows and columns, and handles missing data with 0")
    pivot = pd.pivot_table(
        filtered_data,
        index='sales_region',
        columns='order_type',
        values='sales',
        aggfunc='sum',
        fill_value=0,
        margins=True,
        margins_name='Total'
    )
    # Store result in dictionary
    session_results["Total Sales by Region/Type"] = pivot
    print(pivot)
    
    # Global Export Prompt
    ask_to_export(pivot)

#Created function to sum up average by region 
#Used A.I in order to calculate mean (A,I prompt: How do I calculate mean by a certain criteria like region and organize")
def avg_sales_by_region_state_type(df_sales):
    print("\nAverage sales by region and order_type, with region-state breakdown:")
    pivot = pd.pivot_table(
        df_sales,
        index=['sales_region', 'customer_state'],
        columns='order_type',
        values='sales',
        aggfunc='mean',
        fill_value=0
    )
    # Store result in dictionary
    session_results["Avg Sales Region/State/Type"] = pivot
    print(pivot)
    
    # Global Export Prompt
    ask_to_export(pivot)

#Same code as above but now by sales customer and changed mean to sum of sales. 
def sales_by_customer_order_by_state(df_sales):
    print("\nSales by customer_type + order_type by state:")
    pivot = pd.pivot_table(
        df_sales,
        index=['customer_state', 'customer_type', 'order_type'],
        values='sales',
        aggfunc='sum',
        fill_value=0
    )
    # Store result in dictionary
    session_results["Sales by Cust/Order/State"] = pivot
    print(pivot)
    
    # Global Export Prompt
    ask_to_export(pivot)

#Same code as above but for finding employee i.d that's unique by region
#Used A.I to create filter for unique employee i.d by region (A.I prompt: How do I create a pivot table that shows the number of unique employee i.d by region?)
def unique_employees_by_region(df_sales):
    print("\nNumber of unique employees by sales_region:")
    pivot = pd.pivot_table(
        df_sales,
        index='sales_region',
        values='employee_id',
        aggfunc='nunique' 
    )
    pivot.columns = ['Number of Employees']
    
    # Store result in dictionary
    session_results["Unique Employees by Region"] = pivot
    print(pivot)
    
    # Global Export Prompt
    ask_to_export(pivot)

# The interactive builder that prevents the 'No group keys' error.
def generate_custom_pivot_table(df_sales):
    """The interactive builder that prevents the 'No group keys' error."""
    print("\n=== Custom Pivot Table Builder ===")
    
    # 1. Select the Row (Index)
    row_selection = User_choice(Row_Options, "Row Grouping")
    
    # 2. Select the Column
    col_selection = User_choice(Column_Options, "Column Grouping")
    
    # 3. Select the Value
    val_selection = User_choice(Value_Options, "Value to Calculate")
    
    # 4. Select the (Agg) (Or what we are calculating: sum, mean, count)
    agg_selection = User_choice(Agg_Options, "Calculating type")

    try:
        # Create the table based on the 4 choices above
        #Template for pivot table customized by user 
        pivot = pd.pivot_table(
            df_sales, 
            index=row_selection, 
            columns=col_selection, 
            values=val_selection, 
            aggfunc=agg_selection,
            fill_value=0
        )
        
        # Determine a useful way to handle saving custom pivot tables created
        result_name = f"Custom: {agg_selection} of {val_selection} by {row_selection}/{col_selection}"
        session_results[result_name] = pivot

        #Prints the results of the pivot table with a header that shows what the user selected for the row, column, value,
        #Used A.I to organize the formatting of the results (A.I prompt: How do I format the output of a pivot table with a header that shows what the user selected for the row, column, value, and agg function?)
        print("\n" + "="*40)
        print(f"RESULT: {agg_selection.upper()} of {val_selection} by {row_selection}/{col_selection}")
        print("="*40)
        print(pivot)
        print("="*40)
        
        # Global Export Prompt
        ask_to_export(pivot)
        
    except Exception as e:
        print(f"\n[Error] Could not generate table: {e}")

# Requirement #10 Function to display all stored results from the dictionary
def view_stored_results(df_sales):
    """Displays all pivot tables stored in the session dictionary."""
    if not session_results:
        print("[No analytics stored yet.]")
    else:
        print("" + "X"*50)
        print("       STORED ANALYTICS HISTORY")
        print("X"*50)
        for name, table in session_results.items():
            print(f"Result Name: {name}")
            print("-" * len(name))
            print(table)
            # Global Export also available here
            ask_to_export(table)
        print("X"*50)

#Exit function for display screen
def exit_program(df_sales):
    print("Exiting the program. Goodbye!")
    sys.exit(0)

#This is the display menu that shows the options
#Is a list of tuples that has the name of the function and calls on that function if it is selected by the user.
def display_menu(df_sales):
    menu_options = (
        ("Show rows", show_rows),
        ("Total sales by region and order_type (WITH DATE FILTER)", total_sales_by_region_order_type),
        ("Average sales by region, state and order_type (", avg_sales_by_region_state_type),
        ("Sales by customer_type and order_type by state ", sales_by_customer_order_by_state),
        ("Unique employees by region", unique_employees_by_region),
        ("BUILD A CUSTOM PIVOT TABLE", generate_custom_pivot_table), # Integrated Custom Builder
        ("VIEW ALL STORED RESULTS", view_stored_results), # Requirement #9 display function
        ("Exit", exit_program),
    )

    #Start of display screen menu
    #Used A.I to make this dashboard menu set up with prompt (Make me a dashboard menu that has options to show the first n rows of sales data and exit, and make it so that I can easily add more functions to the menu by just adding to a tuple of tuples)
    while True:
        # Keep track of which analytics have been done and List them above the menu
        print("\n" + "-"*40) #clears space between menu loops
        print("ANALYTICS COMPLETED THIS SESSION:")
        if not session_results:
            print("  (None)")
        else:
            for key in session_results.keys():
                print(f"  - {key}")
        print("-" * 40)

        #Prints Sales Data Dashboard as tittle and also printes the menu options with numbers for user to select
        print("\n--- Sales Data Dashboard ---")
        for i, (label, _) in enumerate(menu_options, 1):
            print(f"{i}. {label}")
        
        choice = input("\nSelect an option: ").strip()
        #Excutes function based on the user's input (1-7) minus 1 to account for index starting at 0, and also accounts for invalid inputs and out of range number
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(menu_options):
                # This executes the function and passes the dataframe to it
                menu_options[idx][1](df_sales)
            else:
                print(f"Please select a number between 1 and {len(menu_options)}.")
        else:
            print("Invalid input. Please enter a number.")

#Loops through the display menu until user exits the program. 
def main():
    df_sales = sales_data()
    if df_sales is not None:
        display_menu(df_sales)

#Main loop 
if __name__ == '__main__':
    main()
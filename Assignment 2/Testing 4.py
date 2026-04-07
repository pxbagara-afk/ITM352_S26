import pandas as pd
from time import time

#Copy and Paste of Ex2-3 that gets data from CSV file added sales column for calculating
def custom_sale_data():
    try:
        df_sales = pd.read_csv("sales_data.csv")
        df_sales = df_sales.fillna(0)
        # Ensure sales column exists for calculations
        #Use A.I for calculating sales column by multiplying quantity and unit price (A.I prompt: How do I create a new column in pandas that multiplies two existing columns together?)
        df_sales['sales'] = df_sales['quantity'] * df_sales['unit_price']
        print(f"[Success] Loaded {df_sales.shape[0]} rows.")
        return df_sales
    except FileNotFoundError:
        print("Error: sales_data.csv not found.")
        return None

# These lists define what the user can choose from 
Row_Options = ['sales_region', 'product_category', 'employee_name']
Column_Options = ['order_type', 'customer_type', 'product_category', 'sales_region']
Value_Options = ['sales', 'quantity', 'unit_price']
Agg_Options = ['sum', 'mean', 'count', 'max', 'min']

#    "Prints a list and returns the string value of the user's numeric choice."
#Use A.I to create a function that prints a list of options and returns the string value of the user's numeric choice (A.I prompt: How do I create a function that prints a list of options and returns the string value of the user's numeric choice?)
#Also Used A.I for logical argument
def User_choice(options, label):
    print(f"Select {label} ---")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        choice = input(f"Enter choice (1-{len(options)}): ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]
        print(f"Invalid input. Please enter a number between 1 and {len(options)}.")

def generate_custom_pivot_table(df_sales):
    """The interactive builder that prevents the 'No group keys' error."""
    print("\n=== Custom Pivot Table Builder ===")
    
    # 1. Select the Row (Index)
    row_selection = User_choice(Row_Options, "Row Grouping")
    
    # 2. Select the Column
    col_selection = User_choice(Column_Options, "Column Grouping")
    
    # 3. Select the Value
    val_selection = User_choice(Value_Options, "Value to Calculate")
    
    # 4. Select the (Agg) (Or what we are calculating: sum, mean, count, max, min)
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
        #Prints the results of the pivot table with a header that shows what the user selected for the row, column, value,
        #Used A.I to organize the formatting of the results (A.I prompt: How do I format the output of a pivot table with a header that shows what the user selected for the row, column, value, and agg function?)
        print("\n" + "="*40)
        print(f"RESULT: {agg_selection.upper()} of {val_selection} by {row_selection}/{col_selection}")
        print("="*40)
        print(pivot)
        print("="*40)
    except Exception as e:
        print(f"\n[Error] Could not generate table: {e}")

#Copy and paste of display menu from Ex3a_NewFunctions with some edits to fit the new pivot table function and also added an exit program function.
#Might just take out so and add on to display menu in Ex3a_NewFunctions instead of having two separate display menus.
def display_menu(df_sales):
    """Main menu to trigger the customization process."""
    while True:
        print(" Main Menu")
        print("1. Build Custom Pivot Table")
        print("2. Exit")
        
        choice = input("\nSelection: ").strip()
        
        if choice == "1":
            generate_custom_pivot_table(df_sales)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Please enter 1 or 2.")

#Main loop
def main():
    df_sales = custom_sale_data()
    if df_sales is not None:
        display_menu(df_sales)

if __name__ == "__main__":
    main()
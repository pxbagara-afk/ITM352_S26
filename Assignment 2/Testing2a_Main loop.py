

import pandas as pd
from time import time
from numpy import number, shape


    # Indicates file being loaded and on succession will load time to load
    # Prints the number of rows and list of columns of dataframe
    # Used AI to calculate time taken to load the CSV file and print it in seconds with 2 decimal places
    # Used A.I to organize a loop and logic statements (wrote codes and functions)
        start_time = time()
        df_sales = pd.read_csv("sales_data.csv")

        if df_sales is not None:
            # Calculate shape and timing immediately
            current_shape = df_sales.shape
            end_time = time()
            load_time = end_time - start_time
            
            print(f"The sales data has {current_shape[0]} rows and {current_shape[1]} columns.")
            print("CSV file loaded successfully.")
            print(f"Time taken to load the CSV file: {load_time:.2f} seconds.")

            # Empty rows or missing data to be converted to 0
            # Also warns user of any missing data and that it will be filled with 0
            df_sales = df_sales.fillna(0)
            print("Missing data has been filled with 0.")

            # Prompts the user to specify how many initial rows of the DataFrame they would like to see.
            # Accepts specific inputs: A number, "all", or Enter to skip.
            while True:
                user_input = input("\nEnter the number of initial rows to display (or 'all' to display all rows, or press Enter to skip): ").strip().lower()
                
                if user_input == "":
                    print("Preview skipped.")
                    break
                elif user_input == "all":
                    print(df_sales)
                    break
                elif user_input.isdigit():
                    num_rows = int(user_input)
                    if num_rows > 0:
                        # Interacts with sales_data.csv file and prints specified rows
                        print(df_sales.head(num_rows))
                        break
                    else:
                        print("Please enter a positive integer for the number of rows or 'all' for all rows.")
                else:
                    print("Invalid input. Please enter a positive integer, 'all', or press Enter to skip.")

    except FileNotFoundError:
        print("Error: sales_data.csv file not found.")

# Main loop execution
if __name__ == "__main__":
    main()
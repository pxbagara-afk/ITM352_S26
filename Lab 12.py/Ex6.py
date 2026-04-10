# Get a page of mortgage rate info from the Hawaii State Data Center and print the data

import urllib.request
import ssl
from bs4 import BeautifulSoup
import pandas as pd

# Create an SSL context that doesn't verify certificates
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"


# Open URL and looks at HTML content
html = urllib.request.urlopen(urllib.request.request, context=ssl_context)
html_to_parse = BeautifulSoup(html, "html.parser")

# Find and print just the mortgage rate rows found in <table> tags
mortgage_rate = html_to_parse.find("table")

list_of_rows = mortgage_rate.find("tbody").find_all("tr")

mortgage_data = []
current_lender = ""
for row in list_of_rows:
    # Extract each table cell's text from the row.
    cells = [cell.get_text(" ", strip=True) for cell in row.find_all("td")]
    

    # Print each row as a single pipe-separated string.
    print(" | ".join(cells))

# Print the total number of rows parsed.
print("Total rows found:", len(mortgage_data))

#organize the data ito rows and columns (Lender	Term/Type, Interest Rate,% Points,% *APR)


# Display all columns and rowws
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

mortgage_df = pd.DataFrame(mortgage_data, columns=["Lender", "Term/Type", "Interest Rate", "% Points", "% *APR"])
print("\nMortgage Rates DataFrame:")
print(mortgage_df)
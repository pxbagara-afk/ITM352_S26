#Grab 1 month interest rate data from the treasury website
import urllib.request
import ssl
import pandas as pd
import lxml

url="https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603" 

ssl._create_default_https_context = ssl._create_unverified_context

print("Opening URL:", url)
web_page = urllib.request.urlopen(url)
data_frame = pd.read_html(web_page, header=0)[0]  # Read the first table from the webpages

print(data_frame.head())
print(data_frame.info())

one_month_rate=data_frame[0].loc[0,"<1 Mo>"]  # Get the 1 month interest rate from the first row
print("1 Month interest rate on 2026-03-01:", one_month_rate)


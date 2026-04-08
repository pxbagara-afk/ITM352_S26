import urllib.request
import ssl

# Disable SSL verification for this example
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"
web_page = urllib.request.urlopen(url)

print("Opening URL:", url)
web_page = urllib.request.urlopen(url)


for line in web_page:
    line = line.decode("utf-8")
    if "title" in line:
        print(line.strip())
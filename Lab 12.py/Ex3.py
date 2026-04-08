#parse the ITM department website to find the people(Faculty, grads, lecturers)
import urllib.request
import ssl
from bs4 import BeautifulSoup

# Disable SSL verification for this example
ssl._create_default_https_context = ssl._create_unverified_context

# Open the URL for the ITM department people
url = "https://shidler.hawaii.edu/itm/people"
web_page = urllib.request.urlopen(url)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(web_page, 'html.parser')

print("=" * 60)
print("BeautifulSoup Object Information:")
print("=" * 60)
print(f"Type of object returned: {type(soup)}")
print("\nFirst 500 characters of prettified HTML:")
print("-" * 60)
prettified = soup.prettify()
print('\n'.join(prettified.split('\n')[:20]))  # First 20 lines

print("\n" + "=" * 60)
print("Extracting ITM People Information:")
print("=" * 60)

# Find all person entries - look for common HTML structures
# This may vary depending on the website structure
people = []

# Try to find people by looking for common patterns
# Check for div classes, article tags, or list items with person info
person_divs = soup.find_all('div', class_=lambda x: x and 'person' in x.lower())
if not person_divs:
    person_divs = soup.find_all('article')
if not person_divs:
    person_divs = soup.find_all('li')

# Extract names and other info
for person_elem in person_divs:
    # Try to extract name - look for common patterns
    name = None
    title = None
    
    # Try different selectors for name
    name_elem = person_elem.find('h2') or person_elem.find('h3') or person_elem.find('a')
    if name_elem:
        name = name_elem.get_text(strip=True)
    
    # Try different selectors for title
    title_elem = person_elem.find('p') or person_elem.find('span', class_=lambda x: x and 'title' in x.lower())
    if title_elem:
        title = title_elem.get_text(strip=True)
    
    if name:
        people.append({'name': name, 'title': title})

# Print results
print(f"\nNumber of people found: {len(people)}")
print("\nPeople List:")
print("-" * 60)
for i, person in enumerate(people, 1):
    print(f"{i}. {person['name']}")
    if person['title']:
        print(f"   Title: {person['title']}")
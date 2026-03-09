# Que-1. Write Python scripts for basic file operations and data processing?
**Script**

***Basic File Operations:*

- Use Python's built-in open() function and the with statement to ensure files are properly closed. The primary modes are 'r' (read), 'w' (write, overwrites existing file), and 'a' (append, adds to the end). To delete or rename files, you need the os module.

#### Writing to a file ('w' mode):
```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")
```
#### Reading from a file ('r' mode):
```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# Output:
# Hello, World!
# This is a new line.
```
#### Appending to a file ('a' mode):
```python
with open('example.txt', 'a') as file:
    file.write("\nAppending this line to the file.")
```
#### Deleting a file:
```python
import os
if os.path.exists('example.txt'):
    os.remove('example.txt')
    print("File deleted.")
else:
    print("File does not exist.")
```
 
### Data Processing with Pandas 
- The pandas library is a powerful tool for data manipulation and analysis. First, you need to install it:
``` pip install pandas. ```

#### Loading and displaying data:
```python
import pandas as pd

# Create a simple DataFrame from a dictionary
data = {'city': ['London', 'Manchester'], 'population': [9787426, 2553379]}
df = pd.DataFrame(data)

# Load a CSV file into a DataFrame
# df = pd.read_csv('data.csv')

# Print the first 5 rows
print(df.head())
```
#### Filtering and grouping data:
```python
# Filter data where population is greater than 5 million
large_cities = df[df['population'] > 5000000]
print(large_cities)

# Group data by city and calculate the mean population (example for larger datasets)
# grouped_data = df.groupby('city').agg({'population': 'mean'})
```
---
# Que-2. Develop a simple web scraper to extract data from a website?
**Script**
- To create a web scraper, you'll use the Requests library to fetch the HTML content of a page and Beautiful Soup to parse it. Install them using pip: 

```pip install requests beautifulsoup4. ```

The example below scrapes the job titles and company names from a public sandbox website

```python
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

# Send a GET request to the URL
page = requests.get(URL)

# Parse the HTML content
soup = BeautifulSoup(page.content, "html.parser")

# Find the container that holds all the job postings
results = soup.find(id="ResultsContainer")

# Find all job cards within the results container
job_cards = results.find_all("div", class_="card-content")

# Extract and print job details
for job_card in job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")

    if title_element and company_element and location_element:
        print(f"Title: {title_element.text.strip()}")
        print(f"Company: {company_element.text.strip()}")
        print(f"Location: {location_element.text.strip()}")
        print("-" * 20)
```
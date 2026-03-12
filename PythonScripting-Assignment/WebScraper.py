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
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all links from the page
for link in soup.find_all("a"):
    print(link.get("href"))
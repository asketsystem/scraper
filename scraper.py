from turtle import title
from urllib import response
import requests 
from bs4 import BeautifulSoup
import random

response = requests.get(
    url="https://en.wikipedia.org/wiki/web_craping",
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.content)

# Get all the links
allLinks = soup.find(id="bodyContent").find_all("a")
random.shuffle(allLinks)
linkToScrape = 0

for link in allLinks:
    # We are only interested in other wiki articles 
    if link['href'].find("/wiki/") == -1:
        continue

    # Use this link to scrape
    linkToScrape = link
    break

print(linkToScrape)

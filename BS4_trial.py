import requests
from bs4 import BeautifulSoup

URL = "https://www.linkedin.com/search/results/people/?keywords=software%20engineer%20microsoft&origin=FACETED_SEARCH&title=Software%20Engineer&company=Microsoft&"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("li", class_="search-result")

for result in results:
    name = result.find("span", class_="name actor-name").text.strip()
    headline = result.find("p", class_="subline-level-1 Sans-14px-black-85% search-result__truncate").text.strip()
    location = result.find("p", class_="subline-level-2 Sans-14px-black-55% search-result__truncate").text.strip()
    print(name, headline, location)

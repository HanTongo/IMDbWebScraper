from requests import get
from bs4 import BeautifulSoup



# Grabs at least something from the site.
url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2003-01-01,2003-12-31'
# Headers used as IMDB doesn't allow the get() without a user agent. 
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
# Implemented the headers to grab url items.
response = get(url, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')
# Identifies the 50 entries on the page, 
movie_containers = html_soup.find_all("li", class_="ipc-metadata-list-summary-item")
first_movie = movie_containers[0]
print(first_movie.h3.text[3:])
first_year = first_movie.find("span", class_="sc-b189961a-8 kLaxqf dli-title-metadata-item")
print(first_year.text)

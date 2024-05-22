from requests import get
from bs4 import BeautifulSoup



# Grabs at least something from the site.
url = 'https://www.imdb.com/search/title/?release_date=2003-01-01,2004-01-31'
# Headers used as IMDB doesn't allow the get() without a user agent. 
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
# Implemented the headers to grab url items.
response = get(url, headers=headers)
# print(response.content.decode())




print(response.text[:1000])
# html_soup = BeautifulSoup(response.text, 'html.parser')
# type(html_soup)
# movie_containers = html_soup.find_all("div", class_="ipc-metadata-list-summary-item")
# print(type(movie_containers))
# print(len(movie_containers))

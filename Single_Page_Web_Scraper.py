from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint

# Lists to store the scraped data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Grabs at least something from the site.
url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2003&sort=boxoffice_gross_us,desc'

# Headers used as IMDB doesn't allow the get() without a user agent. 
# Turns and keeps movie titles in English
headers = {"Accept-Language": "en-US, en;q=0.5",
           "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

# Implemented the headers to grab url items.
response = get(url, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')

# Identifies the 50 entries on the page, 
movie_containers = html_soup.find_all("li", class_="ipc-metadata-list-summary-item")

# Extract data from individual movie container 
for container in movie_containers:
    # If the movie has a Metascore, then extract:
    if container.find("span", class_="metacritic-score-label") is not None:
        
        # Movie Title 
        name = container.h3.text[3:]
        names.append(name)

        # Movie Year Release
        year = container.find("span", class_="sc-b189961a-8 kLaxqf dli-title-metadata-item")
        years.append(int(year.text))

        # Movie's IMDB rating
        rating_retrieval = container.find("span", class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")
        imdb_rating = float(rating_retrieval.text[:3])
        imdb_ratings.append(imdb_rating)
        
        # Movie's Metascore
        metascore = float(container.find("span", class_="sc-b0901df4-0 bcQdDJ metacritic-score-box").text)
        metascores.append(metascore)

        # Number of IMBb votes
        vote_retrieval = container.find("span", class_="ipc-rating-star--voteCount")
        vote = (vote_retrieval.text[2:-1])
        votes.append(vote)

# Sets up dataframe to present data
page_data_df = pd.DataFrame({"Movie": names,
                        "Year Released": years,
                        "IMDb": imdb_ratings,
                        "Metascore": metascores,
                        "Votes": votes
                        })

print(page_data_df)
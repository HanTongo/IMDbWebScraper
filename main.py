import time
from time import sleep
from random import randint
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import warnings

# Lists to store the scraped data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Preparing the url parameter to retrieve film data
years_url = [str(i) for i in range(1940,2024)]

# Headers used as IMDB doesn't allow the get() without a user agent. 
# Turns and keeps movie titles in English
headers = {"Accept-Language": "en-US, en;q=0.5",
           "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

timestart_time = time.time() 
requests = 0 

for years_url in years_url:

    # Makes a request to IMDb for a particular year of films
    response = get("https://www.imdb.com/search/title/?title_type=feature&release_date=" + years_url + "&sort=boxoffice_gross_us,desc", headers=headers)
    sleep(randint(5,8)) 
    requests += 1 
    elapsed_time = time.time() - timestart_time 
    print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))

    # Warnings if unable to request from IMDb. 
    if response.status_code != 200:
        warnings.warn("Request: {}; Status code: {}".format(requests, response.status_code))

    # Prevents endless requests
    if requests > 84:
        warnings.warn("Number of requests was greater than expected.")

    # Allows the parsing of the IMDb page
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
movie_ratings = pd.DataFrame({"Movie": names,
                             "Year Released": years,
                             "IMDb": imdb_ratings,
                             "Metascore": metascores,
                             "Votes": votes
                             })

# Normalises the IMDb score so that it can be on the same scale as Metascore
movie_ratings['n_IMDb'] = movie_ratings['IMDb'] * 10

# Reorder the columns
movie_ratings = movie_ratings[['Movie', 'Year Released', 'IMDb', "n_IMDb", 'Metascore', 'Votes']]

# Output the results to a csv
movie_ratings.to_csv("movie_ratings.csv")
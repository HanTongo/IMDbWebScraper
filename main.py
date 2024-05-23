from requests import get
from bs4 import BeautifulSoup

# Lists to store the scraped data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Grabs at least something from the site.
url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2003-01-01,2003-12-31'
# Headers used as IMDB doesn't allow the get() without a user agent. 
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
# Implemented the headers to grab url items.
response = get(url, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')

# Identifies the 50 entries on the page, 
movie_containers = html_soup.find_all("li", class_="ipc-metadata-list-summary-item")

# Extract data from individual movie container 
for container in movie_containers:
    # If the movie has a Metascore, then extract:
    if container.find("span", class_="metacritic-score-label") is not None:
        # The name 
        name = container.h3.text[3:]
        names.append(name)

        # The year 
        year = container.find("span", class_="sc-b189961a-8 kLaxqf dli-title-metadata-item")
        years.append(year)

        # The IMDB rating
        
        rating_retrieval = container.find("span", class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")
        first_imdb = float(rating_retrieval.text[:3])
        print(first_imdb)
        
        # The Metascore
        first_meta = float(first_movie.find("span", class_="sc-b0901df4-0 bcQdDJ metacritic-score-box").text)
        print(f"Metascore: {first_meta}")

        # Retrieves IMBb votes
        first_vote = first_movie.find("span", class_="ipc-rating-star--voteCount")
        print(first_vote.text[2:-1])


# Retrieves movie's IMDb rating


# Retrieves the meta score




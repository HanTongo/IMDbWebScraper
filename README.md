Multipage IMDb Web Scraper (inspired by Dataquest)
--------------------------------------------------

In this project, I retrieved data on the top grossing films from 1940 to 2023 listed on the [IMDb](https://www.imdb.com/) website.
On the IMDb website, users can find information about films, television shows, film cast and crew, awards, and IMDb's recommendations.
Users then can research on many aspects of media, such as release date, rating, Metascore, IMDb's rating, votes, box office numbers, and much more.

I wanted to start applying and finding out techniques on how to start retrieving data from websites - utilising requests to make HTTP requests and access data from the website, and using BeautifulSoup to parse and extract HTML and XML documents.

Additionally with the data collected, I can plot and analyse the data using matplotlib, which then insights can be found. 

Installation
------------

### Prerequisites

Make sure Python is installed. You can download it from [python.org](https://www.python.org/downloads/).

### Install the requirements

* Install the requirements using `pip install -r requirements.txt`.
  * Create a virtual environment (optional)
  
#### Download and run data-retrieval program

* Clone this repo to your computer.
* Navigate to the project directory.
* Run `python main.py`

#### Analyse the data

* After running `python main.py`, a **movie_ratings.csv** should be created.
* Run `python analyse.py` to display the distribution of IMDb and Metascore ratings. 

Patterns and Insights
--------------------

#### Initial Analysis - IMDb rating, Metascore and both compared

!["IMDb and Metascore Rating, and both compared"](assets/Figure_1.png)
Distribution of IMDb rating and Metascore rating, for the top grossing films from 1940 to 2023. 




Extending this
--------------

Any feedback and comments are greatly welcome!
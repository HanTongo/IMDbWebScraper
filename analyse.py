import matplotlib.pyplot as plt
import pandas as pd

# Import movie ratings data
movie_ratings = pd.read_csv("movie_ratings.csv")

# Prepare 3 subplots
fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,4))
ax1, ax2, ax3 = fig.axes

# Plot 1 consists of a histogram of the IMDb ratings
ax1.hist(movie_ratings["IMDb"], bins = 10, range = (0,10))
ax1.set_title("a) IMDb Rating Distribution")

# Plot 2 consists of a histogram of the Metascore ratings
ax2.hist(movie_ratings["Metascore"], bins = 10, range = (0,100))
ax2.set_title("b) Metascore Distribution")

# Plot 3 consists of two histograms comparing IMDb and Metascore ratings
ax3.hist(movie_ratings["n_IMDb"], bins = 10, range = (0,100), histtype = "step")
ax3.hist(movie_ratings["Metascore"], bins = 10, range = (0,100), histtype = "step")
ax3.legend(["IMDb", "Metascore"], loc = "upper left")
ax3.set_title("c) The Two Normalised Distributions")

# Removes the top and right sides of the plot borders
for ax in fig.axes:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# Displays the three plots
plt.show()
# TODO 2: import requests and bs4
from bs4 import BeautifulSoup
import requests

# TODO 1: Look in to the given website
website = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# TODO 3: make content file from the given website and make the soup
# Retrieving the html code from website by using requests module
content = requests.get(url=website)
html_code = content.text

# Making Soup
soup = BeautifulSoup(html_code, "html.parser")


# TODO 4: look in to website to find out 100 movies name in website and find classes and code line in html
# Our data is lay in h3 tag which have clas="title"
# TODO 5: Extract the movies name in the list

movie_names = soup.find_all(name="h3", class_="title")

# making the list of 100 movies by getting text of the html code
movie_list = []
for name in movie_names:
    movie = name.getText()
    movie_list.append(movie)
# Or you can use list comprehension
# movie_list= [name.getText() for name in movie_names]

# TODO 6: Reorder the movies name from 1 to 100 rank as is from 100 to 1 rank
movie_list.reverse()  # it will mutate the actual list from 100 to 1 ranking to 1 to 100 movie ranking
# movie_list[::-1]   # We can also use this method [start: stop : step]

# TODO 7: make the movies.txt file

with open(file="movies.txt", mode="x", encoding="utf-8") as file:
    for name in movie_list:
        file.write(f"{name}\n")




from bs4 import BeautifulSoup
import os
import requests

DIR = os.getcwd() + "/Day 45 - Beautiful Soup"
os.chdir(DIR)

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_content = response.text

soup = BeautifulSoup(web_content, "html.parser")
#print(soup)

movies = soup.find_all(name="h3", class_="title")

all_movies = [movie.getText() for movie in movies]
movies_title = all_movies[::-1]

with open("movies.txt", mode="w", encoding='utf-8') as file:
    for movie_title in movies_title:
        file.write(f"{movie_title}\n")
        #rint(movie_title)
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.empireonline.com/movies/features/best-movies-2")
soup = BeautifulSoup(req.text, "html.parser")
p = soup.select("p a")
list_of_movies = []
for a in p:
    if "Read Empire's" in a.text:
        list_of_movies.append((a.text).replace("Read Empire's review of ", ""))
list_of_movies = list_of_movies[::-1]
with open(r"movies.txt", mode="w") as movies:
    for i in range(1,len(list_of_movies)+1):
        movies.write(f"{i}. {list_of_movies[i-1]}\n")

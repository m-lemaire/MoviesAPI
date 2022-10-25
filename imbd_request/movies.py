import requests
from requests.models import get_auth_from_url


class Movies:

    def Get_Movie_Reviews(title):
        url = "https://imdb-api.com/en/API"
        api_key = "k_68iqudb6"

        search_movie = requests.get(url+"/SearchMovie/"+api_key+"/"+title)
        print(search_movie.json())
        id = search_movie.json()["results"][0]["id"]
        reviews = requests.get(url+"/Reviews/"+api_key+"/"+id)
        return reviews


class Movie:
    
    def __init__(self,title) -> None:
        self.title = title

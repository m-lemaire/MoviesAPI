import requests
from requests.models import get_auth_from_url


class Movies:

    def Get_Movie_Reviews(title):
        url = "https://imdb-api.com/en/API/"
        api_key = "k_68iqudb6"
        
        SearchMovie = requests.get(url+"/SearchMovie/"+api_key+"/"+title)
        id = SearchMovie.json()["results"][0]["id"]
        Reviews = requests.get(url+"/Reviews/"+api_key+"/"+id)
        return Reviews

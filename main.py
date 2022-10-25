import requests

# response =  requests.get("https://imdb-api.com/en/API/Top250Movies/k_68iqudb6")



title = "The Shawshank Redemption"



response2 = requests.get("https://imdb-api.com/en/API/SearchMovie/k_68iqudb6/"+title)



id = response2.json()["results"][0]["id"]


response3 = requests.get("https://imdb-api.com/en/API/Reviews/k_68iqudb6/"+id)

print(response3.json())

import requests

response =  requests.get("https://imdb-api.com/en/API/Top250Movies/k_68iqudb6")

print(response.json())

title = "The Shawshank Redemption"

id = "tt0111161"

response = requests.get()
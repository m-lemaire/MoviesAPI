from imbd_request.movies import Movies


title = "The Shawshank Redemption"

Result_request = Movies.Get_Movie_Reviews(title)

print(Result_request.json())


from imbd_request.movies import Movies, Movie


title = "The Shawshank Redemption"
movie = Movie(title)
print(movie.title)

Result_request = Movies.Get_Movie_Reviews(title)

# print(Result_request.json())


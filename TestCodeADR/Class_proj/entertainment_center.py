import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w")

#print(toy_story.storyline)
#print(toy_story)

avatar = media.Movie("Avatar",
                        "US marine and blue aliens",
                        "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=teyhlo_cDGo")

#print(avatar.storyline)
#avatar.show_trailer()

xXx = media.Movie("xXx",
                  "Xander Cage is a secret agent",
                  "https://en.wikipedia.org/wiki/XXX_(2002_film)#/media/File:Xxx_movie.jpg",
                  "https://www.youtube.com/watch?v=afxTROGnvkw")

#xXx.show_trailer()

toy_story2 = media.Movie("Toy Story2",
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
                        "https://www.youtube.com/watch?v=azyK_k52R1w")

#print(toy_story.storyline)
#print(toy_story)

avatar2 = media.Movie("Avatar2",
                        "US marine and blue aliens - in the future",
                        "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=teyhlo_cDGo")

#print(avatar.storyline)
#avatar.show_trailer()

xXx2 = media.Movie("xXx2",
                  "Xander Cage is a black secret agent",
                  "https://en.wikipedia.org/wiki/XXX_(2002_film)#/media/File:Xxx_movie.jpg",
                  "https://www.youtube.com/watch?v=afxTROGnvkw")

#xXx.show_trailer()

#xXx2.show_trailer2()

movies = [toy_story, avatar, xXx, toy_story2, avatar2, xXx2] 

#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
#print(media.Movie.VALID_RATINGS)



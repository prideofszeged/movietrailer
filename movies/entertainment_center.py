import media
import fresh_tomatoes

# Create Move objects:
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

big_lebowski = media.Movie("The Big Lebowski",
                           "The Dude gets wrapped up in a mystery about a rug",
                           "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                           "https://youtu.be/x5SwmkpQqtc")

logan = media.Movie("Logan", "Wolverine's last adventure",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://youtu.be/Div0iP65aZo")

usual_suspects = media.Movie("The Usual Suspects", "A group of criminals are recruited for one last job",
                             "https://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg",
                             "https://youtu.be/oiXdPolca5w")

babe = media.Movie("Babe", "A pig that thinks he's a sheepdog",
                             "https://upload.wikimedia.org/wikipedia/en/6/6f/Babe_ver1.jpg",
                             "https://youtu.be/aKcFSeyYoLg")
# Add objects to list
movies = [toy_story, avatar, big_lebowski, logan, usual_suspects, babe]

# Use provided_fresh_tomatoes to open list of movies and creage webpage
fresh_tomatoes.open_movies_page(movies)

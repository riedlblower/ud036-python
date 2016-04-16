import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "http://media.babyoye.com/images/product/large/BPDIS00926_1.JPG",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

hunger_games = media.Movie("Hunger Games",
                     "A story of a teenager competes in a deadly state sponsored reality show",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                     "https://www.youtube.com/watch?v=mfmrPu43DF8",)

ratatouille = media.Movie("Ratatouille",
                              "A story of a trainee waiter and his friend rat that's a great chef",
                              "https://i.ytimg.com/vi/eh62Ri60lXI/movieposter.jpg",
                              "https://www.youtube.com/watch?v=c3sBBRxDAqk")

huntsman = media.Movie("The Huntsman: Winter's War",
                              "Eric and Sara conceal their love in a war between two rival queen sisters",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/a/ab/The_Huntsman_%E2%80%93_Winter's_War_poster.jpg/220px-The_Huntsman_%E2%80%93_Winter's_War_poster.jpg",
                              "https://www.youtube.com/watch?v=_W65ndip7MM")

jungle_book = media.Movie("The Jungle Book",
                              "Mowgli flees the jungle and embarks on a journey of self-discovery",
                              "http://empirecinema.com.au/sites/default/files/the-jungle-book-2016-poster-header-165110.jpg",
                              "https://www.youtube.com/watch?v=5mkm22yO-bs")

despicable = media.Movie("Despicable Me",
                              "When a criminal mastermind uses a trio of orphan girls as pawns for a grand scheme, he finds their love is profoundly changing him for the better.",
                              "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
                              "https://www.youtube.com/watch?v=sUkZFetWYY0")
movies = [toy_story, hunger_games, ratatouille, huntsman, jungle_book, despicable]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

import media
import fresh_tomatoes

toy_story = media.Movie('toy story',
                        'This is a story about the toy',
                        'https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=2523901191,811022794&fm=80',
                        'http://v.youku.com/v_show/id_XMTY2MzE4NDQ5Mg==.html?spm=0.0.yk-slide-86993.5~5!4~5~5!2~A.BnrIdu')

#print(toy_story.storyline)
#toy_story.show_trailer()

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=4200407871,3555187388&fm=80",
                     "http://v.youku.com/v_show/id_XMTY3MjU3MTc4NA==.html?beta&spm=0.0.posterMovieGrid86981.5~5~5~1~3!2~A.BnrIdu&from=y1.3-movie-grid-1095-9921.86981.1-10")

#print(avatar.storyline)
#avatar.show_trailer()

car = media.Movie("car",
                  "It's a car",
                  "https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=3831740550,2455926650&fm=80",
                  "http://v.youku.com/v_show/id_XMTcwMzg0MDEyMA==.html?beta&spm=0.0.yk-slide-107667.5~5!3~5~5!2~A.BnrIdu&from=y1.3-movie-grid-1095-9921.86985-107667.3-1")

#car.show_trailer()

movie = [toy_story, avatar, car]
#fresh_tomatoes.open_movies_page(movie)

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__bases__)

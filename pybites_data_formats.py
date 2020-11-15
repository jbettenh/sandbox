from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    automaker = {}
    for manf in data:
        automaker[manf['automaker']] = 0

    for model in data:
        if model['year'] == year:
            automaker[model['automaker']] = automaker.get(model['automaker']) + 1

    most_new_cars = max(automaker, key=automaker.get)

    return most_new_cars


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    unique_models = set()

    for model in data:
        if model['automaker'] == automaker and model['year'] == year:
            unique_models.add(model['model'])

    return unique_models


print(most_prolific_automaker(1999))

print(get_models('Dodge', 1999))

from collections import namedtuple
from datetime import datetime
import json

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

def dict2nt(dict_):
    # https://stackoverflow.com/questions/43921240/pythonic-way-to-convert-a-dictionary-into-namedtuple-or-another-hashable-dict-li
    mytuple= namedtuple('nt', dict_.keys())(**dict_)
    return mytuple

nt = dict2nt(blog)

def nt2json(nt):
    nt = nt._replace(started=str(nt.started))
    x = nt._asdict()
    j = json.dumps(x)
    return j

nt2json(nt)

import json

files = {"Title":"The Terminator","Year":"1984","Rated":"R","Released":"26 Oct 1984","Runtime":"107 min","Genre":"Action, Sci-Fi","Director":"James Cameron","Writer":"James Cameron, Gale Anne Hurd, William Wisher (additional dialogue)","Actors":"Arnold Schwarzenegger, Michael Biehn, Linda Hamilton, Paul Winfield","Plot":"A seemingly indestructible humanoid cyborg is sent from 2029 to 1984 to assassinate a waitress, whose unborn son will lead humanity in a war against the machines, while a soldier from that war is sent to protect her at all costs.","Language":"English, Spanish","Country":"UK, USA","Awards":"6 wins & 6 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BODE1MDczNTUxOV5BMl5BanBnXkFtZTcwMTA0NDQyNA@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"8.0/10"},{"Source":"Rotten Tomatoes","Value":"100%"},{"Source":"Metacritic","Value":"83/100"}],"Metascore":"83","imdbRating":"8.0","imdbVotes":"665,460","imdbID":"tt0088247","Type":"movie","DVD":"03 Sep 1997","BoxOffice":"N/A","Production":"Orion Pictures Corporation","Website":"http://www.terminator1.com/","Response":"True"}
{"Title":"Horrible Bosses","Year":"2011","Rated":"R","Released":"08 Jul 2011","Runtime":"98 min","Genre":"Comedy, Crime","Director":"Seth Gordon","Writer":"Michael Markowitz (screenplay), John Francis Daley (screenplay), Jonathan Goldstein (screenplay), Michael Markowitz (story)","Actors":"Jason Bateman, Steve Wiebe, Kevin Spacey, Charlie Day","Plot":"Three friends conspire to murder their awful bosses when they realize they are standing in the way of their happiness.","Language":"English","Country":"USA","Awards":"3 wins & 11 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNzYxNDI5Njc5NF5BMl5BanBnXkFtZTcwMDUxODE1NQ@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.9/10"},{"Source":"Rotten Tomatoes","Value":"69%"},{"Source":"Metacritic","Value":"57/100"}],"Metascore":"57","imdbRating":"6.9","imdbVotes":"378,076","imdbID":"tt1499658","Type":"movie","DVD":"11 Oct 2011","BoxOffice":"$116,900,000","Production":"Warner Bros. Pictures","Website":"http://horriblebossesmovie.warnerbros.com/index.html","Response":"True"}
{"Title":"Glengarry Glen Ross","Year":"1992","Rated":"R","Released":"02 Oct 1992","Runtime":"100 min","Genre":"Crime, Drama, Mystery","Director":"James Foley","Writer":"David Mamet (play), David Mamet (screenplay)","Actors":"Al Pacino, Jack Lemmon, Alec Baldwin, Alan Arkin","Plot":"An examination of the machinations behind the scenes at a real estate office.","Language":"English","Country":"USA","Awards":"Nominated for 1 Oscar. Another 6 wins & 10 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNTYzN2MxODMtMDBhOC00Y2M0LTgzMTItMzQ4NDIyYWIwMDEzL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTc1NTQxODI@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.8/10"},{"Source":"Rotten Tomatoes","Value":"94%"},{"Source":"Metacritic","Value":"80/100"}],"Metascore":"80","imdbRating":"7.8","imdbVotes":"83,208","imdbID":"tt0104348","Type":"movie","DVD":"20 Feb 2007","BoxOffice":"N/A","Production":"Artisan Home Entertainment","Website":"http://www.artisanent.com/glengarryglenross","Response":"True"}
{"Title":"Fight Club","Year":"1999","Rated":"R","Released":"15 Oct 1999","Runtime":"139 min","Genre":"Drama","Director":"David Fincher","Writer":"Chuck Palahniuk (novel), Jim Uhls (screenplay)","Actors":"Edward Norton, Brad Pitt, Meat Loaf, Zach Grenier","Plot":"An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.","Language":"English","Country":"USA, Germany","Awards":"Nominated for 1 Oscar. Another 10 wins & 32 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"8.8/10"},{"Source":"Rotten Tomatoes","Value":"79%"},{"Source":"Metacritic","Value":"66/100"}],"Metascore":"66","imdbRating":"8.8","imdbVotes":"1,508,138","imdbID":"tt0137523","Type":"movie","DVD":"06 Jun 2000","BoxOffice":"N/A","Production":"20th Century Fox","Website":"http://www.foxmovies.com/fightclub/","Response":"True"}
{"Title":"Blade Runner 2049","Year":"2017","Rated":"R","Released":"06 Oct 2017","Runtime":"164 min","Genre":"Mystery, Sci-Fi, Thriller","Director":"Denis Villeneuve","Writer":"Hampton Fancher (screenplay by), Michael Green (screenplay by), Hampton Fancher (story by), Philip K. Dick (based on characters from the novel \"Do Androids Dream of Electric Sheep?\")","Actors":"Ryan Gosling, Dave Bautista, Robin Wright, Mark Arnold","Plot":"A young blade runner's discovery of a long-buried secret leads him to track down former blade runner Rick Deckard, who's been missing for thirty years.","Language":"English, Finnish, Japanese, Hungarian, Russian, Somali, Spanish","Country":"USA, UK, Hungary, Canada","Awards":"6 wins & 13 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNzA1Njg4NzYxOV5BMl5BanBnXkFtZTgwODk5NjU3MzI@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"8.4/10"},{"Source":"Rotten Tomatoes","Value":"87%"},{"Source":"Metacritic","Value":"81/100"}],"Metascore":"81","imdbRating":"8.4","imdbVotes":"156,246","imdbID":"tt1856101","Type":"movie","DVD":"N/A","BoxOffice":"$89,276,502","Production":"Warner Bros. Pictures","Website":"http://bladerunnermovie.com","Response":"True"}

def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []

    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            movies.append(data)

    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    genre = "Comedy"
    for movie in movies:
        if movie['Genre'] == "Comedy":
            return movie['Title']


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    pass


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    longest_movie = max(movies, key=movies.get)

get_movie_data(files)
from string import ascii_lowercase

text ="""
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""


def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    results = []
    paragraph = (text.strip()).splitlines()

    for line in paragraph:
        line = line.lstrip()
        if line[0] not in ascii_lowercase:
            continue

        word = line.split(" ")[-1].rstrip("!.")
        results.append(word)

    return results


print(slice_and_dice(text))

from typing import Tuple

text1 = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
vowels = 'aeiou'


def strip_vowels(txt: str) -> Tuple[str, int]:
    """Replace all vowels in the input text string by a star
       character (*).
       Return a tuple of (replaced_text, number_of_vowels_found)

       So if this function is called like:
       strip_vowels('hello world')

       ... it would return:
       ('h*ll* w*rld', 3)

       The str/int types in the function defintion above are part
       of Python's new type hinting:
       https://docs.python.org/3/library/typing.html"""
    new_str = []
    letter = list(text1)
    num_vowels = 0

    for c in letter:
        if c.lower() in vowels:
            c = '*'
            num_vowels += 1
        new_str.append(c)

    return ''.join(new_str), num_vowels


print(strip_vowels(text1))


def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    only_evens = [num for num in numbers if num % 2 == 0 if num > 0]
    return only_evens


list_numbers = [0, -1, -3, -5]
print(filter_positive_even_numbers(list_numbers))


from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}


def get_total_points(belts=ninja_belts):
    """Calculate the amount of points rewarded on PyBites given the
       ninja_belts dictionary, formula: belt score x belt owners (aka ninjas)
       (of course there are more points but let's keep it simple)

       Make your code generic so if we update ninja_belts to include
       more belts (which we do in the tests) it will still work.

       Ah and you can get score and ninjas from the namedtuple with nice
       attribute access: belt.score / belt.ninjas (reason why we get
       you familiar with namedtuple here, because we love them and use
       them all over the place!)

       Return the total number of points int from the function."""
    total_score = 0

    for belt in belts.values():
        total_score = total_score + belt.score*belt.ninjas

    return total_score


print(get_total_points(ninja_belts))


WORKOUT_SCHEDULE = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
REST, CHILL_OUT, TRAIN = 'Rest', 'Chill out!', 'Go train {}'
INVALID_DAY = 'Not a valid day'


def get_workout_motd(day):
    """First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       If day is not in WORKOUT_SCHEDULE, return INVALID_DAY

       If day is in WORKOUT_SCHEDULE retrieve the value (workout)
       and return the following:
       - weekday, return TRAIN with the workout value interpolated
       - weekend day (value 'Rest'), return CHILL_OUT

       Examples:
       - if day is Monday -> function returns 'Go train Chest+biceps'
       - if day is Thursday -> function returns 'Go train Legs'
       - if day is Saturday -> function returns 'Chill out!'
       - if day is nonsense -> function returns 'Not a valid day'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'
    """

    formatted_day = day.lower().capitalize()
    if formatted_day in WORKOUT_SCHEDULE.keys():
        if WORKOUT_SCHEDULE[formatted_day] == REST:
            return CHILL_OUT
        else:
            return TRAIN.format(WORKOUT_SCHEDULE[formatted_day])
    else:
        return INVALID_DAY


print(get_workout_motd('MONDAY'))


def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    try:
        num = int(numerator)
        den = int(denominator)

    except ValueError as err:
        raise ValueError('The input could not be converted') from err

    try:
        result = num / den
        return result
    except ZeroDivisionError as err:
        return 0


print(divide_numbers(1, 2))
print(divide_numbers(8, 2))
print(divide_numbers('3', '2'))
print(divide_numbers(8.2, 2))
print(divide_numbers(1, 2.9))
# print(divide_numbers(2, 's'))
# print(divide_numbers('s', 2))
# print(divide_numbers('v', 'w'))
print(divide_numbers(10, 0))


import xml.etree.ElementTree as ET

# from OMDB
xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>'''  # noqa E501


def get_tree():
    """You probably want to use ET.fromstring"""
    root = ET.fromstring(xmlstring)
    return root


def get_movies():
    """Call get_tree and retrieve all movie titles, return a list or generator"""
    movies = []

    tree = get_tree()

    for branch in tree:
        movies.append(branch.get('title'))

    return movies


def get_movie_longest_runtime():
    """Call get_tree again and return the movie title for the movie with the longest
       runtime in minutes, for latter consider adding a _get_runtime helper"""
    tree = get_tree()
    runtimes = {}

    for branch in tree:
        runtime = branch.get('runtime')
        runtimes[branch.get('title')] = ([int(s) for s in runtime.split() if s.isdigit()])

    longest_runtime = max(runtimes, key=runtimes.get)

    return longest_runtime


print(get_movies())
print(get_movie_longest_runtime())

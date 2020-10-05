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








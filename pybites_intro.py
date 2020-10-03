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





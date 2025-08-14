from stats import count_words
from stats import count_each_character
from stats import sort_character_counts
import sys

def get_book_text(filepath):
    content = ""
    with open(filepath) as file:
        content = file.read()
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    number_of_words = count_words(text)
    number_of_each_character = sort_character_counts(count_each_character(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for dict in number_of_each_character:
        print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

main()
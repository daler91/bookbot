import sys
from stats import get_num_words,count_characters,sort_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    charCount = count_characters(text)
    sortedCount = sort_characters(charCount)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    formatSortedCount(sortedCount)
    print("""============= END ===============""")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def formatSortedCount(sortedCount):
    for items in sortedCount:
        char = items["char"]
        if char.isalpha() == True:
            print(f"{items["char"]}: {items["num"]}" )


main()

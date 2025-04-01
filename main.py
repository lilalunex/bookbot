from stats import get_books_words
from stats import get_books_chars

path_to_file = "books/frankenstein.txt"

def main():
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    get_books_words(path_to_file)
    get_books_chars(path_to_file)
    print(f"============= END ===============")

main()

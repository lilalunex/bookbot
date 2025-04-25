from stats import get_books_words
from stats import get_books_chars
from stats import sort

path_to_file = "books/frankenstein.txt"
words_in_book_dic = {}
words_in_book_list = []

def print_char_count_one():
    print(f"--------- Character Count -------")
    for key, value in words_in_book_dic.items():
        print(f"'{key}': {value}")

def print_char_count_two(list_to_print):
    print(f"--------- Character Count -------")
    for x in list_to_print:
        if x['char'].isalpha():
            print(f"{x['char']}: {x['num']}")

def main():
    global words_in_book_dic
    global words_in_book_list
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    get_books_words(path_to_file)
    words_in_book = get_books_chars(path_to_file)
    #print_char_count_one()
    words_in_book_list = sort(words_in_book)
    print_char_count_two(words_in_book_list)

    print(f"============= END ===============")


main()

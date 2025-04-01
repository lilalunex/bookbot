def get_books_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words_array = file_contents.split()
        print(f"----------- Word Count ----------")
        print(f"Found {len(num_words_array)} total words")

def sort_on(dict):
    return dict["key"]

def get_books_chars(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        dic = {}
        for char in file_contents:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        dic.sort(reverse=True, key=dic[value])
        print(f"--------- Character Count -------")
        for key, value in dic.items():
            print(f"'{key}': {value}")

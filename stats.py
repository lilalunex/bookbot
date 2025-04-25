def get_books_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words_array = file_contents.split()
        print(f"----------- Word Count ----------")
        print(f"Found {len(num_words_array)} total words")


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
    return dic


def sort_on(dic):
    return dic["num"]


def sort(dic):
    sorted_list = []
    for key, value in dic.items():
        temp_dic = {"char": key, "num": value}
        sorted_list.append(temp_dic)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

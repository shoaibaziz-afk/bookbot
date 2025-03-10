path = "/mnt/d/bootdevPython/bookbot/books/frankenstein.txt"
def get_text(path):
    with open(path) as f:
        text = f.read()
    return text
text = get_text(path)

def count_words(path):
    with open(path) as f:
        file_contents = f.read()
        characters = file_contents.split()
        word_count = len(characters)
    return word_count, file_contents

def character_count(text):
    char_dic = {}
    for char in text:
        char_dic[char.lower()] = char_dic.get(char.lower(), 0) + 1
    return char_dic

char_dic = character_count(text)

def sorted_char_count_dic(char_dic):
    char_count_dic = []
    for char, count in char_dic.items():
        char_count_dic.append({"char": char, "count": count})
    def sort_on(dict):
        return dict["count"]
    
    char_count_dic.sort(reverse = True, key = sort_on)
    return char_count_dic


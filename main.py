import sys
from stats import count_words
from stats import character_count
from stats import sorted_char_count_dic
path = sys.argv[1]

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_text(path):
    with open(path) as f:
        text = f.read()
    return text
text = get_text(path)
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    contents = get_book_text(path)
    word_count, _ = count_words(path)
    character_dic = character_count(text)
    sorted_char_count_list = sorted_char_count_dic(character_dic)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count_list:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")        
    # print(contents)
    # print(f"{word_count} words found in the document")
    # print(character_dic)
    # print(sorted_char_count_list)


main()
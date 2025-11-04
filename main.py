import sys
from stats import *

def main():
    book_path = arg_handler()
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def arg_handler():
    args_list = sys.argv
    if len(args_list) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = args_list[1]
    print("=" * 20)
    for arg in args_list:
        print(f"Arg: {arg}")

    print("=" * 20)
    return book_path

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count ----------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("========== END ==========")


main()


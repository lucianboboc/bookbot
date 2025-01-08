from django.conf.locale import fi


def main():
    with open('books/frankenstein.txt') as file:
        file_contents = file.read()
        print(file_contents)
        words_count = count_words(file_contents)
        chars_count = count_characters(file_contents)
        print_report(words_count, chars_count)


def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def count_characters(file_contents):
    map = {}
    for c in file_contents.lower():
        if c >= 'a' and c <= 'z':
            map[c] = map.get(c, 0) + 1
    return map


def print_report(words_count, chars_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document\n")

    for key, value in chars_count.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


main()

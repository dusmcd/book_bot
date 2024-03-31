def main():
    book_text = get_book_text("frankenstein.txt")
    word_count = get_word_count(book_text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"There are {word_count} words in Frankenstein")
    char_count = get_char_count(book_text)
    print_char_report(char_count)
    print("--- End report ---")

def get_book_text(filename):
    with open(f"books/{filename}") as f:
        return f.read()
    
def get_word_count(book_text):
    word_count = len(book_text.split())
    return word_count

def get_char_count(book_text):
    char_info = {}
    for i in range(0, len(book_text) - 1):
        lower_case_letter = book_text[i].lower()
        if lower_case_letter in char_info:
            char_info[lower_case_letter] += 1
        else:
            char_info[lower_case_letter] = 1

    return char_info

def print_char_report(char_info):
    letter_counts = []
    for char in char_info:
        if char.isalpha():
            letter_counts.append({"letter": char, "count": char_info[char]})
    letter_counts.sort(key=lambda item : item["count"], reverse=True)
    
    for letter_info in letter_counts:
        print(f"The '{letter_info["letter"]}' character was found {letter_info["count"]} times")
main()
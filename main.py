def main():
    # book_path = 'books/frankenstein.txt'
    # add input to the book_path variable
    book_path = input("Enter the relative path to the book: ")
    # if the book doesn't exist, print an error message and return
    if not is_valid_path(book_path):
        print("The book path is invalid")
        return
    
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")

    word_count = get_num_words(text)
    print(f"{word_count} words found in the document")

    char_count = get_num_characters(text)
    for cc in list(sorted(char_count, key=char_count.get, reverse=True)):
        print(f"The '{cc}' character was found {char_count[cc]} times")

    print("--- End report ---")

def get_num_words(text):
    return len(text.split())

def sort_on(dict):
    return dict['num']

def get_book_text(path):
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return file_contents
    
def get_num_characters(text):
    chars = {}
    for c in list(filter(lambda x: x.isalpha(), text.lower())):
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def is_valid_path(path):
    try:
        with open(path) as f:
            pass
    except FileNotFoundError:
        return False
    return True

main()
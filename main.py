def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = character_count(text)
    report(char_count, num_words)
    #print(f"{char_count} characters stored in the document")
    #print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def character_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1
    return char_count

def report(char_count, num_words):
    print(f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document\n\n")
    
    for char, count in char_count.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


main()
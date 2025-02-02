def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_counts = count_characters(text)

    generate_report(book_path, num_words, sort_char_counts(character_counts))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}

    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
    
def sort_char_counts(counts):
    sorted_chars = {}
    values = [counts[key] for key in counts.keys() if key.isalpha()]
    values.sort(reverse=True)
    for value in values:
        for item in counts:
            if counts[item] == value:
                sorted_chars[item] = value
    return sorted_chars

def generate_report(path, words, characters):
    print(f"--- Begin report of {path} ---")
    print(f"{words} found in the document")
    print()
    for key, value in characters.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")
main()
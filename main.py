"""Functions for reading a text file and counting words/characters used in a text and printing a report"""

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_counts = count_characters(text)

    generate_report(book_path, num_words, sort_char_counts(character_counts))

def get_book_text(path):
    """Open a text file and read it.
    
    :param path: str - path to file to read
    :return: str - contents of file as a single string
    """

    with open(path) as f:
        return f.read()

def count_words(text):
    """Split string on ' ' and count number of words in list
    
    :param text: str - the string containing the words to count
    :return: int - number of words in text
    """
    
    words = text.split()
    return len(words)

def count_characters(text):
    """Create a dictionary of each letter in a text as a key and the number of
        times that letter (case-insensitive) is used in the text as the corresponding value
    
    :param text: str - the string containing the text to be counted
    return: dict - dictionary comprised of indiividual letters used in a text w/ their corresponding counts
    """
    char_counts = {}

    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
    
def sort_char_counts(counts):
    """Creates a dictionary of only letters used in a text with their corresponding counts
    and sorts it from high count to low count
    
    :param counts: dict - dictionary of all characters used in a text with their corresponding counts
    return: dict - dictionary of only letters used with their counts sorted based on count from high to low
    """
    sorted_chars = {}
    values = [counts[key] for key in counts.keys() if key.isalpha()]
    values.sort(reverse=True)
    for value in values:
        for item in counts:
            if counts[item] == value:
                sorted_chars[item] = value
    return sorted_chars

def generate_report(path, words, characters):
    """Prints a formatted report of word and character counts for a text file
    
    :param path: str - path of the file the report is based on
    :param words: int - number of words in the text file
    :param characters: dict - dictionary of letters in the text with their counts sorted from high to low
    :return: None
    """
    print(f"--- Begin report of {path} ---")
    print(f"{words} found in the document")
    print()
    for key, value in characters.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")
main()
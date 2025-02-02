def main():
    file_path = "books/frankenstein.txt"
    
    book_text = read_file(file_path)
    word_count = count_words(book_text)
    char_dict = count_characters(book_text.lower())

    print(char_dict)

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    dict = {}
    for char in text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    return dict

main()
def main():
    file_path = "books/frankenstein.txt"
    
    book_text = read_file(file_path)
    word_count = count_words(book_text)
    char_dict = count_characters(book_text.lower())
    sorted_char = list_of_dicts(char_dict)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    for dicts in sorted_char:
        char = dicts["character"]
        if char.isalpha():
            count = dicts["count"]
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

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

def sort_key(dict):
    return dict["count"]

def list_of_dicts(dict):
    list = []
    for char in dict:
        count = dict[char]
        new_dict = {"character": char, "count": count}
        list.append(new_dict)
    list.sort(reverse=True, key=sort_key)
    return list

main()
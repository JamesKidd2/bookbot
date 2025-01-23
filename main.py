def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_string = text.lower()
    char_count = {}
    chars_dict = get_character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(nums_chars_dict):
    sorted_list = []
    for ch in nums_chars_dict:
        sorted_list.append({"char": ch, "num": nums_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

def get_num_words(text):
    words = text.split()
    return len(words)


#get_lower_case(text):

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


main()
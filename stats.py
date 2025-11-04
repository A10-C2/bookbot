def get_num_words(words):
    word_list = words.split()
    counter = 0
    for word in word_list:
        counter += 1

    return counter

def get_chars_dict(string):
    seen = {}
    for char in string:
        char = char.lower()
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] += 1
    return seen

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

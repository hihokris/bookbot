def num_words(book_string_for_count):
    return len(book_string_for_count.split())

def character_dict(book_string_for_count):
    char_dict = {}
    for char in book_string_for_count.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(items):
    return items["num"]

def sort_to_decend(dict_for_desc):
    list_of_dict=[]
    iter=0
    for k,v in dict_for_desc.items():
        list_of_dict.append({"key": k, "num":v})

    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

from stats import num_words, character_dict, sort_to_decend
import sys

def get_book_text(filePath):
    bookstring = ""
    with open(filePath) as f:
        bookstring = f.read()
    return bookstring

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = "./" + sys.argv[1]
    string_for_count = get_book_text(book_path)
    

    local_dict = character_dict(string_for_count)
#    for iter in local_dict.keys():
 #       iter2 = local_dict[iter]
 #       print("'"+iter+"': " + str(iter2))
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path + "...")
    print("----------- Word Count ----------")
    print("Found " + str(num_words(string_for_count)) + " total words")
    print("--------- Character Count -------")
    for items in sort_to_decend(local_dict):
        if (items["key"].isalpha()):
            print((items['key'])+": " +str(items['num']))

main()
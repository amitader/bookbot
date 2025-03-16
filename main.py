from stats import count_books_words,char_count,sorted_list
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath=sys.argv[1]
    print(filepath)
    print(len(sys.argv))
    book_contents=get_book_text(filepath)
    num_words=count_books_words(book_contents)
    char_stats=char_count(book_contents)
    sordet_list=sorted_list(char_stats)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for  i in sordet_list:
         if i["char"].isalpha():
             print(f"{i['char']}: {i['value']}")
    print("============= END ===============")


if __name__=="__main__":
    main()

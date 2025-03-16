def count_books_words(book_contents):
    num_words=len(book_contents.split())
    return num_words

def char_count(book_contents):
    num_words = list(book_contents)
    chars_dict={}
    for c in num_words:
         if c.lower() in chars_dict:
            chars_dict[c.lower()]+=1
         else:

            chars_dict[c.lower()] = 1
    return chars_dict

def sorted_list(chars_dict):
    dicts_list=[]
    dict_list = [{'char': k, 'value': v} for k, v in chars_dict.items()]
    dict_list.sort(reverse=True, key=lambda dict_list: dict_list["value"])
    return dict_list
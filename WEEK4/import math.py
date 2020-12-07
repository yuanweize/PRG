# def replace_chars(string,char_original,char_replacement):
#     new_string=""
#     for letter in string:
#         if letter == char_original:
#             new_string = new_string + char_replacement
#         else:
#             new_string = new_string + letter
#     return new_string

# if __name__=="__main__":
#     modified_string = replace_chars("hello","l","L")
#     print(modified_string)


def reverse_string(string):
    new_string=""
    for letter in string:
        new_string=letter +new_string
    return new_string

if __name__=="__main__":
    modified_string=reverse_string('hello')
    print(modified_string)




def is_palindrom(string):
    return reverse_string(string) == string
if __name__=="__main__":
    print(is_palindrom('abcd'))
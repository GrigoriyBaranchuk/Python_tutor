# def to_camel_case(string):
#     lst = string.replace("_", " ").replace("-", " ").split(" ")
#     new_lst = []
#     new_lst.append(lst[0])
#     for i in range(1, len(lst)):
#         new_lst.append(lst[i].capitalize())
#     return "".join(new_lst)
#
# import numpy as np


numbers = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        'eight': "8",
        "nine": "9",
        "ten": "10",
        "eleven": "11",
        "twelve": "12",
        "thirteen": "13",
        "fourteen": "14",
        "fifteen": "15",
        "sixteen": "16",
        "seventeen": "17",
        "eighteen": "18",
        "nineteen": "19",
        "twenty": "20",
        "thirty": "30",
        "forty": "40",
        "fifty": "50",
        "sixty": "60",
        "seventy": "70",
        "eighty": "80",
        "ninty": "90",
        "hundred": "100",
        "thousand": "1000",
        "million": "1000000",
    }
string = 'one million two hundred thousand one thousand two hundred forty-six'
list_string = string.split(" ")





#
# def fun_chunk(lst, n):
#     new_list = []
#     for i in range(0, len(lst), n):
#         new_list.append(lst[i:i+n])
#     return new_list
#
#
# for lst in fun_chunk(list_string, 2):
#     if "-" not in lst[-1]:
#         print(int(numbers[lst[0]]) * int(numbers[lst[1]]))
#     else:
#         if "-" in lst[-1]:
#             list_num = lst[-1].replace('-', ' + ').split(' ')
#             new_list = [numbers[n] if n in numbers.keys() else n for n in list_num]
#             print(eval("".join(new_list)))
#         else:
#             print(int(numbers[lst[-1]]))
#
#



# print( "-" in fun_chunk(list_string, 2)[-1])
# print(list(fun_chunk(list_string,2)))
#
# string2 = [1, 2, 'forty-six']
# print("-" not in string2[-1])

# def parse_int(arr):
#     numbers = {
#         "zero": "0",
#         "one": "1",
#         "two": "2",
#         "three": "3",
#         "four": "4",
#         "five": "5",
#         "six": "6",
#         "seven": "7",
#         'eight': "8",
#         "nine": "9",
#         "ten": "10",
#         "eleven": "11",
#         "twelve": "12",
#         "thirteen": "13",
#         "fourteen": "14",
#         "fifteen": "15",
#         "sixteen": "16",
#         "seventeen": "17",
#         "eighteen": "18",
#         "nineteen": "19",
#         "twenty": "20",
#         "thirty": "30",
#         "forty": "40",
#         "fifty": "50",
#         "sixty": "60",
#         "seventy": "70",
#         "eighty": "80",
#         "ninty": "90",
#         "hundred": "100",
#         "thousand": "1000",
#         "million": "1000000",
#     }
#
#     if len(arr.split(" ")) == 1:
#         if "-" in arr:
#             list_num = arr.replace('-', ' + ').split(' ')
#             new_list =[numbers[n] if n in numbers.keys() else n for n in list_num]
#             return eval("".join(new_list))
#         return int(numbers[arr])
#
# print(parse_int(string))
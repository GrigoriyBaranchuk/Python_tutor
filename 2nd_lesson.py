# def polindrom(lst: list) -> list:
#     #import pdb; pdb.set_trace()
#     new_list = []
#     for word in lst:
#         if word == word[::-1]:
#             new_list.append(word)
#     return new_list
#
#
# lst = ["дед", "дерево", "город", "gorod", "автомобиль", "заказ", "шалаш","книги", "око"]
#
#
# print(polindrom(lst))
#
# print("город" == "город"[::-1])
# print("город"[::-1])
#
# lst = ["дед", "дерево", "город", "gorod", "автомобиль", "заказ", "шалаш", "книги", "око"]
# new_list = [word for word in lst if word == word[::-1]]
# print(new_list)
#
# # print(polindrom(lst))

# lst = [1, 1, 2, 3, 4, 5, 5, 4, 3, 1, 5, 4]
#
#
# def unque_list(lst: list) -> dict:
#     return {num: lst.count(num) for num in lst}
#
# print(unque_list(lst))
#
# print(len(lst) == sum(unque_list(lst).values()))




# def no_pair(lst: list) -> list:
#     new_list = []
#     for i in range(len(lst)):
#         if - lst[i] not in lst:
#             new_list.append(lst[i])
#     return new_list
#
#
# print(no_pair(lst))
#
#
# def numer(lst: list) -> list:
#     new_list = []
#     for index, element in enumerate(lst):
#         # if - lst[i] not in lst:
#         #    new_list.append(lst[i])
#         if - element not in lst:
#             new_list.append(element)
#
#     return new_list
#
# print(numer(lst))


# lst = [1, -1, 2, -2, 4, -4, 3, 3, 5, 7, -4, -8]
#
# def pair_antonims(lst: list) -> list:
#     new_main_list = []
#     for  looking for lst.pop()

# lst = [1, 2, 3, 4, 5]
#
#
# def stair(lst: list):
#     string = ''
#     for index, element in enumerate(lst):
#         string += str(element)
#         print(string)
#         # print(lst[:index+1])
#
# print(stair(lst))


dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}


# dict_a.update(dict_b)
# dict_a.update(dict_c)

dict_sum = {**dict_a, **dict_b, **dict_c}
dict_copy = dict(**dict_sum)
print(dict_copy)

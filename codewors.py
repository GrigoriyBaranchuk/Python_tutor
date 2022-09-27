import math


def persistence(m):
    counter = 0
    #import pdb; pdb.set_trace()
    while len(str(m)) > 1:
        m = math.prod([int(x) for x in str(m)])
        counter += 1
    return counter


def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


def find_nb(m):
    output = 1
    check = 0
    while check <= m:
        check += output ** 3
        if check == m:
            return output
        output += 1
    return -1


def sort_array(source_array): #Sort the od
    sorted_odds = sorted([n for n in source_array if n % 2 == 1])
    new_list = []
    for num in source_array:
        if num % 2:
            new_list.append(sorted_odds.pop(0))
        else:
            new_list.append(num)
    return new_list


def stray(arr):
    dict_count = {int(n): "".join([str(x) for x in arr]).count(n) for n in "".join([str(x) for x in arr])}
    set_arr = list(set(arr))
    if dict_count[set_arr[0]] > dict_count[set_arr[1]]:
        return dict_count[set_arr[1]]
    else:
        return dict_count[set_arr[0]]


def points(lst):
    points = 0
    for mathc in lst:
        #import pdb; pdb.set_trace()
        my_team = [int(x) for x in mathc.split(":")][0]
        compitetors = [int(x) for x in mathc.split(":")][1]
        if my_team > compitetors:
            points += 3
        elif my_team < compitetors:
            points += 0
        elif my_team == compitetors:
            points += 1

    return points


def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]


def duplicate_count(text):
    dict_char = {n: text.lower().count(n) for n in text.lower()}
    new_arr =[]
    for k, v in dict_char.items():
        if v > 1:
            new_arr.append(k)

    return len(new_arr)

string = "the_stealth-warrior"




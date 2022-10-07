string = "two hundred forty-five"



def parsing_numbers(string):
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
    }

    zero = {
        "ten": "10",
        "hundred": "100",
        "thousand": "1000",
        "million": "1000000",
    }
    sting_normal = string.replace("  ", " ")
    list_num = sting_normal.split(" ")
    new_string = []
    if len(list_num) == 1:
        if "-" in string:
            new_list1 = [numbers[n] if n in numbers.keys() else n for n in string.replace("-", " + ").split(" ")]
            new_string.append("".join(new_list1))
            return eval(new_string[0])
        elif "-" not in string:
            new_string.append(numbers[string])
            return eval(new_string[0])
    else:
        for index, element in enumerate(list_num):
            try:
                if element in numbers.keys() and list_num[list_num.index(element)+1] in zero.keys():
                    new_string.append(numbers[element])
                    new_string.append("*")
                    new_string.append(zero[list_num[list_num.index(element)+1]])
                elif "-" in element:
                    new_list1 = [numbers[n] if n in numbers.keys() else n for n in element.replace("-", " + ").split(" ")]
                    new_string.append("".join(new_list1))
            except:
                pass
                return new_string


print(parsing_numbers(string))


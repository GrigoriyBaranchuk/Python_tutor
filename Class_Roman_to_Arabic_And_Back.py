
def to_roman(data):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]

    t = thous[data // 1000]
    h = hunds[data // 100 % 10]
    te = tens[data // 10 % 10]
    o = ones[data % 10]

    return t + h + te + o


def from_roman(s: str) -> int:
    res = 0
    rtoa = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(len(s) - 1):
        if (rtoa[s[i]] < rtoa[s[i + 1]]):
            res = res - rtoa[s[i]]
        elif (rtoa[s[i]] >= rtoa[s[i + 1]]):
            res = res + rtoa[s[i]]

    res = res + rtoa[s[len(s) - 1]]
    return res


numbers = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

ROMANS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'C': 100,
    'XC': 90,
    'L': 50,
    'X': 10,
    'V': 5,
    'IV': 4,
    'I': 1,
}


class RomanNumerals:

    def to_roman(n):
        s = ''
        for key, value in ROMANS.items():
            while n % value != n:
                n = n - value
                s += key
        return s

    def from_roman(r):
        s = 0
        for key, value in ROMANS.items():
            while r.startswith(key):
                r = r[len(key):]
                s += value
        return s

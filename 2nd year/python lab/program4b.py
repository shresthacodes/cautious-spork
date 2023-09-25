import re
def roman_to_int(roman):
    roman_numerals = {
        'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5, 'I': 1 }
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

    if re.match(pattern, roman):
        total = 0
        prev_value = 0
        for num in reversed(roman):
            value = roman_numerals[num]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
    else:
        return "Invalid Roman numeral"
roman_numeral = input(">>")
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}")

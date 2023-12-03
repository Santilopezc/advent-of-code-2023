import re
def second_problem():
    number_str_to_digit = {'one':'1','two':'2',
                        'three':'3','four':'4',
                        'five':'5','six':'6',
                        'seven':'7','eight':'8',
                        'nine':'9'}
    with open ('input.txt','r') as file:

        sum = 0
        for line in file.readlines():
            # Find the first digit, either numeric or textual representation
            first_digit_match = re.search(r'(?:one|two|three|four|five|six|seven|eight|nine|\d)', line, re.IGNORECASE)
            first_digit = first_digit_match.group() if first_digit_match else 0
            if not first_digit.isdigit():
                first_digit = number_str_to_digit[first_digit]

            # Find the last digit, either numeric or textual representation
            last_digit_match =re.search(r'(?:eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)', line[::-1], re.IGNORECASE)
            last_digit = last_digit_match.group()[::-1] if last_digit_match else 0
            if not last_digit.isdigit():
                last_digit = number_str_to_digit[last_digit]
            sum += int(first_digit + last_digit)

        return sum
print(second_problem())
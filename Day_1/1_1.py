def first_problem():
    with open ('input.txt','r') as file:
        digits = []
        for line in file.readlines():
            first_digit = None
            last_digit = None
            if not first_digit:
                for index, char in enumerate(line):
                    if char.isdigit():
                        first_digit = char
                        break
            for index, char in enumerate(line[::-1]):
                if char.isdigit():
                    last_digit = char
                    break
            digits.append(int(first_digit + last_digit))
            first_digit = None
            last_digit = None
        return sum(digits)    
    
print(first_problem())

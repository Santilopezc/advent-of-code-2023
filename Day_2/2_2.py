import re
def extract_numbers_by_color():
    with open ('input.txt','r') as file:
        sum = 0
        index = 1
        for line in file.readlines():
            pattern = r'(\d+)\s+(\w+)'
            matches = re.findall(pattern, line)

            result = {}
            for number, color in matches:
                number = int(number)
                current_max = result.get(color, float('-inf'))  # Default to negative infinity if the color is not in the result dictionary
                result[color] = max(current_max, number)
            # Multiplication of all values in a dictionary
            multiplication = result['red'] * result['green'] * result['blue']
            sum += multiplication
        return sum
print(extract_numbers_by_color())
import re
possible_games = {'red': 12,
                  'green': 13,
                  'blue': 14,}

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
            is_legal = all(result.get(color,0) <= possible_games[color] for color in possible_games)

            if is_legal:
                sum += index
            index += 1
        return sum

print(extract_numbers_by_color())

with open('input.txt', 'r') as file:
    sum = 0
    for line in file.readlines():
        card_string, number_string = line.split(':')
        winning_numbers = number_string.split('|')[0].split()
        my_numbers = number_string.split('|')[1].split()
        common_numbers = len(set(winning_numbers) & set(my_numbers))
        sum += 2**(common_numbers-1) if common_numbers else 0
    print(sum)



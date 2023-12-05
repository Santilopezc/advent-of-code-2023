with open('input.txt', 'r') as file:
    lines = file.readlines()


current_card = 1
card_copies = {}
for i in range(1, len(lines)+1):
    card_copies[i] = 1

for line in lines:
    card_string, number_string = line.split(':')
    winning_numbers = number_string.split('|')[0].split()
    my_numbers = number_string.split('|')[1].split()
    common_numbers = len(set(winning_numbers) & set(my_numbers))
    print(f'Current card: {current_card}')
    print(f'Matching numbers: {common_numbers}')
    print(f'First card copy: {current_card + 1}, until: {current_card + common_numbers}')
    if common_numbers!=0:
        for i in range(current_card + 1, current_card + common_numbers + 1):
            card_copies[i] += card_copies[current_card]
    current_card += 1
    print(card_copies)
result = sum(card_copies.values())
print(result)



list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = list_numbers[0]

for current_num in list_numbers:
    if current_num > max_:
        max_ = current_num


list_numbers[9], list_numbers[-1] = list_numbers[-1], max_

print(list_numbers)

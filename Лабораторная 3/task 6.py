list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = 0
i_element = list_numbers[0]

for i in range(len(list_numbers)):
     if list_numbers[i] > i_element:
        i_element = list_numbers[i]
        max_ = i

list_numbers[-1], list_numbers[max_] = list_numbers[max_], list_numbers[-1]  #присваиваем a, b = b. a

print(list_numbers)

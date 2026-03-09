numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
first_part = numbers[:4]
second_part = numbers[5:]
new_numbers = first_part + second_part
new_element = sum(new_numbers)/len(numbers)
numbers[4] = new_element
print("Измененный список:", numbers)

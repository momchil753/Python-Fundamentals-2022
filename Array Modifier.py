array = list(map(int, input().split(' ')))
numbers = array
command = input()


while True:

    if command == "end":
        break

    new_command = command.split(' ')
    current_command = new_command[0]

    if len(new_command) > 1:
        element_1_pos = int(new_command[1])
        element_2_pos = int(new_command[2])

    if current_command == "swap":
        numbers[element_1_pos], numbers[element_2_pos] = numbers[element_2_pos], numbers[element_1_pos]

    if current_command == "multiply":
        numbers[element_1_pos] = numbers[element_1_pos] * numbers[element_2_pos]

    if current_command == "decrease":
        numbers = [number - 1 for number in array]

    command = input()

fixed_lst = str(numbers)[1:-1]
print(fixed_lst)
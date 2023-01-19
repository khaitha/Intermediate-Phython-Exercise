def unique_list(input_list):
    unique_list = []
    for i in input_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

my_list = [1, 2, 3, 2, 1, 4]
print(unique_list(my_list))
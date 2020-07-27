def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return recursive_search(input_list, number, 0 , len(input_list)-1)

def recursive_search(input_list, number, start_index, last_index):
    mid = (start_index + last_index) // 2
    #print(start_index, last_index)
    if start_index > last_index:
        return -1
        
    if input_list[mid] == number:
        return mid

    if input_list[mid] <= input_list[last_index]:
        if number >= input_list[mid] and number <= input_list[last_index]:
            return recursive_search(input_list, number, mid+1, last_index)
        else:
            return recursive_search(input_list, number, start_index, mid-1)
    elif number >= input_list[mid] or number <= input_list[last_index]:
        return recursive_search(input_list, number, mid+1, last_index)
    else:
        return recursive_search(input_list, number, start_index, mid-1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)) #expected output: 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
print('--------------------------------------')

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)) #expected output: 5
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
print('--------------------------------------')

print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8)) #expected output: 2
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
print('--------------------------------------')

print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1)) #expected output: 3
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
print('--------------------------------------')

print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 9)) #expected output: -1
test_function([[6, 7, 8, 1, 2, 3, 4], 19])
print('--------------------------------------')

print(rotated_array_search([4,5,6,7,8,1,9,10,2], 3)) #expected output: -1
test_function([[4,5,6,7,8,1,9,10,2], 3])
print('--------------------------------------')




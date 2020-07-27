def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    index = 0
    low_index = 0
    high_index = len(input_list)-1
    
    while index <= high_index:
        if input_list[high_index] == 2:
            high_index -= 1
            continue
        if input_list[index] == 0:
            input_list[index] = input_list[low_index]
            input_list[low_index] = 0
            index += 1
            low_index += 1
        elif input_list[index] == 2:
            input_list[index] = input_list[high_index]
            input_list[high_index] = 2
            high_index -= 1
        else:
            index += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
#expected output: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
print('---------------------------------')

print(sort_012([1,2,1,2,2,2,1,1,2,1]))
#expected output: [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
test_function([1,2,1,2,2,2,1,1,2,1])
print('---------------------------------')

print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
#expected output: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('---------------------------------')

print(sort_012([0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0]))
#expected output: [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
test_function([0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0])
print('---------------------------------')

print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
#expected output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
print('---------------------------------')




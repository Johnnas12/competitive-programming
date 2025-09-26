'''
Impelementing Reverse an Array really easy problem from inefficient solution to efficient
'''

# the below implementation runs O(n) since its copied to new array
def reverse_array(list_to_reverse):
    new_array = []
    last_index = len(list_to_reverse) - 1
    for i in range(len(list_to_reverse)):
        new_array.append(list_to_reverse[last_index])
        last_index -= 1
    return new_array

# the below is in place efficient implementation with space complexity O(1) and O(n) time complexity
def reverse_array_optimal(list_to_reverse):
    left_pointer = 0 
    right_pointer = len(list_to_reverse) -1 

    while left_pointer < right_pointer:
        left_pointer_value = list_to_reverse[left_pointer]
        right_pointer_value = list_to_reverse[right_pointer]

        list_to_reverse[left_pointer] = right_pointer_value
        list_to_reverse[right_pointer] = left_pointer_value

        left_pointer += 1
        right_pointer -= 1
    return list_to_reverse


if __name__ == "__main__":
    original_array = [1, 4, 3, 2, 6, 5]
    print(reverse_array(original_array))
    print(reverse_array_optimal(original_array))

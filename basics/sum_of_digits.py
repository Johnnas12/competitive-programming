'''
one of simple and famous problem called sum of digits we will take multple approach to solve this problem
'''
# implementation of sum of digits 
def sum_of_digits(number):
    result = 0
    while number != 0:
        digit = number % 10 
        result += digit
        number //=  10
    return result

# recursive implementation
def sum_of_digits_recursive(number):
    if number == 0:
        return 0
    return number % 10 + sum_of_digits_recursive(number // 10)

# converting intiger into string to solve the problem 
def sum_of_digits_string(number):
    converted = str(number)
    result = 0
    for char in converted:
        result += int(char)
    return result

if __name__ == "__main__":
    print(sum_of_digits(687))
    print(sum_of_digits_recursive(687))
    print(sum_of_digits_string(687))



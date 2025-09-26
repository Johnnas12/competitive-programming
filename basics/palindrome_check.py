def palindrome_check(str):
    reversed_string = str[::-1]
    if reversed_string == str:
        return True
    else:
        return False
    

# we can use two pointer to reverse the string
def palindrome_check_2(str):
    i, j = 0, len(str) - 1
    while i < j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True

# recursive Implementation of it
def palindrome_check_recursive(str, i, j):
    if i >= j:
        return True
    if str[i] != str[j]:
        return False
    return palindrome_check_recursive(str, i+1, j-1)



if __name__ == "__main__":
    str= "malayalam"
    print(palindrome_check(str))
    print(palindrome_check_2(str))
    print(palindrome_check_recursive(str, 0, len(str)-1))

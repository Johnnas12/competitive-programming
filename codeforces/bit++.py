
def bit_plus_plus(expression, value):
    str_to_list = list(expression)
    # for perfix expression
    if str_to_list[0] and str_to_list[1] == '+':
        result = value + 1
        return result

    # for suffix expression
    if str_to_list[1] and str_to_list[2] == '+':
        result = value + 1
        return result

    # for suffix expression of subtraction
    if str_to_list[0] and str_to_list[1] == '-':
        result = value - 1
        return result

    # for suffix expression
    if str_to_list[1] and str_to_list[2] == '-':
        result = value - 1
        return result


if __name__ == "__main__":
    n = int(input())
    final_result = 0
    value  = 0
    for _ in range(n):
        user_input = str(input())
        value = bit_plus_plus(user_input, value)
    print(value)

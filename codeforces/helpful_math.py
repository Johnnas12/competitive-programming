input_string = input()
cleaned = input_string.split("+")
to_integer_list = [int(s) for s in cleaned]
to_integer_list.sort()

print("+".join(map(str, to_integer_list)))
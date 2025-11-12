user_input = input()

splitted = user_input.split(" ")

number = int(splitted[0])
steps = int(splitted[1])

for i in range(steps):
    if number % 10 == 0:
        number //= 10
    else:
        number -= 1
print(number)
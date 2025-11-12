n = int(input())
steps = [5, 4, 3, 2, 1]

for i in range(len(steps)):
    if n == steps[i]:
        print()
        break
    elif n % steps[i] == 0:
        result = n // steps[i]
        print(result)
        break
        
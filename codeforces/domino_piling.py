n = input()
splitted_n = n.split(" ")
my_m = int(splitted_n[0])
my_n = int(splitted_n[1])

row_occupied = my_m // 2
colwise = 0
remainder = my_m % 2
if remainder > 0:
    colwise  = my_n // 2

result = (row_occupied * my_n) + colwise
print(result)
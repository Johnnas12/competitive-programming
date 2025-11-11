user_input = input()
clean = user_input.split(" ")
a = int(clean[0])
b = int(clean[1])

year_counter = 0
while True:
    a = a * 3
    b = b * 2
    year_counter+=1
    if a > b:
        break

print(year_counter)
        
    
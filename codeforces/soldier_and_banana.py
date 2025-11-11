user_input = input()
clean = user_input.split(" ")

k = int(clean[0])
n = int(clean[1])
w = int(clean[2])
total_price = 0
for i  in range(w):
    total_price += (k * (i+1))
    
if (total_price - n)  <= 0:
    print(0)
else:
    print(total_price - n)

    
    



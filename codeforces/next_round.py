n = input()
splitted = n.split(" ")
my_n = int(splitted[0])
k = int(splitted[1])
count = 0

for _ in range(my_n):
    scores = input()
    scores_splitted = scores.split(" ")
    break
integer_list = list(map(int, scores_splitted))
for i in range(my_n):
    if integer_list[i] <= 0:
        continue
    if integer_list[i] >= int(integer_list[k-1]):
        count+=1
print(count)
    
    
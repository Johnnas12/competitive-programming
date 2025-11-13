n = int(input())
s = input()
count_anton = 0
count_dan = 0
for i in range(n):
    if s[i] == 'A':
        count_anton += 1
    else:
        count_dan += 1

if count_anton > count_dan:
    print("Anton")
elif count_anton < count_dan:
    print("Danik")
else:
    print("Friendship")
    
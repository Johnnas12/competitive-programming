s = input()

count_consecutive = 0

for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        count_consecutive += 1
        if count_consecutive == 7:
            print("YES")
            break
    else:
        count_consecutive = 0
print("NO")
input_str = input()
umap = {}
key = 0
for letter in input_str:
    umap[letter] = key
    key+=1
    
length = len(umap)

if length % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
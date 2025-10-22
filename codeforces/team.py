def team(descision):
    splitted = descision.split(" ")
    counter = splitted.count("1")
    if counter >= 2:
        return True
    
if __name__ == "__main__":
    t = int(input())
    total = 0 
    for _ in range(t):
        my_input = input()
        result = team(my_input)
        if result:
            total += 1
    print(total)
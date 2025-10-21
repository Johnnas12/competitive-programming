def watermelon(w):
    if w>2 and w%2==0:
        return "Yes"
    return "No"

if __name__ == "__main__":
    w = int(input())
    print(watermelon(w))
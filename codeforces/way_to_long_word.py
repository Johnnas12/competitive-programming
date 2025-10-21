def way_to_long(my_str):
    n = len(my_str)
    if n <= 10:
        return my_str
    else:
        first = my_str[0]
        last = my_str[-1]
        return f"{first}{n - 2}{last}"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        word = input().strip()
        print(way_to_long(word))
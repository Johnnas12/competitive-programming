user_input = input()
splitted = user_input.split(" ")
n = int(splitted[0])
fence_height = int(splitted[1])

heights = input()
heights_splitted = heights.split(" ")

minimum_width = 0
for individual_height in heights_splitted:
    if fence_height < int(individual_height):
        minimum_width += 2
    else:
        minimum_width += 1
print(minimum_width)
    

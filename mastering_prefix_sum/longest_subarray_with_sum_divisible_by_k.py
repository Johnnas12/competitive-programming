def longest_sub_array_by_k(arr, k):
    n = len(arr)
    umap = {}
    sum = 0
    result = [0]
    
    for i in range(n):
        
        sum += arr[i]

        if sum % k == 0:
            result.append(i + 1)   
        else:
             diff = sum % k
             if diff in umap:    
                j = umap[diff]   
                result.append(i -j) 
            #  adding them to hashmap
        if sum not in umap:
                umap[sum % k] = i
    return max(result)


if __name__ == "__main__":
    arr= [2, 7, 6, 1, 4, 5]
    k = 3

    print(longest_sub_array_by_k(arr, k))
    		



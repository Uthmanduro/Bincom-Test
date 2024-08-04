def recursive_search(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return recursive_search(arr, target, index + 1)

# Example usage
arr = [1, 2, 3, 4, 5]
target = 3
print("Index of target:", recursive_search(arr, target))

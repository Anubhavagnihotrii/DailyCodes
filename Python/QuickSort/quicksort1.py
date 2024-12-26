def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        less_than_pivot = [x for x in arr[:-1] if x <= pivot]
        greater_than_pivot = [x for x in arr[:-1] if x > pivot]
    return quickSort(less_than_pivot) + [pivot] + quickSort(greater_than_pivot)

if __name__ == "__main__":
    arr = [-1, 2, 3,21,4,-2,56,8]
    sorted_arr = quickSort(arr)
    print("Sorted array:", sorted_arr)
    print(type(sorted_arr))

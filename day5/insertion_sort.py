def sort_insert(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and item < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = item

    return arr


if __name__ == "__main__":
    data = [1, 4, 5, 0]
    print(sort_insert(data))

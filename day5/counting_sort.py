def counting_sort(arr):
    arr_size = len(arr)
    output = [0] * arr_size

    # intialize count array
    count = [0] * 10

    for i in range(0, arr_size):
        count[arr[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = arr_size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, arr_size):
        arr[i] = output[i]

    return output


if __name__ == "__main__":
    arr = [4, 5, 5, 7, 1, 8, 1, 4]
    print(counting_sort(arr))

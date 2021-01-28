def sort_bubble(arr):

    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                # print(arr[j], arr[i])
                continue
            elif arr[j] > arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            # print(arr[i], arr[j])
    return arr


if __name__ == "__main__":
    arr = [1, 5, 8, 9, 3, 0]
    # arr = [1, 2, 3, 4]
    print(sort_bubble(arr))

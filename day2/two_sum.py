def two_sum(ls, target):
    for i in range(len(ls)):
        for j in range(i):
            total = ls[i] + ls[j]
            if total == target:
                return [j, i]
    return None


if __name__ == "__main__":

    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
    print(two_sum([2, 5, 5, 11], 10))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([1, 3, 4, 2], 6))

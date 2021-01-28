def select(seq, start):
    min_index = start

    for i in range(start + 1, len(seq)):
        if seq[min_index] > seq[i]:
            min_index = i
    return min_index


def sort_select(seq):
    for i in range(len(seq) - 1):
        min_index = select(seq, i)
        temp = seq[i]
        seq[i] = seq[min_index]
        seq[min_index] = temp
    return seq


if __name__ == "__main__":
    array = [5, 7, 6, 2, 1]
    print(sort_select(array))

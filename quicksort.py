# Hoare partition
def swap(data_list, si, ei):
    if si != ei:
        tmp = data_list[si]
        data_list[si] = data_list[ei]
        data_list[ei] = tmp


def partition(data_list, start, end):
    pi = start
    pivot = data_list[pi]

    while start < end:

        while start < len(data_list) and data_list[start] <= pivot:
            start += 1

        while end >= 0 and data_list[end] > pivot:
            end -= 1

        if start < end:
            swap(data_list, start, end)

    swap(data_list, pi, end)
    return end



def quicksort(data_list, si, ei):
    if si < ei:
        pi = partition(data_list, si, ei)
        quicksort(data_list, si, pi-1)
        quicksort(data_list, pi+1, ei)





if __name__ == '__main__':
    # dl = [11,9,29,7,2,15,28]
    # dl = [2, 7, 9, 11, 15, 28, 29]
    # dl = [29,28,15,11,9,7,2]
    # dl = []
    # dl = [0]
    dl = ['sim', 'ks', 'yunus', 'upendra']
    quicksort(dl, 0, len(dl)-1)
    print(dl)
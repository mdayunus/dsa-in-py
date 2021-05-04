# Lomuto partition
# pivot = last element
# pindex = i = 0 in the start
# move pindex,i to right untill you find value > pivot
# move i to right untill you find value < pivot
#swap value at pindex and i 
# continue
def swap(data_list, start, end):
    if start != end:
        tmp = data_list[start]
        data_list[start] = data_list[end]
        data_list[end] = tmp


def partition(data_list, start, end):
    pivot = data_list[end]
    pindex = start
    i = start
    first_run = True
    while pindex < end or i < end:
        while data_list[pindex] < pivot:
            if first_run:
                pindex += 1
                i += 1
            else:
                pindex += 1

        while data_list[i] >= pivot and i < end: 
            first_run = False
            i += 1

        if (data_list[i] < data_list[pindex]):
            swap(data_list, pindex, i)

    return pindex


def quicksort(data_list, start, end):
    if start < end:
        pindex = partition(data_list, start, end)
        quicksort(data_list, start, pindex-1)
        quicksort(data_list, pindex+1, end)



if __name__ == '__main__':
    dl = [11,9,29,7,2,15,29]
    quicksort(dl, 0, len(dl)-1)
    print(dl)
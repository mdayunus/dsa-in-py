def bubble_sort(data_list):
    size = len(data_list)
    swapped = False
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if data_list[j] > data_list[j+1]:
                temp = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = temp
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':

    dl = [5,9,2,1,67,34,88,34]
    print(dl)
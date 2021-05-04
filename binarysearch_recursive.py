def binary_search(data_list, data, start, end):
    if start <= end:
        num = (start + end) / 2
        if data == data_list[num]:
            return num
        elif data < data_list[num]:
            return binary_search(data_list, data, start, end-1)
        elif data > data_list[num]:
            return binary_search(data_list, data, start+1, end)
    return -1


dl = [1,2,3,4,5,6,7,8]
d = 6
print(binary_search(dl, d, len(dl)-1, 0))
    
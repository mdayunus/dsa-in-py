def mergesort(data_list):
    if len(data_list) <= 1:
        return data_list
    
    mid = len(data_list) // 2
    left = data_list[:mid]
    right = data_list[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge_two_array(left, right)

def merge_two_array(a1,a2):
    sortedList = []
    a1size = len(a1)
    a2size = len(a2)
    i=j=0

    while i < a1size and j < a2size:
        if a1[i] < a2[j]:
            sortedList.append(a1[i])
            i+=1
        else:
            sortedList.append(a2[j])
            j+=1 
    while i < a1size:
        sortedList.append(a1[i])
        i+=1
    while j < a2size:
        sortedList.append(a2[j])
        j+=1
    return sortedList


if __name__ == '__main__':
    data_list = [11,9,29,27,2,15,28]
    print(mergesort(data_list))
    
    # a1 = [5,8,12,56,89,100]
    # a2 = [7,9,45,51]
    # print(merge_two_array(a1, a2))

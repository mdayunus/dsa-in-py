def insertionsort(data_list):
    for j in range(1,len(data_list)):
        while j > 0 and data_list[j] < data_list[j-1]:
            tmp = data_list[j]
            data_list[j] = data_list[j-1]
            data_list[j-1] = tmp
            j = j - 1
        
        

if __name__ == '__main__':
    data_list = [11,9,29,27,2,15,28]
    insertionsort(data_list)
    print(data_list)
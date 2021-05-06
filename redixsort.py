def redix(inpArr):
    len_max_elem = len(str(max(inpArr)))
    arr = [[] for _ in range(9)]
    arr.insert(0,inpArr)
    modBy = 10
    divBy = 1

    for _ in range(len_max_elem):
        modBy = modBy * 10
        divBy = divBy * 10
        otptArr = [[] for _ in range(10)]

        for elems in arr:
            for elem in elems:
                v = elem % modBy
                v = v / divBy
                if otptArr[v] == None:
                    otptArr[v] = [elem]
                else:
                    otptArr[v].append(elem)
        arr = otptArr

    return otptArr[0]


if __name__ == '__main__':
    arr = [647, 654, 426, 476, 886, 893, 895, 853, 190, 535]
    ans = redix(arr)
    print(ans)

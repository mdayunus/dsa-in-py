def mergesort(dl):

    if len(dl) <= 1:
        return dl

    mid = len(dl) // 2
    left = dl[:mid]
    right = dl[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)





def merge(ldl,rdl):
    sortedArr = []
    sizeldl = len(ldl)
    sizerdl = len(rdl)
    i=j=0
    while i < sizeldl and j < sizerdl:
        if ldl[i] < rdl[j]:
            sortedArr.append(ldl[i])
            i+=1
        else:
            sortedArr.append(rdl[j])
            j+=1
    while i < sizeldl:
        sortedArr.append(ldl[i])
        i+=1
    while j < sizerdl:
        sortedArr.append(rdl[j])
        j+=1
    return sortedArr

if __name__ == '__main__':
    dl = [11,9,29,7,2,15,28]
    x = mergesort(dl)
    print(x)

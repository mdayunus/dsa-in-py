def shellsort(dl):
    size = len(dl)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            while i >= gap and dl[i-gap] > dl[i]:
                tmp = dl[i]
                dl[i] = dl[i-gap]
                dl[i-gap] = tmp
                i -= gap
        
        gap = gap // 2

if __name__ == '__main__':
    dl = [11,9,29,7,2,15,28]
    shellsort(dl)
    print(dl)
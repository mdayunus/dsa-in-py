def shellsort(dl):
    gap = len(dl) // 2
    size = len(dl)
    while gap > 0:
        x = [d for d in range(gap,size)]
        print(x)
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

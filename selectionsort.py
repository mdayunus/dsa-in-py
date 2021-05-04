def selectionsort(dl):
    for i in range(len(dl)):
        mi = i
        for j in range(i, len(dl)):
            if dl[j] < dl[mi]:
                mi = j

        tmp = dl[mi]
        dl[mi] = dl[i]
        dl[i] = tmp

if __name__ == '__main__':
    dl = [11,9,29,7,2,15,28]
    selectionsort(dl)
    print(dl)
def binary_search(dl, d):
    start = 0
    end = len(dl) - 1
    while start <= end:
        mid = (start + end) // 2
        if dl[mid] == d:
            return mid
        if d < dl[mid]:
            end = mid-1
        if d > dl[mid]:
            start = mid+1
    return -1

if __name__ == '__main__':
    dl = [1,2,3,4,5,6,7,8]
    d = 0
    print(binary_search(dl, d))

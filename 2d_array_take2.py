def simple(a):
    maxi = 0
    for i in range(1,5):
        for j in range(1,5):
            insum = a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i][j]+a[i+1][j-1]+a[i+1][j]+a[i+1][j+1]
            if insum > maxi:
                maxi = insum
    return maxi



if __name__ == '__main__':
    a = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    print(simple(a))
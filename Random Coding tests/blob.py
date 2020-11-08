arr = [
    "0 0 0 0 0 0 0 0 0 0",
    "0 0 1 1 1 0 0 0 0 0",
    "0 0 1 1 1 1 1 0 1 0",
    "0 0 1 0 0 0 1 0 0 0",
    "0 0 1 1 1 1 1 0 0 0",
    "0 0 0 0 1 0 1 0 0 0",
    "0 0 0 0 1 0 1 0 0 0",
    "0 0 0 0 1 1 1 0 0 0",
    "0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0 0"]
arr = [line.split(" ") for line in arr]
row = 10
col = 10


def blob(arr, row, col):
    top, left, right, bottom = 0, 0, row-1, col-1
    count = 0
    for i in range(top,bottom+1):
        for j in range(left,right+1):
            count += 1
            if arr[i][j] == '1':
                top = i
                break
        if arr[i][j] == '1':
            break
    for j in range(left,right+1):
        for i in range(top,bottom+1):
            count += 1
            if arr[i][j] == '1':
                left = j
                break
        if arr[i][j] == '1':
            break
    for i in range(bottom,top,-1):
        for j in range(right, left-1, -1):
            count += 1
            if arr[i][j] == '1':
                bottom = i
                break
        if arr[i][j] == '1':
            break
    for j in range(right, left-1, -1):
        for i in range(bottom,top, -1):
            count += 1
            if arr[i][j] == '1':
                right = j
                break
        if arr[i][j] == '1':
            break
    print("Cell Reads:", count)
    print("Top:", top)
    print("Left:", left)
    print("Right:", right)
    print("Bottom:", bottom)


blob(arr, row, col)

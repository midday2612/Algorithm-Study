n = int(input())
max_x = 9
max_y = 9
arr = []

for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y, 1])

for i in range(n):
    for j in range(n):
        if (arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]):
            arr[i][2] += 1

for i in range(n):
    print(arr[i][2], end = ' ')
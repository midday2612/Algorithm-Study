N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr = [int(i) for i in arr]
arr.sort(reverse = True)

count = 0
sum = 0
first = arr[0]
second = arr[1]

while(True):
    for i in range(K):
        if (count == M): break
        sum += first
        count += 1
    if (count == M): break
    sum += second
    count += 1

print(sum)

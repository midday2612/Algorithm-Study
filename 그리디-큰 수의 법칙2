N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr = [int(i) for i in arr]
arr.sort(reverse = True)

sum = 0
first = arr[0]
second = arr[1]

first_count = int(M / (K + 1)) * K
first_count += M % (K + 1)

sum += first_count * first
sum += (M - first_count) * second

print(sum)

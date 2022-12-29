dx = [1, -1 , 1, -1]
dy = [1, -1, -1, 1]
data = input()

x = int(ord(data[0]))-int(ord('a'))+1
y = int(data[1])

count = 0

for i in range(4):
    nx = int(x) + dx[i]*2
    ny = y + dy[i]
    if (nx>=1 and nx<=8 and ny>=1 and ny<=8):
        count += 1

for i in range(4):
    nx = int(x) + dx[i]
    ny = y + dy[i]*2
    if (nx>=1 and nx<=8 and ny>=1 and ny<=8):
        count += 1


print(count)

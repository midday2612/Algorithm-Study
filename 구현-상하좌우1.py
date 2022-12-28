def lrud(a, n):
    global x, y
    if (a == 'L' and y > 1):
        y -=1
    elif (a == 'R' and y < n):
        y +=1
    elif(a == 'U' and x > 1):
        x -= 1
    elif (a == 'D' and x < n):
        x += 1

n = int(input())
cmd = input().split()

x = 1
y = 1

for w in cmd:
    lrud(w, n)

print(x, y)

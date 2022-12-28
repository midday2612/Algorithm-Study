n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for z in range(60):
            h, m, s = i, j, z
            result = str(i)+str(j)+str(z)
            if ('3'in result): count+=1
print(count)

n=int(input())
for i in range(1,n+1):
    str1 =' '*(n-i)
    for j in range(1,2*i):
            if j < i+1:
                str1 = str1 + str(j)
            else:
                str1 = str1 + str(2*i-j)
    str1 = str1 + ' '*(n-i)
    print(str1)
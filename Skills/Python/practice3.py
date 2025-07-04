num= int(input('Enter the length of binary string:'))
def binary(n):
    ans=[]
    if n==1:
        return ['0','1']
    for i in binary(n-1):
        str='0'+i
        if str not in ans :
            ans.append(str)
        str='1'+i
        if str not in ans:
            ans.append(str)
    return ans
for i in binary(num):
    print(i)
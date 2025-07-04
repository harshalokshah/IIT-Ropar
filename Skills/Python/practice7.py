s=input('Enter the string:')
def permute (s):
    for i in range(len(s)):
        x=s[:i]+s[i+1:] + s[i]
        if x not in lst:
            lst.append(x)
            permute(x)
lst=[]
permute(s)
print(lst)       
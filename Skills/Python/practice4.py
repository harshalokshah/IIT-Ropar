str1=input('enter the string: ').lower()
lowest=len(str1)
for i in str1:
    str2=str1.replace(i,'')
    count=len(str1)-len(str2)
    if count<lowest:
        lowest=count
def first(lowest,str1):
    for i in str1:
        str2=str1.replace(i,'')
        count=len(str1)-len(str2)
        if count==lowest:
            return i
print(first(lowest,str1))
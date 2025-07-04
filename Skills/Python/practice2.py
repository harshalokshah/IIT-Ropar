n= int(input('Enter a number of students: '))
hgrade=0
num=0
student_data={}
while num<n:
    num+=1
    name = input('Enter the name of student'+str(num)+' :')
    age = int(input('Enter the age of student'+ str(num)+' :'))
    grade= float(input('Enter the grade of student'+str(num)+' :'))
    student_data[name]={'age':age,'grade':grade}
    if grade> hgrade:
        hgrade=grade
        topper=name
    else:
        continue
print(student_data)
print('The student with higest grade is:',topper)
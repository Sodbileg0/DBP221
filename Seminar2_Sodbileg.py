
#Problem1
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("Palindrome тоо байна.")
else:
    print("Palindrome тоо биш.")
#Problem2
a=input()
def problem2(word):
    count = 0
    for i in word:
        if i.isupper():
            count += 1
    return count
def y(word2):
    count1 = 0
    for i in word2:
        if i.islower():
            count1 += 1
    return count1
count1 =y(a)
count = problem2(a)
print('uppercase',count)
print('lowercase',count1)
#Problem3
print('хэдэн утгатай лист вэ?', )
n=int(input())
b=[]
for i in range(0,n):
    a=int(input())
    b.append(a)
print('Таны лист',b)
def multiplication(x):
    c=1
    for i in x:
        c=c*i
    return c
print('листний үржвэр',multiplication(b))
#Problem4
k = int(input())
def factorial(x):
    c=1
    for i in range(1,x+1):
        c=c*i
    return c
print('Factorial утга',factorial(k))
#Problem5
print('Хэдэн утгатай лист вэ', )
n=int(input())
b=[]
print('Тоогоо оруулна уу')
for i in range(0,n):
    a=int(input())
    b.append(a)
print(b)
b.reverse()
print(b)
#Problem6
print('Хэдэн утгатай лист вэ', )
n=int(input())
b=[]
for i in range(0,n):
    a=int(input())
    b.append(a)
l=0
for i in b:
    l = l+i
print('sum=',l)
#Problem7
j=[]
n = int(input('Хэдэн утгатай лист вэ-'))
for i in range(0,n):
    b=input()
    j.append(b)
print(j)
a=set(j)
print('Давхардаагүй утгууд',a)
#Problem8
a=int(input())
b=int(input())
c=int(input())
l=[a,b,c]
print('max value=',max(l))
#DBP221 Seminar_1

#Problem 1
l = ['python','php','java']
print(l)

#Problem 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total=0
for i in numbers:
    total= total + i
    
print(total)
#Problem 3
n=[2, 3, 4, 6]
def p3(l):
    mult=1
    for i in l:
        mult=mult * i
    print(mult)
print(p3(n))

#Problem 4
def multiply(l):
    mult1=1
    for a in l:
        mult1=mult1 * l[2] * l[-1]
        return mult1
print(multiply(numbers))
print(multiply(n))

#Problem 5
def min_max(l):
    print("list-ийн хамгийн бага утга", min(l))
    print("list-ийн хамгийн их утга", max(l))

print(min_max(n))
print(min_max(numbers))

# Problem 6

#Problem 7
def p7(l):
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)
        elif i in new_list:
            r = new_list.count(i)
            if r < 1:
                new_list.append(i)

    print(new_list)
newlist=[1, 1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 'abd', 'abd']
print(p7(newlist))

# Problem 8
def p8(l):
    if len(l)==0:
        print('Hooson baina')
    else:
        print('Hooson bish')
nnn=[]
print(p8(n))
print(p8(nnn))

#Problem 9
def p9(l):
    l.pop(3)
    l.pop(4)
    l.pop(5)
    return l
print(p9(numbers))

#Problem 10
x=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(x)

#Problem 11
y=list(x)
y.append(11)
x=tuple(y)
print(x)

#Problem 12
print(x[1])
print(x[-2])

#Problem 13


#Problem 14
for i in x:
    print(i)

#Problem 15
fruits = {'orange', 'apple', 'pear', 'tomato'}
veggie = {'tomato', 'potato', 'carrots', 'broccolli'}
Newset = fruits.union(veggie)
print(Newset)

#Problem 16
Newset2 = fruits.intersection(veggie)
print(Newset2)

#Problem 17
print(len(Newset))

#Problem 18
Newset.remove('apple')
print(Newset)

#Problem 19
Newset.clear()
print(Newset)

#Problem 20
del Newset

#Problem 21
dict = {1:7, 2:3, 3:4, 4:10, 5:6, 6:2}

#Problem 22

def p22(l):
    if i in l:
        print('Baina.')
    else:
        print('Baihgui baina.')
print(p22(dict))
#Problem 23
i = 3
if i in dict:
    print("Value dict- байна.")
else:
    print("Value dict-д байхгүй байна.")
#Problem 24
for x in dict:
    print(x)

# Problem 25
a = {1:2, 2:3, 3:4, 4:5, 5:6}
b = {6:7, 7:8, 8:9, 9:10}
def p25(a, b):
    c = a.copy()
    c.update(b)
    return c
print(p25(a, b))
    
#Problem 26
values = dict.values()

total = sum(values)
print(total)
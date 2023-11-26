tup = (6 , 2 , 7 , 8)
for i in range(2 , 8 , 1):
    s = 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            s += j
    if s == i:
        print(i)
#
tup = (5 , 2 , -2 , 7 , -8 , -9 , 1)
counter = 0
minus = tup[0] < 0
for i in range(1 , len(tup[1:])+1):
    if (tup[i] < 0) != minus:
        counter += 1
    minus = tup[i] < 0
print(counter)
#
list1 = [4, 1, 6, 9]
list2 = [8, 1, 2, 4, 9, 5, 7, 6]
list3 = list()
for num in list1:
    if num not in list2:
        list3.append(num)
        print(min(list3))
else:
    print("нет такого элемента")
#
nums = [18 , 42 , 8 , 122]
for x in nums:
    y = str(x)[::-1]
    print(x , '->' , y)
    x+=1
#
list=[5,2,4,5,1,2]
list2 = set(list)
counter = 0
for n in list2:
    counter = list.count(n)
    print(n , counter)
#
list=[7,4,1]
list2=[]
for n in list:
    list2.append(n)
    list2.append(0)
print(list2)
#
str1='9 5 1 7 3 2 6 1 9'
str2=set()
digits = str1.split()
for n in digits:
    if n in str2:
        print("YES")
    else:
        str2.add(n)
        print("NO")
#
dic = {'big':'huge','high':'tall','small':'tiny' , 'short':'low' , 'handsome':'pretty'}
word = input('write a word: ')
if word in dic:
    syn = dic[word]
    print('syn', word , syn)
else:
    print('no syn')
#

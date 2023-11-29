a = 5
b = -1
c = 2
result = 'true' if a < 0 or b < 0 or c < 0 else 'false'
print(result)
# #
num1 = int(input('введите число:'))
num2 = int(input('введите число2:'))
if (num1 % 2) == 0 and (num2 % 2) == 0:
      result = num1 == num2 or num1 != num2
print(result)
#
a = 7
b = 2
c = 4
sum = (a % 2 == 0 ) + (b % 2 == 0 ) + (c % 2 == 0 )
print(sum)
#
num1 = 85
if num1 >= 10:
     print('Да')
else:
     print('Нет')
#
# n1 = 10
# while n1 <=20:
#      print(n1)
#      n1 +=0
#
x = 5
for y in range(1 , 6 , 1):
     print(y**3)
#
x = 1
for i in range(5 , 21):
     x *= i
     print(x)
#
x = 15
for y in range (1 , x + 1):
     if y**2 <= 15:
          print(y**2)
#
n = 123456789
n = str(n)
n_low = n.index(min(n))
print('мин значение-', n[n_low])
#
ny = int(input('Напишите год - '))
if ny % 4 == 0 and ny % 100 != 0 or ny % 400 == 0:
     print('высокосный год')
else:
     print('не высоскосный год')
#
x = 7
for i in range (1 , x + 1):
     if i == 1:
          print('на лугу' , i , 'корова')
     elif 2 <= i <= 4:
              print ('на лугу' , i , 'коровы')
     else:
          print('на лугу' , i , 'коров')
#
n = 8
f1 = f2 = 1
print(f1, f2, end=' ')
for i in range(2, n):
     f1, f2 = f2, f1 + f2
     print(f2, end=' ')
#
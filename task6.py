print([x ** 2 for x in range(1, 11)])
#
print([x for x in range(100, 1000) if not x % 3 and not x % 5])

#
def numbs(a , b):
    return(min(a , b))
finish = numbs(numbs(11 , 21 ,),numbs(51, 5))
print(finish)
#
def fib(n):
    numb1 = numb2 = 1
    for i in range(2, n):
          numb1, numb2 = numb2, numb1 + numb2
    print(numb2)
#
def closet_mod_5(x):
    if x % 5 == 0:
        return
    else:
        return (x//5+1)*5
print(closet_mod_5(1))
#
def modify_list(lst):
    lst = [i // 2 for i in lst if i % 2 == 0]
modify_list([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10])
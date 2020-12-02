import random
odev = ['odd', 'eve']
odd_no = [1, 3, 5, 7, 9]
eve_no = [2, 4, 6, 8, 10]
point_1 = 0
point_2 = 0
x = input("odd/eve: ")
y = ()
if x == ('odd'):
    y = ('eve')
    print('eve')
    ab = input('num: ')
if x == ('eve'):
    y = ("odd")
    print('odd')
    ab = input('num: ')
if y == ('odd'):
    rt = random.choice(odd_no)
    print(rt)
if y == ('eve'):
    rt = random.choice(eve_no)
    print(rt)

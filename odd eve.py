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
num = int(input("what will be the total,please sach bolna: "))
if (num % 2) == 0 and  x == ('odd'):
   print("{0} is Even".format(num))
   print('I chose to ball')
   y = ('ball')
else:
   print("{0} is Odd".format(num))
   print('what do you choose')
   choice = input('bat/ball: ')
   if choice == ('bat'):
       print('ball')
       y = 'ball'
   else:
       print('please take bat,your is bat')
while True:
        ccs = int(input('number: '))
        while point_1 > 19999999999:
            ccs = point_1+ccs
            break
        rs = random.randint(0,10)
        print(ccs)
        if ccs == rs:
            print('you are out')
            break
        
ol = int(input("What's the target? "))
while point_2 < ol:
    sst = input('enter num: ')
    ost = random.randint(0,11)
    point_2 = point_2 + ost
    print(point_2)
    if ost == sst:
        print('out')
        break
    if point_2 > ol:
        print('ya I won')
        break
    print('lol')

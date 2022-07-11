"""
# Iterative statement
# for loop
# patterns: star, numbers, alphabets
================================================
# Que. WAP to print given alphabet patterns
==================================================
A
BB
CCC
DDDD
EEEEE

for i in range (1, 6):
    print(chr( i + 64)* i)
========================================

EEEEE
DDDD
CCC
BB
A

for i in range (5,0,-1):
    print(chr(i + 64)* i)
===========================================

AAAAA
BBBB
CCC
DD
E

for i in range (5,0,-1):
    print(chr(70-i)* i)

or
for i in range (1,6):
    print(chr(i+ 64)*(6-i))
=======================================

E
DD
CCC
BBBB
AAAAA

for i in range (1,6):
    print(chr(70-i)* i)

or
for i in range (5,0,-1):
    print(chr(i+ 64)*(6-i))
==================================

A
A B
A B C
A B C D
A B C D E

for i in range (1,6):
    x = 65
    for j in range(1, i+1):
        print(chr(x), end= ' ')
        x += 1
    print()
======================================

        A
      A B
    A B C
  A B C D
A B C D E

for i in range (1 ,6):
    for k in range(1, 6 - i):
        print(' ', end=' ')
    x = 65
    for j in range(1, i+1):
        print(chr(x), end= ' ')
        x += 1
    print()
============================================

A B C D E
A B C D
A B C
A B
A

for i in range (5 , 0, -1):
    x = 65
    for j in range(1, i+1):
        print(chr(x), end= ' ')
        x += 1
    print()
===========================================

A B C D E
  A B C D
    A B C
      A B
        A

for i in range (5 ,0 ,-1):
    for k in range(1, 6 - i):
        print(' ', end=' ')
    x = 65
    for j in range(1, i+1):
        print(chr(x), end= ' ')
        x += 1
    print()
============================================

E
E D
E D C
E D C B
E D C B A

for i in range (1, 6):
    x = 69
    for j in range(1, i+1):
        print(chr(x), end= ' ')
        x -= 1
    print()
===========================================

        E
      E D
    E D C
  E D C B
E D C B A

for i in range (1, 6):
    for k in range(1, 6 - i):
        print(' ', end=' ')
    x = 69
    for j in range(1, i+1):
        print(chr(x), end= ' ')
        x -= 1
    print()
=======================================

E D C B A
E D C B
E D C
E D
E

for i in range (5 , 0, -1):
    x = 69
    for j in range(1, i+1):
        print(chr(x), end= ' ')
        x -= 1
    print()
========================================

E D C B A
  E D C B
    E D C
      E D
        E

for i in range (5 ,0 ,-1):
    for k in range(1, 6 - i):
        print(' ', end=' ')
    x = 69
    for j in range(1, i+1):
        print(chr(x), end= ' ')
        x -= 1
    print()
==============================================

equilateral triangle pyramid of alphabets:
            A
           B C
          D E F
         G H I J
        K L M N O
       P Q R S T U
      V W X Y Z [ \

print('equilateral triangle pyramid of alphabets: ')
s = 7
x = 65
m = (2 * s) - 2
for i in range(0, 7):
    for j in range(0, m):
        print(end='')
    m -= 1
    for k in range(0, i+1):
        print(chr(x), end=' ')
        x += 1
    print()
==============================================================
"""

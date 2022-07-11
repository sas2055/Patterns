"""
# Iterative statement
# while loop
# patterns: star, numbers, alphabets
========================================
# Que. WAP to print given alphabet patterns
=======================================

A
B B
C C C
D D D D
E E E E E

x = 65
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(chr(x) , end= ' ')
        j = j + 1
    i += 1
    print()
    x += 1
========================================

E E E E E
D D D D
C C C
B B
A

x = 69
i = 1
while i <= 5:
    j = 5
    while j >= i:
        print(chr(x) , end= ' ')
        j = j - 1
    i += 1
    print()
    x -= 1
=======================================

A A A A A
 B B B B
  C C C
   D D
    E

i = 0
j = 6
while i < 5:
    print(' ' * i + (chr(65 + i)+ ' ')* ((j * 1)-1))
    j -= 1
    i += 1
==============================================

E E E E E
 D D D D
  C C C
   B B
    A

i = 0
j = 6
while i < 5:
    print(' ' * i + (chr(69 - i)+ ' ')* ((j * 1)-1))
    j -= 1
    i += 1
=================================================

"""
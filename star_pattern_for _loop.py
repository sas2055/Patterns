"""
# Iterative statement
# for loop
# patterns: star, numbers, alphabets
========================================
# Que. WAP to print the given star patterns
========================================

*
* *
* * *
* * * *
* * * * *

for i in range (1,6):
    print(i* '* ')

or
for i in range (0,5):
    for j in range(0, i+ 1):
        print('*', end= ' ')
    print()
========================================

* * * * *
* * * *
* * *
* *
*

for i in range (6,0,-1):
    print(i* '* ')
======================================

        *
      * *
    * * *
  * * * *
* * * * *

for i in range (1,6):
    for k in range(1, 6-i):
        print(' ', end= ' ')
    for j in range(1, i+ 1):
       print('*', end= ' ')
    print()
========================================

* * * * *
  * * * *
    * * *
      * *
        *

for i in range (5,0,-1):
    for k in range(1, 6-i):
        print(' ', end= ' ')
    for j in range(1, i+ 1):
       print('*', end= ' ')
    print()
=========================================

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

for i in range (1,6):
    for k in range(1, 6-i):
        print(' ', end= ' ')
    for j in range(1,(2* i- 1)+ 1):
       print('*', end= ' ')
    print()
=====================================

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

for i in range (5,0,-1):
    for k in range(1, 6 - i):
        print(' ', end= ' ')
    for j in range(1,(2* i- 1)+ 1):
       print('*', end= ' ')
    print()
======================================


"""

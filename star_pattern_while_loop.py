"""
# Iterative statement
# while loop
# patterns: star, numbers, alphabets
========================================
# Que. WAP to print the given star patterns
========================================

*
* *
* * *
* * * *
* * * * *

num = int(input('enter the number of rows: '))
i = 1
while i <= num:
    print(i* '*' , end= ' ')
    print()
    i += 1

or
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*' , end= ' ')
        j = j + 1
    print()
    i += 1
========================================

* * * * *
* * * *
* * *
* *
*

i = 1
while i <= 5:
    j = 5
    while j >= i:
        print('*' , end= ' ')
        j = j - 1
    print()
    i += 1
======================================

        *
      * *
    * * *
  * * * *
* * * * *

i = 0
while i < 5:
    k = (5 - 1) - i
    while (k > 0):
        print(' ', end= ' ')
        k = k - 1
    j = i + 1
    while j > 0:
        print('*' , end= ' ')
        j = j - 1
    i = i + 1
    print()
=====================================

    *
   * *
  * * *
 * * * *
* * * * *

i = 1
while i <= 5:
    j = 1
    while (j <= 5 - i):
        print(' ', end= '')
        j = j + 1
    k = 1
    while k <= i:
        print('*' , end= ' ')
        k = k + 1
    print()
    i += 1
======================================

* * * * *
 * * * *
  * * *
   * *
    *

i = 5
while i >= 1:
    j = 1
    while (j <= 5 - i):
        print(' ', end= '')
        j = j + 1
    k = 1
    while k <= i:
        print('*' , end= ' ')
        k = k + 1
    print()
    i -= 1
===================================================
"""

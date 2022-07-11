"""
# Iterative statement
# while loop
# patterns: star, numbers, alphabets
========================================
# Que. WAP to print given number patterns
=======================================

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j , end= ' ')
        j = j + 1
    print()
    i += 1
=======================================

        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1

i = 1
while i < 6:
    k = (6 - 1) - i
    while (k > 0):
        print(' ', end= ' ')
        k = k - 1
    j = i
    while j > 0:
        print(j , end= ' ')
        j = j - 1
    i = i + 1
    print()
========================================

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

i = 1
while i < 6:
    k = 6 - i
    while (k > 0):
        print(k, end= ' ')
        k = k - 1
    j = i + 1
    while j > 0:
        print(' ' , end= ' ')
        j = j - 1
    i = i + 1
    print()
=========================================

    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

i = 1
while i <= 5:
    j = 1
    while (j <= 5 - i):
        print(' ', end= '')
        j = j + 1
    k = 1
    while k <= i:
        print(k , end= ' ')
        k = k + 1
    print()
    i += 1
=========================================

5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

i = 1
while i <= 5:
    j = 5
    while j >= i:
        print(j , end= ' ')
        j = j - 1
    print()
    i += 1
=========================================

        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9

i = 0
while i < 5:
    print('  ' * (4 - i), end= '')
    j = 0
    while (j - 1) < (i * 2):
        print(j + 1, end= ' ')
        j = j + 1
    print()
    i += 1
========================================

1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1

n = 5
i = 1
while n > 0:
    j = 1
    while j < i:
        print(' ', end= ' ')
        j = j + 1
    k = 1
    while (k <= (n*2) -1):
        print(k, end= ' ')
        k = k + 1
    print()
    n -= 1
    i += 1
========================================

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(i , end= ' ')
        j = j + 1
    print()
    i += 1
=========================================

        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5

i = 1
while i < 6:
    k = (6 - 1) - i
    while (k > 0):
        print(' ', end= ' ')
        k = k - 1
    j = i
    while j > 0:
        print(i , end= ' ')
        j = j - 1
    i = i + 1
    print()
=======================================

    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5

i = 1
while i <= 5:
    j = 1
    while (j <= 5 - i):
        print(' ', end= '')
        j = j + 1
    k = 1
    while k <= i:
        print(i , end= ' ')
        k = k + 1
    print()
    i += 1
========================================

    5
   4 4
  3 3 3
 2 2 2 2
1 1 1 1 1

i = 1
while i <= 5:
    j = 1
    while (j <= 5 - i):
        print(' ', end= '')
        j = j + 1
    k = 1
    while k <= i:
        print(j , end= ' ')
        k = k + 1
    print()
    i += 1
========================================

1 1 1 1 1
2 2 2 2
3 3 3
4 4
5

i = 1
while i <= 5:
    j = 5
    while j >= i:
        print(i , end= ' ')
        j = j - 1
    print()
    i += 1
=========================================

5
4 4
3 3 3
2 2 2 2
1 1 1 1 1

i = 1
while i <= 5:
    j = 1
    while (j <= 5 - i):
        print('', end= '')
        j = j + 1
    k = 1
    while k <= i:
        print(j , end= ' ')
        k = k + 1
    print()
    i += 1
=========================================

        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5

i = 1
k = 1
while i <= 5:
    b = 1
    while b <= 5 - i:
        print(' ', end= ' ')
        b = b + 1
    j = 1
    while j <= k:
        print(i, end= ' ')
        j = j + 1
    k = k +2
    print()
    i += 1
========================================

1 1 1 1 1 1 1 1 1
  2 2 2 2 2 2 2
    3 3 3 3 3
      4 4 4
        5

n = 5
i = 1
while n > 0:
    j = 1
    while j < i:
        print(' ', end= ' ')
        j = j + 1
    k = 1
    while (k <= (n*2) -1):
        print(i, end= ' ')
        k = k + 1
    print()
    n -= 1
    i += 1
=================================================

        5
      4 4 4
    3 3 3 3 3
  2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 1

n = 1
i = 5
while n <= 5:
    j = 1
    while j < i:
        print(' ', end= ' ')
        j = j + 1
    k = 1
    while (k <= (n*2) -1):
        print(i, end= ' ')
        k = k + 1
    print()
    n += 1
    i -= 1
========================================

        1
      3 3 3
    5 5 5 5 5
  7 7 7 7 7 7 7
9 9 9 9 9 9 9 9 9

i = 1
k = 1
while i <= 5:
    b = 1
    while b <= 5 - i:
        print(' ', end= ' ')
        b = b + 1
    j = 1
    while j <= k:
        print(k, end= ' ')
        j = j + 1
    k = k +2
    print()
    i += 1
==========================================

        2
      4 4 4
    6 6 6 6 6
  8 8 8 8 8 8 8
10 10 10 10 10 10 10 10 10

i = 1
k = 1
while i <= 5:
    b = 1
    while b <= 5 - i:
        print(' ', end= ' ')
        b = b + 1
    j = 1
    while j <= k:
        print(i * 2, end= ' ')
        j = j + 1
    k = k + 2
    print()
    i += 1
===============================================

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

x = 1
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(x, end= ' ')
        x += 1
        j += 1
    print()
    i += 1
==================================================
"""

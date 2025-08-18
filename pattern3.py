Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Example: input = 5 → highest letter = 'E'
... 
... n = int(input("Enter number of rows (max letter = A + n - 1): "))
... 
... for i in range(n):
...     # Left side letters from A to (n-i-1)th letter
...     for j in range(n - i):
...         print(chr(65 + j), end=" ")
... 
...     # Spaces in the middle
...     spaces = 2 * i - 1
...     for s in range(spaces):
...         print(" ", end=" ")
... 
...     # Right side letters, skip the center letter in first row
...     for j in range(n - i - 1, -1, -1):
...         if i == 0 and j == n - i - 1:
...             continue
...         print(chr(65 + j), end=" ")
... 

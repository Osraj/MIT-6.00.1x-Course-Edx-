'''
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is:  (0.25∗n∗s**2)/(tan(π/n))
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
'''

import math

def polysum(n, s):
    '''
    :argument1 "n": is the number of sides
    :argument2 "s": is the length of each side
    :return: the sum the area and square of the perimeter of the polygon (rounded to 4 decimal places)
    '''
    area = (0.25 * n * s**2) / (math.tan(math.pi / n) )
    perimeter_of_polysum = (n * s) ** 2
    total = round(area + perimeter_of_polysum, 4)
    return total


# Test Case 1: (6316301.7484)
# print(polysum(41, 59))

# Test Case 2: (112894.017)
# print(polysum(5, 65))

# continued fractions for square roots program
# this program's goal is to print the continued fractions for square roots
# or if the root is a perfect square, to print the corresponding integer

import math
import os


def continued(x):

	cont_frac = ''

	if math.sqrt(x).is_integer():

		cont_frac = f'{x}:'+str(int(math.sqrt(x)))
		return cont_frac




	a = int(math.sqrt(x))

	b = int((math.sqrt(x)+a)/(x-a**2))

	cont_frac = f'{x} : {a} ; {b}'

	if x - a**2 == 1 and a - b * x + b * a**2 == -a:

		return cont_frac

	u = a - b * x + b * a**2

	v = x - a**2

	while v != 1 or u != -a:

		c = int(((math.sqrt(x)-u)/((x-u**2)/v)))

		v = int((x-u**2)/v)

		u = -u - c * v

		cont_frac += f', {c}'

	return cont_frac



print('''This program will do the following: 

	If you enter a perfect square, it will return the square root. 

	If you enter an integer that is not a perfect square,

	it will return the values for the continued fraction of that square root.

	The pattern repeats indefinitely.

	Please enter an integer.''')

c = int(input())

print(continued(c))

# print('Would you like to enter another number? Press Y to continue or N to exit.')

# ans = str(input()).lower

# if ans == 'Y'.lower:

# 	print('Input an integer.')

# 	c = int(input())

# 	print(continued(c))
		







os.system('pause')

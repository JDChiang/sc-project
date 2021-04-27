"""
File: quadratic_solver.py
Name: Frank Chiang
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	The entire main function includes greeting and type the digit sub function.
	The type_the_digit function will constitute solve_the_equation sub function.
	"""
	greeting()
	type_the_digit()


def greeting():
	"""
	This function is for greeting.
	"""
	print('stanCode Quadratic Solver!')


def type_the_digit():
	a = int(input('Enter a: '))
	if a == 0:
		# if we type 0, function will tell us to retype the equation.
		print('Please retype your values')
		type_the_digit()
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	# d stands for the discriminant.
	d = float(b * b - 4 * a * c)
	while True:
		"""
		The following codes will define how the equation will be written.
		Because b and c may be >, ==, <0, we need to double confirm the equation.   
		"""
		if b > 0:
			# under b > 0, we will need to double confirm what c is positive, negative, or zero.
			if c > 0:
				print('Is your equation: ' + str(a) + 'x^2' + '+' + str(b) + 'x' + '+' + str(c) + ' = 0?(Y/N)')
				ans = str(input())
				# If the equation is correct, we type Y and solve the equation.
				if ans == 'Y':
					solve_the_equation(a, b, c, d)
				# If the equation is not correct, this will return to the beginning of the function.
				elif ans == 'N':
					break
				# If we type words other than Y and N, this will return to the beginning of the function.
				else:
					print('Please retype your values.')
					type_the_digit()
			elif c == 0:
				print('Is your equation: ' + str(a) + 'x^2' + '+' + str(b) + 'x' + ' = 0?(Y/N)')
				ans = str(input())
				if ans == 'Y':
					solve_the_equation(a, b, c, d)
				elif ans == 'N':
					break
				else:
					print('Please retype your values.')
					type_the_digit()
			else:
				print('Is your equation: ' + str(a) + 'x^2' + '+' + str(b) + 'x' + str(c) + ' = 0?(Y/N)')
				ans = str(input())
				if ans == 'Y':
					solve_the_equation(a, b, c, d)
				elif ans == 'N':
					break
				else:
					print('Please retype your values.')
					type_the_digit()
		elif b < 0:
			# under b < 0, we will need to double confirm what c is positive, negative, or zero.
			if c > 0:
				print('Is your equation: ' + str(a) + 'x^2' + str(b) + 'x' + '+' + str(c) + ' = 0?(Y/N)')
				ans = str(input())
				if ans == 'Y':
					solve_the_equation(a, b, c, d)
				elif ans == 'N':
					break
				else:
					print('Please retype your values.')
					type_the_digit()
			elif c == 0:
				print('Is your equation: ' + str(a) + 'x^2' + str(b) + 'x' + ' = 0?(Y/N)')
				ans = str(input())
				if ans == 'Y':
					solve_the_equation(a, b, c, d)
				elif ans == 'N':
					break
				else:
					print('Please retype your values.')
					type_the_digit()
			else:
				print('Is your equation: ' + str(a) + 'x^2' + str(b) + 'x' + str(c) + ' = 0?(Y/N)')
				ans = str(input())
				if ans == 'Y':
					solve_the_equation(a, b, c, d)
				elif ans == 'N':
					break
				else:
					print('Please retype your values.')
					type_the_digit()
		else:
			# under b == 0, we will need to double confirm what c is positive, negative, or zero.
			if c > 0:
				print('Is your equation: ' + str(a) + 'x^2' + '+' + str(c) + ' = 0?(Y/N)')
				ans = str(input())
				if ans == 'Y':
					solve_the_equation(a, b, c, d)
				elif ans == 'N':
					break
				else:
					print('Please retype your values.')
					type_the_digit()
			elif c == 0:
				print('Is your equation: ' + str(a) + 'x^2' + ' = 0?(Y/N)')
				ans = str(input())
				if ans == 'Y':
					solve_the_equation(a, b, c, d)
				elif ans == 'N':
					break
				else:
					print('Please retype your values.')
					type_the_digit()
			else:
				print('Is your equation: ' + str(a) + 'x^2' + str(c) + ' = 0?(Y/N)')
				ans = str(input())
				if ans == 'Y':
					solve_the_equation(a, b, c, d)
				elif ans == 'N':
					break
				else:
					print('Please retype your values.')
					type_the_digit()
	print('Please retype your values.')
	type_the_digit()


def solve_the_equation(a, b, c, d):
	"""
	This function is for solving the equation, using discriminant to define
	whether the equation having real roots or not.
	"""
	if d > 0:
		# If the discriminant > 0, the equation will have two real roots.
		x1 = float((-b + math.sqrt(d)) / 2 * a)
		x2 = float((-b - math.sqrt(d)) / 2 * a)
		print('Two roots:' + str(x1) + ',' + str(x2))
		type_the_digit()
	elif d == 0:
		# If the discriminant == 0, the equation will have one real root.
		x = float((-b + math.sqrt(d)) / 2 * a)
		print('One root:' + str(x))
		type_the_digit()
	else:
		# If the discriminant < 0, the equation will have no roots.
		print('No real roots')
		type_the_digit()


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()

"""
File: largest_digit.py
Name: Jo-Di(Frank), Chiang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the digit that we want to find the
	:return: answer of each helper_function
	"""
	return get_helper(abs(n), 0)


def get_helper(n, max_digit):
	"""
	:param n: int, current number
	:param max_digit: int, current max digit
	:return: int, answer of helper function
	"""
	if n % 10 > max_digit:
		max_digit = n % 10
	if n//10 == 0:
		return max_digit
	else:
		return get_helper(n//10, max_digit)



if __name__ == '__main__':
	main()

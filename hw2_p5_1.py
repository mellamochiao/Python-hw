def Fibonacci(n):
	x = 0
	y = 1
	z = ''
	if n == 0:
		z = x
	if n == 1:
		z = y
	else:
		c = 2
		while c <= n:
			z = x + y
			x = y
			y = z
			c += 1
	print('The %d-th Fibonacci sequence number is : %d' %(n, z), end='')
	return ''

n = int(input('Input an integer number : '))
print(Fibonacci(n))
print('(i)')
a, b = 63, 105
while b:
	a, b = b, a % b
print(a)

print('(h)')
n = 21
while n != 1:
	print(n, end=", ")
	if n % 2 == 0:
		n = n // 2
	else:
		n=n*3+1 
print(n, end=".\n")

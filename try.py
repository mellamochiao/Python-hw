s = input('Enter a string :')
l = len(s)

n = 0
while n < l-2 :
	if s[n] == s[n+2]:
		if l == 3:
			print('Longest palindrome substring is : '+s[:])
		else:
			find = 0
			while s[n-find] == s[n+2+find] and find < l-n-3:
				if n+2+find == l:
					print('Longest palindrome substring is : '+s[n-find:])
				find += 1
			print('Longest palindrome substring is : '+s[n-find+1:n+2+find])
	n += 1





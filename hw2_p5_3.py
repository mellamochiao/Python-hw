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
	return z

def palindromic(s):
	l = len(s)
	start = 0
	length = 1
	i = 0
	while i < l:
		left = i
		right = i
		while right < l and left >= 0 and s[left] == s[right]:
			if right - left + 1 > length:
				start = left
				length = right - left +1
			right += 1
			left -= 1
        
        # 偶數長度回文
		left = i
		right = i + 1
		while right < l and left >= 0 and s[left] == s[right]:
			if right - left + 1 > length:
				start = left
				length = right - left +1
			right += 1
			left -= 1
		i += 1
	return s[start:start + length]


def encrypt(s, n, s1, s2):
    encrypted_text = ''
    index = 0
    a = len(palindromic(s1))
    b = len(palindromic(s2))
    f = Fibonacci(n)
    while index < len(s):
        char = s[index]
        if char.isalpha():
            ascii_code = ord(char)
            if char.isupper():
                # 凱薩
                caesar_shift = (ascii_code + f)
                # 仿射
                affine_cipher = (a * (caesar_shift) + b)
                encrypted_char = chr(((affine_cipher - ord('A'))%26)+ord('A'))
            else:
                # 凱薩
                caesar_shift = (ascii_code + f)
                # 仿射
                affine_cipher = (a * (caesar_shift) + b)
                encrypted_char = chr(((affine_cipher - ord('a'))%26)+ord('a'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
        index += 1
    print(encrypted_text)
    return ''


n = int(input('The number of the requested element in Fibonacci(n) = '))
s1 = input('The first string for Palindromic detection = ')
s2 = input('The second string for Palindromic detection = ')
si = input('The plaintext to be encryped : ')

print('- '*5 + 'extract key for encrypt method' + '- '*5)

print('The %d-th Fibonacci sequence number is : '%(n),Fibonacci(n))
print('Longest Palindromic Substring is : '+palindromic(s1))
print('Length is : %d' %len(palindromic(s1)))
print('Longest Palindromic Substring is : '+palindromic(s2))
print('Length is : %d' %len(palindromic(s2)))

print('- '*7 + 'encryption completed' + '- '*7)

print('The encrypted text is : ', end='')
print(encrypt(si, n, s1, s2),)

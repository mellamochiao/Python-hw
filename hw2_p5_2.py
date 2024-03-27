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
	print('Longest Palindromic Substring is : '+s[start:start + length])
	print('Length is : %d' %len(s[start:start + length]), end = '')
	return ''


s = input('Enter a string :')
print(palindromic(s))



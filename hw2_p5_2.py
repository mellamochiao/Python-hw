def longest_palindromic_substring(s):
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


s = input('Enter a string :')
print("Longest Palindromic Substring is : {}".format(longest_palindromic_substring(s)))		



	
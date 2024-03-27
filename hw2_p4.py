def tree(l, t, g, w, h):
	b = (g*(l-1)+t)*2 - 1 		# 最底層字元數
	s = (b - 1)//2 				# 星星前的空格
	print(' '* s + '#')
	a1 = 2
	while a1 < t:
		if t <= 2:
			print(' '*(s-(a1-1)) + '#'*(a1*2-1))
		else:
			print(' '*(s-(a1-1)) + '#' + '@'*((a1-1)*2-1) +'#')
		a1 += 1					
	print(' '*(s-(a1-1)) + '#'*(2*a1-1))		# 第一層結束
	layer = 2
	while layer <= l:
		a = 2
		while a < t + (g*(layer-1)):
			print(' '*(s-(a-1)) + '#' + '@'*((a-1)*2-1) +'#')
			a += 1
		print(' '*(s-(a-1)) + '#'*(2*a-1))	
		layer += 1
	height = 1
	while height <= h:
		print(' '*(s-((w-1)//2)) + '|'*w)
		height += 1
	return ''

try:
	layer = int(input('Enter the number of layers (2 to 5) : '))
	top_length = int(input('Enter the side length of the top layer :'))
	growth = int(input('Enter the growth of each layer : '))
	width = int(input('Enter the trunk width (odd number, 3 to 9) : '))
	height = int(input('Enter the trunk height (4 to 10) : '))
	print(tree(layer, top_length, growth, width, height), end = '')
except ValueError:
	print("Please enter a valid integer.")
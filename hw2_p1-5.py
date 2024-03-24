print('(a)')
x=7
y=8
if x < 7 or x <= 10 and y > 8:
   print("ugh")
else:
   print("yuck")

print('(b)')
phrase = "python"
vowels = "aeiou"
count = 0
while (not phrase[count] in vowels):
   count = count + 1
print(count)

print('(c)')
if 'alpha' < 'zebra':
   print('alpha < zebra')
elif 'alpha' > 'zebra':
   print('alpha > zebra')
elif 'alpha' == 'zebra':
   print('alpha == zebra')
else:
   print('none of the above')
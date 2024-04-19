s1 = input('Input sequence of seats : ')
s2 = s1.split(' ')
s = ''.join(s2)
n = len(s)

rmax = [0]*n
lmax = [0]*n

rmax[0] = s[0]
i = 1
while i < n :
    if s[i] > rmax[i-1]:
      rmax[i] = s[i]
    else:
      rmax[i] = rmax[i-1]
    i += 1

lmax[n-1] = s[n-1]
i = n-1
while i > 0 :
    if s[i-1] > lmax[i]:
      lmax[i-1] = s[i-1]
    else :
      lmax[i-1] = lmax[i]
    i -= 1

i = 1
water = 0
while i < n :
    if min(lmax[i], rmax[i]) > s[i]:
       water += (int (min(lmax[i], rmax[i])) - int(s[i]))
    i += 1
print(water)
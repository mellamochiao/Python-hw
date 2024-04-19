s1 = input('Input sequence of seats : ')
s2 = s1.split(' ')
s = ''.join(s2)
n = len(s)

rmax = []
rmax += s[0]
i = 1
while i < n :
    if s[i] > rmax[i-1]:
      rmax[i-1] = s[i]
      rmax += s[i]
    else :
      rmax += s[i]
    i += 1
print(rmax)


i = 1
water = 0
while i < n :
    if rmax[i] > s[i]:
      water += (int(max[i]) - int(s[i]))
    i += 1
print(water)
# 使用單指只能判斷一個方向（例如305, 503會得到不同結果）
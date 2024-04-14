s1 = input('Input sequence of seats : ')
s2 = s1.split(' ')
s = ''.join(s2)
n = len(s)

left_max = [0] * n
right_max = [0] * n
   
i = 1
left_max[0] = s[0]
while i < n:
    left_max[i] = max(left_max[i-1], s[i])
    i += 1

right_max[n-1] = s[n-1]
i = n - 2
while i >= 0:
    right_max[i] = max(right_max[i+1], s[i])
    i -= 1

water_units = 0
i = 0
j = n - 1

while i < j:
    if s[i] < s[j]:
        water_units += max(0, int(min(left_max[i], right_max[j])) - int(s[i]))
        i += 1
    else:
        water_units += max(0, int(min(left_max[i], right_max[j])) - int(s[j]))
        j -= 1
print(water_units)

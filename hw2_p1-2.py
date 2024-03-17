s1 = "spam"
s2 = "ni!"

print(s2.upper()[:2])
print(s2 + s1 + s2)
print((((s1.capitalize() + s2.capitalize()) + " ") *3).rstrip())
print(s1[:3] + s2[0])
print(s1[:2] + s1[3])


# upper()：全大寫 # capitalize()：句首大寫
# strip("")：移除字元
# rstrip("")：移除右邊字元
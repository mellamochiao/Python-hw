poly = input('Input polynomial : ')
x = input('Input the value of X : ')
poly_l = list(poly)

i = 0
cal = ""
while i < len(poly_l):
    if 'X' == poly_l[i]:
        poly_l[i] = x
    if '^' == poly_l[i]:
        poly_l[i] = '**'
    cal += poly_l[i]  # 将多项式字符串的每个部分连接成一个字符串
    i = i+1

r = eval(cal)  # 使用 eval() 函数计算多项式表达式的值
print(r)

#未解之謎：無法運算負號、不能使用eval()、開頭不能有負號

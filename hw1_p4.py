# User input h, m1, m2
h =  input("Input the height of the 1st ball : ")
m1 = input("Input the mass of the 1st ball : ")
m2 = input("Input the mass of the 2nd ball : ")
h = float(h)
m1 = float(m1)
m2 = float(m2)

# Calculate v1
g = 9.8
v1 = (2*g*h)**(1/2)

# Calculate v2 
v2 = (m1*(v1**2)/m2)**(1/2)

# print m1, m2, v2
print('The velocity of the 1st ball after slide :', v1, 'm/s')
print('The velocity of the 2nd ball after collision :', v2, 'm/s')
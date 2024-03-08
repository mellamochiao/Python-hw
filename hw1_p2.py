# User input F, r, m1
F =  input("Input the force : ")
m1 = input("Input the mass of m1 : ")
r = input("Input the distance : ")

# Convert from a string to a number
F = float(F)
m1 = float(m1)
r = float(r)

# Calculate m2
G = 6.67*(10**(-11))
m2 = F*(r**2)/(G*m1)

# Calculate E
c = 299792458
E = m2*(c**2)

# Print m, E
print('The mass of m2 =', m2)
print('The energy of m2 =', E)

# Reminder : input(""), float()=

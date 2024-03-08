# User input v
v = input("Input velocity : ")
v = float(v)

# Calculate r
c = 299792458
r = 1/((1-(v**2)/(c**2)))**(1/2)

# lightyear to meter : *c*3600*365
# Calculate Δtp and print
print('Percentage of light speed =', v/c)
print('AlphaCentauri :', 4.3/r)
print('Barnard’sStar :', 6.0/r)
print('Betelgeuse(intheMilkyWay) :', 309/r)
print('BAndromedaGalaxy(closestgalaxy) :', 2000000/r)

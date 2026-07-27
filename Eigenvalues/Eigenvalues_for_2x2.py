from math import sqrt
row1 = input("Row 1 seperated by spaces: ").split()
for i in [0,1]:
    row1[i] = int(row1[i])
row2 = input("Row 2 seperated by spaces: ").split()
for i in [0,1]:
    row2[i] = int(row2[i])
m = (row1[0]+row2[1])/2
p = (row1[0]*row2[1])-(row1[1]*row2[0])
eigenvalues = list(set([m+sqrt(m**2-p), m-sqrt(m**2-p)]))
print("Eigenvalues:")
for eigenv in eigenvalues:
    print(eigenv)
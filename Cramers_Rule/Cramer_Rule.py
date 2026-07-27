from numpy.linalg import det

num_var = int(input("Number of variables: "))
vars = input("Variables in order seperated by spaces: ").split()
matrix = []
constants = []
for i in range(num_var):
    matrix.append(list(map(float, input("Coeffiecients of variables in equation {0}, including zeroes: ".format(i)).split())))
    constants.append(int(input("Constant on the right hand side in equation {0}: ".format(i))))
for i in range(num_var):
    temp_matrix = [row[:] for row in matrix]
    for j in range(num_var):
        temp_matrix[j][i] = constants[j]
    print(vars[i] + ": " + str(det(temp_matrix)/det(matrix)))
Cramer's Rule is a concept used in linear algebra to solve systems of linear equations.
Cramer's Rule is applicable to n linear equations, each containing n different variables. The coefficients of the variables are put in one matrix, A, and the coefficients of the constants on the right-hand side are put in another matrix, B. The variables are put in yet another matrix, X.
The relationship between the two variables is AX=B. To solve for x, the inverse matrix of A is taken and multiplied by B.
The value of each variable in X can be expressed as xi = det(Ai)/det(A), where xi is the ith variable, Ai is the matrix A, but with the ith column of A being replaced with the column of B.

Cramer_Rule.py takes in the coefficients of the equations, the constants, and the variables to calculate and output the solution to the system using Cramer's rule.

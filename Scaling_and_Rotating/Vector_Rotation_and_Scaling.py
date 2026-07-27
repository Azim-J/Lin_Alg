from math import cos, sin, pi
import matplotlib.pyplot as plt
vector = input("Vector x and vector y seperated by spaces: ").split()
scaler = float(input("Scalar amount to scale the vector by: "))
angle_deg = float(input("Angle in degrees to rotate vector counterclockwise by: "))
angle_rad = angle_deg * (pi/180)
i_adjust = [round(cos(angle_rad), 5), round(sin(angle_rad), 5)]
j_adjust = [round(cos(angle_rad+pi/2), 5), round(sin(angle_rad+pi/2), 5)]
i_adjust, j_adjust
[x, y] = vector
x = float(x)
y = float(y)
vector = [x, y]
x = x*scaler
y = y*scaler
[ix, iy] = i_adjust
[jx, jy] = j_adjust
adj_vector = [x*ix+y*jx, x*iy+y*jy]
print(adj_vector)
plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color = "blue", label="Original")
plt.quiver(0, 0, adj_vector[0], adj_vector[1], angles='xy', scale_units='xy', scale=1, color = "red", label = "Adjusted")
plt.grid()
plt.title("Vectors")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.xlim((-1.5*max([abs(adj_vector[0]), abs(vector[0])]), 1.5*max([abs(adj_vector[0]), abs(vector[0])])))
plt.ylim((-1.5*max([abs(adj_vector[1]), abs(vector[1])])), 1.5*max([abs(adj_vector[1]), abs(vector[1])]))
plt.axhline(y=0, color="black", linewidth=2)
plt.axvline(x=0, color="black", linewidth=2)
plt.show()
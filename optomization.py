import numpy as np
from scipy.optimize import minimize,least_squares
from sklearn.metrics import mean_squared_error

#d = [xc yc xd yd zd]
#d = [0   1  2  3  4]
def distances(d):
    #Rosenbrock function - all equations to translate mirror distances with their relevant positions
    AC = np.sqrt(d[0]**2+d[1]**2)
    AD = np.sqrt(d[2]**2+d[3]**2+d[4]**2)
    BC = np.sqrt((np.sqrt(14604)-d[0])**2 + d[1]**2)
    CD = np.sqrt((d[0]-d[2])**2+(d[1]-d[3])**2 +d[4]**2)
    BD = np.sqrt((np.sqrt(14604)-d[2])**2+d[3]**2+d[4]**2)
    return AC,AD,BC,CD,BD

def rosen(d):
    #Rosenbrock function
    AC,AD,BC,CD,BD = distances(d)
    return  ((AC-np.sqrt(9891))**2 + (AD-np.sqrt(11889))**2 + (BC-np.sqrt(6664))**2 + (CD-np.sqrt(2094))**2 + (BD-np.sqrt(9578))**2)


#d0 = [[50,70,90,90,23]]
limit = 100
d0 =[[np.random.randint(limit, size=5)],[np.random.randint(limit, size=5)],[np.random.randint(limit, size=5)],[np.random.randint(limit, size=5)],[np.random.randint(limit, size=5)],[np.random.randint(limit, size=5)],[np.random.randint(limit, size=5)]]


Pos = []
#list = ["nelder-mead","powell","CG","BFGS","L-BFGS-B","TNC","COBYLA","SLSQP","trust-constr"]
#list = ["nelder-mead"]
#o = least_squares(rosen,d0,method="lm")
for j,i in enumerate(d0):
    a = minimize(rosen, i,method="nelder-mead",options={"disp":True})
    Pos.append(a.x)

Pos_n=np.array(Pos).reshape((len(d0),5))
#print(np.array(Pos).reshape((len(d0)*6,5)))

#print([rosen(Pos_n[0]),rosen(Pos_n[1]),rosen(Pos_n[2]),rosen(Pos_n[3]),rosen(Pos_n[4]),rosen(Pos_n[5])])
print(d0)
print(Pos_n)
#print(rosen(Pos_n[1]))
"""
import matplotlib.pyplot as plt

print(Pos)

x = Pos_n[:, 0]
y = Pos_n[:, 1]
z = Pos_n[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of points
ax.scatter(x, y, z, c='b', marker='o')

# Set labels for the axes
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Show the plot
plt.show()
"""

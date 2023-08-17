import numpy as np
from scipy.optimize import minimize,least_squares
from sklearn.metrics import mean_squared_error


#d = [xa ya za xb yb zb xc yc zc xd yd zd]
#d = [0   1  2  3  4  5  6 7  8  9  10 11]
def rosen(d):
    #Rosenbrock function
    AB = np.sqrt((d[0]-d[3])**2 + (d[1]-d[4])**2 + (d[2]-d[5])**2)
    AC = np.sqrt((d[0]-d[6])**2 + (d[1]-d[7])**2 + (d[2]-d[8])**2)
    AD = np.sqrt((d[0]-d[9])**2 + (d[1]-d[10])**2 + (d[2]-d[11])**2)
    BC = np.sqrt((d[3]-d[6])**2 + (d[4]-d[7])**2 + (d[5]-d[8])**2)
    DC = np.sqrt((d[6]-d[9])**2 + (d[7]-d[10])**2 + (d[8]-d[11])**2)
    BD = np.sqrt((d[3]-d[9])**2 + (d[4]-d[10])**2 + (d[5]-d[11])**2)
    return (AB-np.sqrt(14604))**2 + (AC-np.sqrt(9891))**2 + (AD-np.sqrt(11889))**2 + (BC-np.sqrt(6664))**2 + (DC-np.sqrt(2094))**2

d0 = [100,2,100,11,26,7,50,70,38,90,90,23]
d_correct = [82,3,96,9,28,3,57,82,41,94,75,15]
Pos = []
list = ["nelder-mead","powell","CG","BFGS","L-BFGS-B","TNC","COBYLA","SLSQP","trust-constr"]
#o = least_squares(rosen,d0,method="lm")
for j,i in enumerate(list):
    a = minimize(rosen, d0,method=i,options={"disp":True})
    Pos.append(a.x)


Pos_n = np.array(Pos).reshape((len(list)*4,3))


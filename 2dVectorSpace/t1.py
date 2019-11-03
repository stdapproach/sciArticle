#test python
import numpy as np
import matplotlib.pyplot as plt
import math

def matrMultVect(A,b):
    return A.dot(b)

def appendV(a,b):
    Z = np.empty([0,1])
    Z = np.vstack((Z, a))
    Z = np.vstack((Z, b))
    return Z

def newVec():
    return np.empty([0,1])

def getMaxAbs(U):
    xmax=U[np.unravel_index(abs(U).argmax(), U.shape)]
    return xmax

def crtChartQuiver(U, V, ax):
    n = U.shape[0]
    X = np.zeros(n)
    Y = np.zeros(n)
    colors = ["b" for x in range(n)]
    colors[0]='r'
    colors[math.floor(n/4)]='g'
    ax.quiver(X, Y, U, V, units='xy' ,scale=1, color=colors)
    #ax.quiver([0], [0], [0.5], [0.2], units='xy' ,scale=1, color='y', linestyle='-.')
    setupScale(U, V, ax)
    plt.grid()
    ax.set_aspect('equal')

def setupScale(U,V, ax):
    Z = appendV(U,V)
    xmax=1.1*getMaxAbs(Z)
    ax.set_xlim(-xmax,xmax)
    ax.set_ylim(-xmax,xmax)

def printAsRose(U, V):
    fig, ax = plt.subplots()
    crtChartQuiver(U, V, ax)
    plt.show()
#
def show2ChartAsRow1(x1, y1, x2, y2):
    fig, axes = plt.subplots(nrows=1, ncols=2)#, figsize=(5, 3))
    crtChartQuiver(x1, y1, axes[0])
    crtChartQuiver(x2, y2, axes[1])
    fig.tight_layout()
    plt.show()

#A = np.array([[ -1, -2 ], [ -1, 4 ]])#negative matrix
A = np.array([[ 3, -2 ], [ -1, 4 ]])

N = 10
#
arr = np.empty([0,6])
v_a1 = newVec()
v_a2 = newVec()
v_b1 = newVec()
v_b2 = newVec()
for i in range(N):
    phi = 2*math.pi*i/N
    a1 = math.cos(phi)
    a2 = math.sin(phi)
    v_a1 = np.vstack((v_a1, np.array([a1])))
    v_a2 = np.vstack((v_a2, np.array([a2])))
    vec_a = np.array([ a1, a2 ])
    vec_b = matrMultVect(A, vec_a)
    b1 = vec_b[0]
    b2 = vec_b[1]
    arr = np.vstack((arr, np.array([i, phi, a1, a2, b1, b2])))
    v_b1 = np.vstack((v_b1, np.array([b1])))
    v_b2 = np.vstack((v_b2, np.array([b2])))
print ("arr=", arr)

#printAsRose(v_a1, v_a2)
#printAsRose(v_b1, v_b2)
show2ChartAsRow1(v_a1, v_a2, v_b1, v_b2)
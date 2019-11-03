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

def crtChartQuiver(U, V, ax, title=''):
    n = U.shape[0]
    X = np.zeros(n)
    Y = np.zeros(n)
    colors = ["b" for x in range(n)]
    colors[0]='r'
    colors[math.floor(n/4)]='g'
    ax.quiver(X, Y, U, V, units='xy' ,scale=1, color=colors)
    #ax.quiver([0], [0], [0.5], [0.2], units='xy' ,scale=1, color='y', linestyle='-.')
    ax.set_title(title)
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

def show4Chart(x1, y1, x2, y2, x3, y3, x4, y4, title1, title2, title3, title4):
    fig, axes = plt.subplots(nrows=2, ncols=2)#, figsize=(5, 3))
    crtChartQuiver(x1, y1, axes[0,0], title1)
    crtChartQuiver(x2, y2, axes[0,1], title2)
    crtChartQuiver(x3, y3, axes[1,0], title3)
    crtChartQuiver(x4, y4, axes[1,1], title4)
    fig.tight_layout()
    plt.show()

A1 = np.array([[ -1, -2 ], [ -1, 4 ]])#negative matrix
A2 = np.array([[ 3, -2 ], [ -1, 4 ]])
N = 32

def crtChartTRansferPlaneByMatrix(A1, A2, n):
    arr = np.empty([0,6])
    v_a1 = newVec()
    v_a2 = newVec()
    v_b1 = newVec()
    v_b2 = newVec()
    v_c1 = newVec()
    v_c2 = newVec()
    for i in range(n):
        phi = 2*math.pi*i/n
        a1 = math.cos(phi)
        a2 = math.sin(phi)
        v_a1 = np.vstack((v_a1, np.array([a1])))
        v_a2 = np.vstack((v_a2, np.array([a2])))
        vec_a = np.array([ a1, a2 ])
        vec_b = matrMultVect(A1, vec_a)
        vec_c = matrMultVect(A2, vec_a)
        b1 = vec_b[0]
        b2 = vec_b[1]
        c1 = vec_c[0]
        c2 = vec_c[1]
        arr = np.vstack((arr, np.array([i, phi, a1, a2, b1, b2])))
        v_b1 = np.vstack((v_b1, np.array([b1])))
        v_b2 = np.vstack((v_b2, np.array([b2])))
        v_c1 = np.vstack((v_c1, np.array([c1])))
        v_c2 = np.vstack((v_c2, np.array([c2])))
    #print ("arr=", arr)

    #printAsRose(v_a1, v_a2)
    #printAsRose(v_b1, v_b2)
    #show2ChartAsRow1(v_a1, v_a2, v_b1, v_b2)
    s1 = np.array2string(A1, precision=2, separator=',', suppress_small=True)
    s2 = np.array2string(A2, precision=2, separator=',', suppress_small=True)
    show4Chart(v_a1, v_a2, v_b1, v_b2, v_a1, v_a2, v_c1, v_c2, 'negative matrix*R2-->', s1, 'positive matrix*R2-->', s2)

crtChartTRansferPlaneByMatrix(A1, A2, N)

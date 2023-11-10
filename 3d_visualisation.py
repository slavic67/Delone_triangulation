import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy.solvers.solveset import nonlinsolve,linsolve

with open("triangles.txt",'r') as file:
    triangles = [row.strip().split(' ') for row in file]
    triangles=[[int(item) for item in elem] for elem in triangles]

with open('data3.txt','r') as file:
    pts = [row.strip().split(' ') for row in file]
    pts= [[float(item) for item in elem] for elem in pts]

pts=np.array(pts)
P_c=[np.mean(pts[:,0]),np.mean(pts[0,:])]
P_o=[P_c[0],P_c[1],5]

# for elem in triangles:
#     plt.plot((pts[elem[0]][0], pts[elem[1]][0]), (pts[elem[0]][1], pts[elem[1]][1]))
#     plt.plot((pts[elem[0]][0], pts[elem[2]][0]), (pts[elem[0]][1], pts[elem[2]][1]))
#     plt.plot((pts[elem[1]][0], pts[elem[2]][0]), (pts[elem[1]][1], pts[elem[2]][1]))

#plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set(xlim=(-10,10),ylim=(-10,10),zlim=(0,15))


pts_Bi=[]
for i in range(len(pts)):
    t=sp.symbols("t")
    Pix=pts[i][0]
    Piy=pts[i][1]
    Piz=0
    Cx=P_c[0]
    Cy=P_c[1]
    Cz=3
    R=3
    Dx=Cx-Pix
    Dy=Cy-Piy
    Dz=Cz-Piz
    #ax.plot((Pix,Cx),(Piy,Cy),(Piz,Cz))


    eq=[sp.Eq((Pix + t * Dx - Cx)**2 + (Piy + t * Dy - Cy)**2 + (Piz + t * Dz - Cz)**2,R**2)]
    res=sp.solve(eq,t)


    numeric_solutions = [float(solution[0]) for solution in res]
    t=min(numeric_solutions)
    Bi=[Pix+t*Dx,Piy+t*Dy,Piz+t*Dz]
    print(Bi)
    pts_Bi.append(Bi)

pts_Bi=np.array(pts_Bi)





#ax.scatter(pts_Bi[:,0],pts_Bi[:,1],pts_Bi[:,2])
for elem in triangles:
    # ax.plot((pts_Bi[elem[0]][0], pts_Bi[elem[1]][0]), (pts_Bi[elem[0]][1], pts_Bi[elem[1]][1]))
    # ax.plot((pts_Bi[elem[0]][0], pts_Bi[elem[2]][0]), (pts_Bi[elem[0]][1], pts_Bi[elem[2]][1]))
    # ax.plot((pts_Bi[elem[1]][0], pts_Bi[elem[2]][0]), (pts_Bi[elem[1]][1], pts_Bi[elem[2]][1]))
    ax.plot((pts_Bi[elem[0]][0], pts_Bi[elem[1]][0]), (pts_Bi[elem[0]][1], pts_Bi[elem[1]][1]), (pts_Bi[elem[0]][2], pts_Bi[elem[1]][2]))
    ax.plot((pts_Bi[elem[0]][0], pts_Bi[elem[2]][0]), (pts_Bi[elem[0]][1], pts_Bi[elem[2]][1]), (pts_Bi[elem[0]][2], pts_Bi[elem[2]][2]))
    ax.plot((pts_Bi[elem[1]][0], pts_Bi[elem[2]][0]), (pts_Bi[elem[1]][1], pts_Bi[elem[2]][1]), (pts_Bi[elem[1]][2], pts_Bi[elem[2]][2]))
plt.show()
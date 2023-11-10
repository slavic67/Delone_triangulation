from python_delaunay import Graph, Point, Edge, Triangle
import random
import sys
#import pygame
import matplotlib.pyplot as plt

graph = Graph()
random.seed(1)

pts=[]
with open('data3.txt','r') as file:
    for i in range(218):
        string=file.readline()
        words=string.split()
        x,y=int(float(words[0])*100),int(float(words[1])*100)
        pts.append([x,y])


print("Adding points...")
for x in range(0,218):
	#while graph.addPoint(Point(random.randint(50,974), random.randint(50,718))) is False:
	while graph.addPoint(Point(pts[x][0], pts[x][1])) is False:
		print("Couldn't add point")

print("Generating Delaunay Mesh...")
graph.generateDelaunayMesh()


# for p in graph._points:
#     plt.scatter(p.pos()[0],p.pos()[1])
# for e in graph._edges:
# 	plt.plot((e._a.pos()[0],e._b.pos()[0]),(e._a.pos()[1],e._b.pos()[1]))


# for triangle in graph._triangles:
#     plt.plot((triangle._a.pos()[0],triangle._b.pos()[0]),(triangle._a.pos()[1],triangle._b.pos()[1]))
#     plt.plot((triangle._a.pos()[0], triangle._c.pos()[0]), (triangle._a.pos()[1], triangle._c.pos()[1]))
#     plt.plot((triangle._b.pos()[0], triangle._c.pos()[0]), (triangle._b.pos()[1], triangle._c.pos()[1]))


don_array=[]
for triangle in graph._triangles:
    a=pts.index(triangle._a.pos())
    b=pts.index(triangle._b.pos())
    c=pts.index(triangle._c.pos())
    don_array.append([a,b,c])

for elem in don_array:
    plt.plot((pts[elem[0]][0],pts[elem[1]][0]),(pts[elem[0]][1],pts[elem[1]][1]))
    plt.plot((pts[elem[0]][0], pts[elem[2]][0]), (pts[elem[0]][1], pts[elem[2]][1]))
    plt.plot((pts[elem[1]][0], pts[elem[2]][0]), (pts[elem[1]][1], pts[elem[2]][1]))

print(don_array[0])
# with open('triangles.txt','w') as file:
#     for elem in don_array:
#         file.write(f'{elem[0]} {elem[1]} {elem[2]}\n')

plt.show()
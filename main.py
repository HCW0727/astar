import cv2
import numpy as np
from astar import Astar

img = np.array([[0] * 100 for _ in range(100)])

f = open('pointcloud.txt','r')

f_lines = f.readlines()

for idx in range(len(f_lines)):
    x,y,z = f_lines[idx].split(' ')
    x_point = int((float(x)+15)/30*100)
    z_point = 100-int(float(z)/30*100)
    img[z_point,x_point] = 255

astar = Astar(img)

start_p = [40,99]
goal_p = [50,0]

result = astar.run(start_p,goal_p)

for block in result:
    img[block[1],block[0]] = 123

cv2.imwrite('result.png',img)

f.close()
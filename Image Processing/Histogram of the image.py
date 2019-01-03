'''
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
src=Image.open('Infrared.jpg')
r,g,b=src.split()

plt.figure("lena")
ar=np.array(r).flatten()
print(ar)
plt.hist(ar, bins=256, density=1,facecolor='r',edgecolor='r')
ag=np.array(g).flatten()
plt.hist(ag, bins=256, density=1, facecolor='g',edgecolor='g')
ab=np.array(b).flatten()
plt.hist(ab, bins=256, density=1, facecolor='b',edgecolor='b')
plt.show()
'''

from PIL import Image
from pylab import *
# 读取图像到数组中
im = array(Image.open('Infrared.jpg').convert('L'))
# 新建一个图像
figure()
# 不使用颜色信息
gray()
# 在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')
figure()
hist(im.flatten(),128)
show()

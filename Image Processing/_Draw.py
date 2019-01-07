from PIL import Image
import _numpy as np
import pylab 
# 读取图像到数组中
im = np.array(Image.open('C:\\Users\\vaiduryass\\Desktop\\Infrared.jpg'))
# 绘制图像
pylab.imshow(im)
# 一些点
x = [100,100,400,400]
y = [200,500,200,500]
# 使用红色星状标记绘制点
pylab.plot(x,y,'r*')
# 绘制连接前两个
# 添加标题，显示绘制的图像
pylab.title('Plotting: "empire.jpg"')
pylab.show()

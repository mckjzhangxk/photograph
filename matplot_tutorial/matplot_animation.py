import matplotlib as mlt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import itertools
import numpy as np

# 定义一个generator，为 生成每一帧 “种子数据"
# def gen_func():
#     for n in itertools.count():
#         t=n/10
#         # 在T的时候，指数函数 从1下降到 z0.5
#         T=4
#         C=np.log(1/0.5)/T
#         yield (t,np.sin(t)*np.exp(-C*t))

def gen_func():
    for n in itertools.count():
        if n>500:
            n=500
        t=n/10
        # 在T的时候，指数函数 从1下降到 z0.5
        omega=1
        # (D^2+w0^2)y=cos(w0t)的解
        yield (t,t*np.sin(omega*t)/(2*omega))

fig, axes = plt.subplots()
line, = axes.plot([], [])
axes.grid()
xdata, ydata = [], []


# 这里可以理解成为初始 的清屏函数
def init():
    axes.set_ylim(-1, 1)
    axes.set_xlim(0, 2)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)

# 画图函数，参数是 gen_func 生成的数据
def drawFunc(data):
    x, y = data
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    xmin,xmax=axes.get_xlim()
    ymin,ymax=axes.get_ylim()
    if x>xmax:
        axes.set_xlim(xmin,x)
        # axes.figure.canvas.draw()
    if y>ymax:
        axes.set_ylim(-y,y)
    # return line,
ani=animation.FuncAnimation(fig,drawFunc,gen_func,interval=10,init_func=init)
plt.show()
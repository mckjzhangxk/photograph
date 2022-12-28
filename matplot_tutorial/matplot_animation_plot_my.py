import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



fig, axes = plt.subplots()
x = np.arange(0, 4*np.pi, 0.01)
y=np.sin(x)
line, = axes.plot(x, y)

# 计算导数
def calGrad(x):
    x,y=x,np.sin(x)

    dx= 0.5
    dy=dx*np.cos(x)

    if np.abs(dy)<1e-3:
        dx,dy=0,0

    return x+dx,y+dy

arrow = {"arrowstyle": "<-", "color": 'red'}
grad=axes.annotate("", xy=(x[0], y[0]), xytext=calGrad(x[0]), arrowprops=arrow)
# 计算导数结束


scatter,=axes.plot([0],[0],marker='o',color='#ff00ff',lw=5)
axes.grid()

def animate(i):
    # line.set_xdata(x)
    # line.set_ydata(np.sin(x + i / 50))  # update the data.
    n=i%len(x)
    scatter.set_xdata([x[n]])
    scatter.set_ydata([y[n]])

    grad.xy=(x[n],y[n])
    grad.set_position(calGrad(x[n]))


    # return scatter,

ani=animation.FuncAnimation(fig,animate,interval=10)
plt.show()
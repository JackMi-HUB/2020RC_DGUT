import numpy as np
import cv2 as cv
from scipy import interpolate
import matplotlib.pyplot as plt
import matplotlib.patches as mp

class Point_Move:
    showverts = True
    offset = 100 # 距离偏差设置

    def __init__(self):
        # 创建figure（绘制面板）、创建图表（axes）
        self.fig,self.ax = plt.subplots()
        # 设置标题
        self.ax.set_title('B—spline  2020robocon')
        # 设置坐标轴范围
        self.ax.set_xlim((-10000, 0))
        self.ax.set_ylim((0, 6650))
        rect = mp.Rectangle((-1000, 0), 1000, 1000, color='b', alpha=0.5, angle=0)
        rect1 = mp.Rectangle((-10000, 0), 10000, 1575, color='darkgreen', alpha=0.5, angle=0)
        rect2 = mp.Rectangle((-5000, 1575), 5000, 2500, color='royalblue', alpha=0.5, angle=0)
        rect3 = mp.Rectangle((-7500, 1575), 2500, 2500, color='b', alpha=0.5, angle=0)
        rect4 = mp.Rectangle((-10000, 1575), 2500, 2500, color='navy', alpha=0.5, angle=0)
        rect5 = mp.Rectangle((-10000, 4075), 10000, 2075, color='lime', alpha=0.5, angle=0)
        rect6 = mp.Rectangle((-10000, 4075), 1000, 1000, color='b', alpha=0.5, angle=0)
        rect7 = mp.Rectangle((-10000, 6150), 1500, 475, color='cornflowerblue', alpha=0.5, angle=0)
        rect8 = mp.Rectangle((-8500, 6150), 1300, 475, color='gold', alpha=0.5, angle=0)
        rect9 = mp.Rectangle((-7200, 6150), 580, 475, color='darkgreen', alpha=0.5, angle=0)
        rect10 = mp.Rectangle((-6620, 6150), 750, 475, color='gold', alpha=0.5, angle=0)
        rect11 = mp.Rectangle((-5870, 6150), 580, 475, color='darkgreen', alpha=0.5, angle=0)
        rect12 = mp.Rectangle((-5290, 6150), 750, 475, color='gold', alpha=0.5, angle=0)
        rect13 = mp.Rectangle((-4540, 6150), 580, 475, color='darkgreen', alpha=0.5, angle=0)
        rect14 = mp.Rectangle((-3940, 6150), 750, 475, color='gold', alpha=0.5, angle=0)
        rect15 = mp.Rectangle((-3190, 6150), 580, 475, color='darkgreen', alpha=0.5, angle=0)
        rect16 = mp.Rectangle((-2610, 6150), 750, 475, color='gold', alpha=0.5, angle=0)
        rect17 = mp.Rectangle((-1860, 6150), 580, 475, color='darkgreen', alpha=0.5, angle=0)
        rect18 = mp.Rectangle((-1300, 6150), 1300, 475, color='gold', alpha=0.5, angle=0)
        # 圆形 圆心坐标 半径 颜色 alpha
        circ = plt.Circle((-6910, 4075), 107, color='r', alpha=0.5)
        circ1 = plt.Circle((-5580, 2560), 107, color='r', alpha=0.5)
        circ2 = plt.Circle((-4250, 4075), 107, color='r', alpha=0.5)
        circ3 = plt.Circle((-2920, 2560), 107, color='r', alpha=0.5)
        circ4 = plt.Circle((-1590, 4075), 107, color='r', alpha=0.5)

        # 两点之间连线
        x = [[-10000, 0], [-500, -500], [-2233, -2233], [-4198, -4198],
             [-6163, -6163], [-2233, -6163], [-5580, -5580], [-2920, -2920]
            , [-10000, 0], [-10000, -9000], [-9500, -9500], [-6940, -6940], [-4250, -4250], [-1590, -1590]]  # 要连接点的x坐标
        y = [[500, 500], [0, 1000], [500, 3302], [500, 3302], [500, 3302],
             [3302, 3302], [3302, 5810], [3302, 5810], [5660, 5660],
             [4575, 4575], [4075, 5660], [5510, 5810], [5510, 5810], [5510, 5810]]

        for i in range(len(x)):
            plt.plot(x[i], y[i], linewidth=3, color='w')
        # 添加常见的图形对象。这些对象被成为块(patch).完整的patch集合位于matplotlib.patches中
        # 绘制patch对象图形：plt.gca().add_patch), (-6955.645161290322, 2990.34090909091), (-7177.419354838709, 3350.189393939395), (-7419.354838709677, 3566.098484848486)](patch_name)
        plt.gca().add_patch(rect)
        plt.gca().add_patch(rect1)
        plt.gca().add_patch(rect2)
        plt.gca().add_patch(rect3)
        plt.gca().add_patch(rect4)
        plt.gca().add_patch(rect5)
        plt.gca().add_patch(rect6)
        plt.gca().add_patch(rect7)
        plt.gca().add_patch(rect8)
        plt.gca().add_patch(rect9)
        plt.gca().add_patch(rect10)
        plt.gca().add_patch(rect11)
        plt.gca().add_patch(rect12)
        plt.gca().add_patch(rect13)
        plt.gca().add_patch(rect14)
        plt.gca().add_patch(rect15)
        plt.gca().add_patch(rect16)
        plt.gca().add_patch(rect17)
        plt.gca().add_patch(rect18)
        plt.gca().add_patch(circ)
        plt.gca().add_patch(circ1)
        plt.gca().add_patch(circ2)
        plt.gca().add_patch(circ3)
        plt.gca().add_patch(circ4)

        # 设置初始值
        pos = plt.ginput(5)
        #print(pos)
        self.x = [pos[0][0],pos[1][0],pos[2][0],pos[3][0],pos[4][0]]
        self.y = [pos[0][1],pos[1][1],pos[2][1],pos[3][1],pos[4][1]]
        list=[(self.x[0],self.y[0]),(self.x[1],self.y[1]),(self.x[2],self.y[2]),(self.x[3],self.y[3]),(self.x[4],self.y[4])]
        #print(list)

        # b样条算法
        #
        #print(list0)
        ctr = np.array(list)
        # ,(-6100,1700)
        x = ctr[:, 0]
        y = ctr[:, 1]
        # print(pos)
        # B样条算法
        tck, u = interpolate.splprep([x, y], k=3, s=10)
        u = np.linspace(0, 1, num=100, endpoint=True)
        out = interpolate.splev(u, tck)
        file = open('2.txt', mode='w')
        np.savetxt('2.txt', out, fmt='%d', delimiter=',')
        # B样条曲线地图绘制
        plt.plot(x, y, 'ro', out[0], out[1], 'b')
        # 图二B样条曲线绘制

           # 标志值设为none
        self._ind = None
        # 设置画布，方便后续画布响应事件
        canvas = self.fig.canvas
        canvas.mpl_connect('draw_event', self.draw_callback)
        canvas.mpl_connect('button_press_event', self.button_press_callback)
        canvas.mpl_connect('button_release_event', self.button_release_callback)
        canvas.mpl_connect('motion_notify_event', self.motion_notify_callback)
        self.canvas = canvas
        plt.grid()
        plt.show()

    # 界面重新绘制
    def draw_callback(self, event):
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        #self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)

    def get_ind_under_point(self, event):
        'get the index of the vertex under point if within epsilon tolerance'
        # 在公差允许的范围内，求出鼠标点下顶点坐标的数值
        xt,yt = np.array(self.x),np.array(self.y)
        d = np.sqrt((xt-event.xdata)**2 + (yt-event.ydata)**2)
        indseq = np.nonzero(np.equal(d, np.amin(d)))[0]
        ind = indseq[0]
        # 如果在公差范围内，则返回ind的值
        if d[ind] >=self.offset:
            ind = None
        return ind

    # 鼠标被按下，立即计算最近的顶点下标
    def button_press_callback(self, event):
        'whenever a mouse button is pressed'
        if not self.showverts: return
        if event.inaxes==None: return
        if event.button != 1: return
        self._ind = self.get_ind_under_point(event)

    # 鼠标释放后，清空、重置
    def button_release_callback(self, event):
        'whenever a mouse button is released'
        if not self.showverts: return
        if event.button != 1: return
        self._ind = None

    # 鼠标移动的事件
    def motion_notify_callback(self, event):
        'on mouse movement'
        if not self.showverts: return
        if self._ind is None: return
        if event.inaxes is None: return
        if event.button != 1: return
        # 更新数据
        x,y = event.xdata, event.ydata

        self.x[self._ind] = x
        self.y[self._ind] = y
        # 根据更新的数值，重新绘制图形zz
        print(self.x)
        print(self.y)
        plt.draw()
        plt.clf()
        rect = mp.Rectangle((-1000, 0), 1000, 1000, color='b', alpha=0.5, angle=0)
        rect1 = mp.Rectangle((-10000, 0), 10000, 1575, color='darkgreen', alpha=0.5, angle=0)
        rect2 = mp.Rectangle((-5000, 1575), 5000, 2500, color='royalblue', alpha=0.5, angle=0)
        rect3 = mp.Rectangle((-7500, 1575), 2500, 2500, color='b', alpha=0.5, angle=0)
        rect4 = mp.Rectangle((-10000, 1575), 2500, 2500, color='navy', alpha=0.5, angle=0)
        rect5 = mp.Rectangle((-10000, 4075), 10000, 2075, color='lime', alpha=0.5, angle=0)
        rect6 = mp.Rectangle((-10000, 4075), 1000, 1000, color='b', alpha=0.5, angle=0)
        rect7 = mp.Rectangle((-10000, 6150), 1500, 475, color='cornflowerblue', alpha=0.5, angle=0)
        rect8 = mp.Rectangle((-8500, 6150), 1300, 475, color='gold', alpha=0.5, angle=0)
        rect9 = mp.Rectangle((-7200, 6150), 580, 475, color='darkgreen', alpha=0.5, angle=0)
        rect10 = mp.Rectangle((-6620, 6150), 750, 475, color='gold', alpha=0.5, angle=0)
        rect11 = mp.Rectangle((-5870, 6150), 580, 475, color='darkgreen', alpha=0.5, angle=0)
        rect12 = mp.Rectangle((-5290, 6150), 750, 475, color='gold', alpha=0.5, angle=0)
        rect13 = mp.Rectangle((-4540, 6150), 580, 475, color='darkgreen', alpha=0.5, angle=0)
        rect14 = mp.Rectangle((-3940, 6150), 750, 475, color='gold', alpha=0.5, angle=0)
        rect15 = mp.Rectangle((-3190, 6150), 580, 475, color='darkgreen', alpha=0.5, angle=0)
        rect16 = mp.Rectangle((-2610, 6150), 750, 475, color='gold', alpha=0.5, angle=0)
        rect17 = mp.Rectangle((-1860, 6150), 580, 475, color='darkgreen', alpha=0.5, angle=0)
        rect18 = mp.Rectangle((-1300, 6150), 1300, 475, color='gold', alpha=0.5, angle=0)
        # 圆形 圆心坐标 半径 颜色 alpha
        circ = plt.Circle((-6910, 4075), 107, color='r', alpha=0.5)
        circ1 = plt.Circle((-5580, 2560), 107, color='r', alpha=0.5)
        circ2 = plt.Circle((-4250, 4075), 107, color='r', alpha=0.5)
        circ3 = plt.Circle((-2920, 2560), 107, color='r', alpha=0.5)
        circ4 = plt.Circle((-1590, 4075), 107, color='r', alpha=0.5)

        # 两点之间连线
        x = [[-10000, 0], [-500, -500], [-2233, -2233], [-4198, -4198],
             [-6163, -6163], [-2233, -6163], [-5580, -5580], [-2920, -2920]
            , [-10000, 0], [-10000, -9000], [-9500, -9500], [-6940, -6940], [-4250, -4250], [-1590, -1590]]  # 要连接点的x坐标
        y = [[500, 500], [0, 1000], [500, 3302], [500, 3302], [500, 3302],
             [3302, 3302], [3302, 5810], [3302, 5810], [5660, 5660],
             [4575, 4575], [4075, 5660], [5510, 5810], [5510, 5810], [5510, 5810]]

        for i in range(len(x)):
            plt.plot(x[i], y[i], linewidth=3, color='w')
        # 添加常见的图形对象。这些对象被成为块(patch).完整的patch集合位于matplotlib.patches中
        # 绘制patch对象图形：plt.gca().add_patch), (-6955.645161290322, 2990.34090909091), (-7177.419354838709, 3350.189393939395), (-7419.354838709677, 3566.098484848486)](patch_name)
        plt.gca().add_patch(rect)
        plt.gca().add_patch(rect1)
        plt.gca().add_patch(rect2)
        plt.gca().add_patch(rect3)
        plt.gca().add_patch(rect4)
        plt.gca().add_patch(rect5)
        plt.gca().add_patch(rect6)
        plt.gca().add_patch(rect7)
        plt.gca().add_patch(rect8)
        plt.gca().add_patch(rect9)
        plt.gca().add_patch(rect10)
        plt.gca().add_patch(rect11)
        plt.gca().add_patch(rect12)
        plt.gca().add_patch(rect13)
        plt.gca().add_patch(rect14)
        plt.gca().add_patch(rect15)
        plt.gca().add_patch(rect16)
        plt.gca().add_patch(rect17)
        plt.gca().add_patch(rect18)
        plt.gca().add_patch(circ)
        plt.gca().add_patch(circ1)
        plt.gca().add_patch(circ2)
        plt.gca().add_patch(circ3)
        plt.gca().add_patch(circ4)
        list2 = [(self.x[0], self.y[0]), (self.x[1], self.y[1]), (self.x[2], self.y[2]), (self.x[3], self.y[3]),
                 (self.x[4], self.y[4])]
        #print(list2[0])
        #print(list2[1])

        ctr = np.array(list2)
        # ,(-6100,1700)
        x = ctr[:, 0]
        y = ctr[:, 1]
        # print(pos)
        # B样条算法
        tck, u = interpolate.splprep([x, y], k=3, s=10)
        u = np.linspace(0, 1, num=100, endpoint=True)
        out1 = interpolate.splev(u, tck)
        file = open('2.txt', mode='w')
        np.savetxt('2.txt', out1, fmt='%d', delimiter=',')
        # B样条曲线地图绘制
        plt.plot(x, y, 'ro', out1[0], out1[1], 'b')


if __name__ == '__main__':
    Point_Move()



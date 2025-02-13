from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import numpy as np
import sympy
from matplotlib import pyplot as plt

from agent import Agent

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Простой генетический алгоритм")
        self.setGeometry(100, 100, 800, 600)
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        # Поля ввода параметров
        self.FunEdit = QtWidgets.QLineEdit(self)
        self.AEdit = QtWidgets.QLineEdit(self)
        self.BEdit = QtWidgets.QLineEdit(self)
        self.DEdit = QtWidgets.QLineEdit(self)
        self.MutStrange = QtWidgets.QLineEdit(self)
        self.MutChast = QtWidgets.QLineEdit(self)
        self.CountPopSB = QtWidgets.QSpinBox(self)
        self.CountPopSB.setValue(10)
        self.CountOsSB = QtWidgets.QSpinBox(self)
        self.CountOsSB.setValue(10)
        self.TypeBox = QtWidgets.QComboBox(self)
        self.TypeBox.addItems(["Max","Min"])
        self.StartBtn = QtWidgets.QPushButton("Start", self)
        self.StopBtn = QtWidgets.QPushButton("Stop", self)
        self.Slider = QtWidgets.QSlider(self)
        self.Slider.setOrientation(1)
        self.Graph = QtWidgets.QLabel(self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("Func:"))
        layout.addWidget(self.FunEdit)
        layout.addWidget(QtWidgets.QLabel("Bounds A and B:"))
        layout.addWidget(self.AEdit)
        layout.addWidget(self.BEdit)
        layout.addWidget(QtWidgets.QLabel("Tolerance:"))
        layout.addWidget(self.DEdit)
        layout.addWidget(QtWidgets.QLabel("Mutation frequency:"))
        layout.addWidget(self.MutChast)
        layout.addWidget(QtWidgets.QLabel("Mutation strangeness:"))
        layout.addWidget(self.MutStrange)
        layout.addWidget(QtWidgets.QLabel("Number of populations:"))
        layout.addWidget(self.CountPopSB)
        layout.addWidget(QtWidgets.QLabel("Number of populations:"))
        layout.addWidget(self.CountOsSB)
        layout.addWidget(QtWidgets.QLabel("Optimization type:"))
        layout.addWidget(self.TypeBox)
        layout.addWidget(self.StartBtn)
        layout.addWidget(self.StopBtn)
        layout.addWidget(QtWidgets.QLabel("Choose generation:"))
        layout.addWidget(self.Slider)
        layout.addWidget(self.Graph)
        central_widget.setLayout(layout)
        self.StartBtn.clicked.connect(self.start)
        self.Slider.valueChanged.connect(self.slide)
        self.StopBtn.setVisible(False)
        self.count = 0

    # создаем UI (пользовательский интерфейс)
    def start(self):
        A = int(self.AEdit.text())
        B = int(self.BEdit.text())
        D = int(self.DEdit.text())
        tp = self.TypeBox.currentText()
        countpop = self.CountPopSB.value()
        strengMut = float(self.MutStrange.text())
        chastMut = float(self.MutChast.text())
        countos = self.CountOsSB.value()
        self.Slider.setMaximum(countpop-1)
        self.agents = []        #INIT FUNC
        x = sympy.Symbol('x')
        fun = sympy.lambdify(x, self.FunEdit.text())
        ar = np.array(self.gen_x(A, B))
        xx, y = self.get_y(fun, ar)

        #создаем точки, особи (агенты)
        for i in range(countos):
            par = (B - A) * np.random.rand() + A
            self.agents.append(Agent(par))
            self.agents[-1].calculate(fun)

        for i in range(countpop):
            self.drawplot(xx, y) #далее ищем "плохие" точки
            for k in range(int(countos / 2)):
                minim = 1000
                maxim = -1000
                index = 0
                ind = 0
                if tp == 'максимум':
                    for d in self.agents:
                        if d.rY() < minim:
                            minim = d.rY()
                            index = ind
                        ind += 1
                elif tp == 'минимум':
                    for d in self.agents:
                        if d.rY() > maxim:
                            maxim = d.rY()
                            index = ind
                        ind += 1
                self.drawpoint(self.agents[index].rX(), self.agents[index].rY(), 'r')
                del self.agents[index]
            for f in self.agents:
                self.drawpoint(f.rX(), f.rY(), 'g')
            self.saveplt(i)

            #Генерируем следующее поколение
            secund = 0
            for dl in range(int(countos / 2)):
                self.agents.append(Agent(self.agents[secund].rX()))
                secund += 1
            for ag in range(len(self.agents)):
                self.agents[ag].mutate(strengMut, chastMut)
                self.agents[ag].calculate(fun)
        self.show_graph(0)

    # slider`s event-function
    def slide(self):
        self.show_graph(self.Slider.value())

    # функция для вывода графика (открывается в папке - tmp)
    def show_graph(self, name):
        self.mypix = QPixmap("./tmp/" + str(name) + ".jpg").scaled(640, 480)
        self.Graph.setPixmap(self.mypix)

    # генерируем массив между A и B.
    def gen_x(self, A, B):
        shag = 0.01
        ret = []
        while A < B:
            ret.append(A)
            A += shag
        return ret

    # функция преобразования массива Y в формат numpy
    def get_y(self, fun, ar):
        ret = np.zeros(len(ar))
        for ind, i in enumerate(ar):
            ret[ind] = fun(i)
        return ar, ret

    # функция прорисовки графика
    def drawplot(self, xx, y):
        fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1)
        self.ax.plot(xx, y)

    # функция для добавления точки к графику
    def drawpoint(self, x, y, color):
        self.ax.scatter(x, y, c=color)

    # функция для сохранения графика
    def saveplt(self, name):
        plt.savefig('./tmp/' + str(name) + '.jpg', dpi=50)
        plt.close()
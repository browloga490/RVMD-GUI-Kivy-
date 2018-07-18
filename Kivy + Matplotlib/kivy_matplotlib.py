from matplotlib import pyplot as plt
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
#from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

import matplotlib
matplotlib.use("module://kivy.garden.matplotlib.backend_kivy")
from kivy.garden.matplotlib import FigureCanvasKivyAgg

class LineBuilder:
    n = 0
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
#        self.cid = line.figure.canvas.mpl_connect('motion_notify_event', self)

    def __call__(self, event):
#        print 'click', event
        if event.inaxes!=self.line.axes: return
        print('n=', self.n)
        self.n += 1
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

class GT(BoxLayout):
    """Receives custom widget from corresponding <name>.kv file"""
    label_widget = ObjectProperty()
    graph_widget = ObjectProperty()
    def __init__(self, **kwargs):
        super(GT, self).__init__(**kwargs)
        Window.clearcolor = (0.9, 0.93, 0.95, 1)

    def do_action(self):
        self.label_widget.text = 'Graph was clicked.' # This works
        self.info = 'Important info!'


class frameworkApp(App):
    def build(self):
        return GT()
    """I want to invoke matplotlib for graphs, but have them appear
    within a RelativeLayout of a BoxLayout, not in a separate window.
    Note: The 8 icons above the pyplot graph (Figure 1) are not necessary here."""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('click to build line segments')
    line, = ax.plot([0], [0])  # empty line
    linebuilder = LineBuilder(line)
    plt.show()


if __name__ == '__main__':
    frameworkApp().run()

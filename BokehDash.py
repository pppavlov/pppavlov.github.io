import random
from bokeh.plotting import figure, show
from bokeh.io import output_file, show, output_notebook, save

class DashPlot:
    
    def __init__(self):
        self.n = 42 
        self.x = list(range(0, self.n))
        self.y = [random.random()  for i in range(0,self.n)]
        
    def func_plot(self):


        # generate list of rgb hex colors in relation to y
        colors = ["#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in self.y]

        # create new plot
        p = figure(
            title="Automate random point",
            sizing_mode="stretch_width",
            max_width=500,
            height=250,
        )

        # add circle and line renderers
        line = p.line(self.x, self.y, line_color="blue", line_width=1)
        circle = p.circle(self.x, self.y, fill_color=colors, line_color="blue", size=15)

        output_file('index.html')

        save(p, 'index.html')
    
    def update_data(self):
        self.n = self.n + 1
        self.x.append(self.n)
        self.y.append(random.random())
    
    def update_func(self):
        self.update_data()
        self.func_plot()

        
dp = DashPlot()
dp.update_func()
    
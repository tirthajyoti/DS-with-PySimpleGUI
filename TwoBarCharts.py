import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

sg.theme('Light Brown 3')
FIG_WIDTH = 5
FIG_HEIGHT = 3

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

values_to_plot = (20, 35, 30, 35, 27)
ind = np.arange(len(values_to_plot))
width = 0.4
fig1 = plt.figure(figsize=(FIG_WIDTH, FIG_HEIGHT))
p1 = plt.bar(ind, values_to_plot, width)
plt.ylabel('Y-Axis Values')
plt.title('First bar chart')
plt.xticks(ind, ['Item'+str(i) for i in ind])
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0],), ('Data Group 1',))
figure_x, figure_y, figure_w, figure_h = fig1.bbox.bounds

# define the window layout
layout = [[sg.Text('Two bar charts', font='Times 18 bold')],
          [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-1')],
          [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-2')],
          [sg.OK(pad=((figure_w / 2, 0), 3), size=(4, 2))]]

# create the form and show it without the plot
window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI',
    layout, force_toplevel=True, finalize=True)

# add the plot to the window
fig_photo1 = draw_figure(window['-CANVAS-1'].TKCanvas, fig1)

fig2 = plt.figure(figsize=(FIG_WIDTH, FIG_HEIGHT))
values_to_plot = (10, 55, 20, 31, 17, 65, 44)
ind = np.arange(len(values_to_plot))
p2 = plt.bar(ind, values_to_plot, width)
plt.ylabel('Y-Axis Values')
plt.title('Second bar chart')
plt.xticks(ind, ['Item'+str(i) for i in ind])
plt.yticks(np.arange(0, 81, 10))
plt.legend((p2[0],), ('Data Group 2',))

fig_photo2 = draw_figure(window['-CANVAS-2'].TKCanvas, fig2)

# show it all again and get buttons
event, values = window.read()
window.close()
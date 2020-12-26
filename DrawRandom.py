import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Update function
def data_gen():
    fig1 = plt.figure(dpi=125)
    x = np.round(10*np.random.random(20),3)
    y = np.round(10*np.random.random(20),3)
    p1 = plt.scatter(x,y,edgecolor='k')
    plt.ylabel('Y-Values')
    plt.xlabel('X-Values')
    plt.title('Scatter plot')
    figure_x, figure_y, figure_w, figure_h = fig1.bbox.bounds
    return (x,y,fig1,figure_x, figure_y, figure_w, figure_h)

def draw_figure(canvas, figure, loc=(0, 0)):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

def delete_fig_agg(fig_agg):
    fig_agg.get_tk_widget().forget()
    plt.close('all')

# Define the window's contents i.e. layout
layout = [
        [sg.Button('Generate a random scatter plot',enable_events=True, key='-GENERATE-', font='Helvetica 16')],
        [sg.Canvas(size=(350,350), key='-CANVAS-', pad=(20,20))],
        [sg.Button('Exit')],
        ]

# Create the window
window = sg.Window('Generate random integer', layout, size=(700,700))

# Event loop
fig_agg = None
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-GENERATE-':
        if fig_agg is not None:
            delete_fig_agg(fig_agg)
        _,_,fig1,figure_x, figure_y, figure_w, figure_h = data_gen()
        canvas_elem = window['-CANVAS-'].TKCanvas
        canvas_elem.Size=(int(figure_w),int(figure_h))
        fig_agg = draw_figure(canvas_elem, fig1)

# Close the window i.e. release resource
window.close()
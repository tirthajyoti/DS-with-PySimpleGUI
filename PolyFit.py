import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Update function
def data_gen():
    fig1 = plt.figure(dpi=125)
    x = np.round(10*np.random.random(20),3)
    y = 0.5*x**2+3*x+5+np.random.normal(scale=noise,size=20)
    p1 = plt.scatter(x,y,edgecolor='k')
    plt.ylabel('Y-Values')
    plt.xlabel('X-Values')
    plt.title('Scatter plot')
    figure_x, figure_y, figure_w, figure_h = fig1.bbox.bounds
    return (x,y,fig1,figure_x, figure_y, figure_w, figure_h)

def fit_redraw(x,y,model):
    fig2 = plt.figure(dpi=125)
    x_min,x_max = np.min(x),np.max(x)
    x_reg = np.arange(x_min,x_max,0.01)
    y_reg = np.poly1d(model)(x_reg) 
    p1 = plt.scatter(x,y,edgecolor='k')
    p2 = plt.plot(x_reg,y_reg,color='orange',lw=3)
    plt.ylabel('Y-Values')
    plt.xlabel('X-Values')
    plt.title('Scatter plot with fit')
    return fig2

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
        [sg.Button('Generate',enable_events=True, key='-GENERATE-', font='Helvetica 16'), 
         sg.Button('Fit',enable_events=True, key='-FIT-', font='Helvetica 16', size=(10,1))],
        [sg.Text("Gaussian noise (std. devition)", font=('Helvetica', 12)), 
         sg.Slider(range=(0,6), default_value=3, size=(20,20), orientation='h',font=('Helvetica', 12), key='-NOISE-')],
        [sg.Canvas(size=(350,350), key='-CANVAS-', pad=(20,20))],
        [sg.Button('Exit')],
        ]

# Create the window
window = sg.Window('Polynomial fitting', layout, size=(700,700))

# Event loop
fig_agg = None
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-GENERATE-':
        noise = values['-NOISE-']
        if fig_agg is not None:
            delete_fig_agg(fig_agg)
        x,y,fig1,figure_x, figure_y, figure_w, figure_h = data_gen()
        canvas_elem = window['-CANVAS-'].TKCanvas
        canvas_elem.Size=(int(figure_w),int(figure_h))
        fig_agg = draw_figure(canvas_elem, fig1)
    if event == '-FIT-':
        model = np.polyfit(x, y, 2)
        if fig_agg is not None:
            delete_fig_agg(fig_agg)
        fig2 = fit_redraw(x,y,model)
        canvas_elem = window['-CANVAS-'].TKCanvas
        fig_agg = draw_figure(canvas_elem, fig2)
# Close the window i.e. release resource
window.close()
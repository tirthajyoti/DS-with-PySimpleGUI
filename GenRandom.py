import PySimpleGUI as sg
import numpy as np

# Update function
def update():
    r = np.random.randint(1,100)
    text_elem = window['-text-']
    text_elem.update("This is a random integer: {}".format(r))

# Define the window's contents i.e. layout
layout = [[sg.Button('Generate',enable_events=True, key='-FUNCTION-', font='Helvetica 16')],
         [sg.Text('This is a random integer:', size=(25, 1), key='-text-', font='Helvetica 16')]]

# Create the window
window = sg.Window('Generate random integer', layout, size=(350,100))

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-FUNCTION-':
        update()

# Close the window i.e. release resource
window.close()
import PySimpleGUI as sg
from math import sqrt

def solver(a,b,c):
    if b**2 >=4*a*c:
        x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
        return round(x1,3),round(x2,3)
    else:
        omega1 = round(-b/(2*a),3)
        omega2 = round(sqrt(4*a*c-b**2)/(2*a),3)
        x1 = str(omega1)+" + "+str(omega2)+"i"
        x2 = str(omega1)+" - "+str(omega2)+"i"
        return x1,x2

layout = [
     [sg.T('a', key='lbl_a',font='consalo 14'), sg.I('', key='edit_a', size=(10,1),pad=(10,10)),
      sg.T('b', key='lbl_b', font='consalo 14'), sg.I('', key='edit_b', size=(10,1),pad=(10,10)),
     sg.T('c', key='lbl_c', font='consalo 14'), sg.I('', key='edit_c', size=(10,1),pad=(10,10))],
    [sg.B('Calculate', key='calc', border_width=5, pad=(10,10))],
     [sg.T('x1', key='lbl_x1', font='consalo 14'), sg.I('', key='x1', size=(15,1),pad=(10,10))],
     [sg.T('x2', key='lbl_x2', font='consalo 14'), sg.I('', key='x2', size=(15,1),pad=(10,10))]
  ]

window = sg.Window('Quadratic solver', layout, size=(400,180))

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break

    if event == 'calc':
        try:
            a = float(values['edit_a'])
        except:
            a = 0
            sg.popup_error("The leading coefficient cannot be zero")
            break
        try:
            b = float(values['edit_b'])
        except:
            b = 0
        try:
            c = float(values['edit_c'])
        except:
            c = 0
       
        x1,x2 = solver(a,b,c)
        window['x1'].update(str(x1))
        window['x2'].update(str(x2))

window.close()
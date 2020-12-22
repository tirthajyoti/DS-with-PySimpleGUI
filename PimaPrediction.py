import PySimpleGUI as sg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def read_table():
    sg.set_options(auto_size_buttons=True)
    layout = [[sg.Text('Dataset (a CSV file)', size=(16, 1)),sg.InputText(),
               sg.FileBrowse(file_types=(("CSV Files", "*.csv"),("Text Files", "*.txt")))],
               [sg.Submit(), sg.Cancel()]]

    window1 = sg.Window('Input file', layout)
    try:
        event, values = window1.read()
        window1.close()
    except:
        window1.close()
        return
    
    filename = values[0]
    
    if filename == '':
        return

    data = []
    header_list = []

    if filename is not None:
        fn = filename.split('/')[-1]
        try:                     
            if colnames_checked:
                df = pd.read_csv(filename, sep=',', engine='python')
                # Uses the first row (which should be column names) as columns names
                header_list = list(df.columns)
                # Drops the first row in the table (otherwise the header names and the first row will be the same)
                data = df[1:].values.tolist()
            else:
                df = pd.read_csv(filename, sep=',', engine='python', header=None)
                # Creates columns names for each column ('column0', 'column1', etc)
                header_list = ['column' + str(x) for x in range(len(df.iloc[0]))]
                df.columns = header_list
                # read everything else into a list of rows
                data = df.values.tolist()
            # NaN drop?
            if dropnan_checked:
                df = df.dropna()
                data = df.values.tolist()
            window1.close()
            return (df,data, header_list,fn)
        except:
            sg.popup_error('Error reading file')
            window1.close()
            return

def show_table(data, header_list, fn):    
    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  font='Helvetica',
                  pad=(25,25),
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=min(25, len(data)))]
    ]

    window = sg.Window(fn, layout, grab_anywhere=False)
    event, values = window.read()
    window.close()

def show_stats(df):
    stats = df.describe().T
    header_list = list(stats.columns)
    data = stats.values.tolist()
    for i,d in enumerate(data):
        d.insert(0,list(stats.index)[i])
    header_list=['Feature']+header_list
    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  font='Helvetica',
                  pad=(10,10),
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=min(25, len(data)))]
    ]

    window = sg.Window("Statistics", layout, grab_anywhere=False)
    event, values = window.read()
    window.close()
    
def sklearn_model(output_var):
    """
    Builds and fits a ML model
    """
    from sklearn.ensemble import RandomForestClassifier
    X = df.drop([output_var], axis=1)
    y = df[output_var]
    
    clf = RandomForestClassifier(n_estimators=20,
                                 max_depth=4)
    clf.fit(X, y)
    #print("Prediction accuracy {}".format(clf.score(X,y)))
    return clf, np.round(clf.score(X,y),3)
    
#=====================================================#
# Define the window's contents i.e. layout
layout = [
        [sg.Button('Load data',size=(10,1), enable_events=True, key='-READ-', font='Helvetica 16'),
        sg.Checkbox('Has column names?', size=(15,1), key='colnames-check',default=True),
        sg.Checkbox('Drop NaN entries?', size=(15,1), key='drop-nan',default=True)], 
         [sg.Button('Show data',size=(10,1),enable_events=True, key='-SHOW-', font='Helvetica 16',),
        sg.Button('Show stats',size=(15,1),enable_events=True, key='-STATS-', font='Helvetica 16',)],
            [sg.Text("", size=(50,1),key='-loaded-', pad=(5,5), font='Helvetica 14'),],
    [sg.Text("Select output column",size=(18,1), pad=(5,5), font='Helvetica 12'),],    
    [sg.Listbox(values=(''), key='colnames',size=(30,3),enable_events=True),],
    [sg.Text("", size=(50,1),key='-prediction-', pad=(5,5), font='Helvetica 12')],
     [sg.ProgressBar(50, orientation='h', size=(100,20), key='progressbar')],
        ]

# Create the window
window = sg.Window('Pima', layout, size=(600,300))
progress_bar = window['progressbar']
prediction_text = window['-prediction-']
colnames_checked = False
dropnan_checked = False
read_successful = False
# Event loop
while True:
    event, values = window.read()
    loaded_text = window['-loaded-']
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-READ-':
        if values['colnames-check']==True:
            colnames_checked=True
        if values['drop-nan']==True:
            dropnan_checked=True
        try:
            df,data, header_list,fn = read_table()
            read_successful = True
        except:
            pass
        if read_successful:
            loaded_text.update("Datset loaded: '{}'".format(fn))
            col_vals = [i for i in df.columns]
            window.Element('colnames').Update(values=col_vals, )
    if event == '-SHOW-':
        if read_successful:
            show_table(data,header_list,fn)
        else:
            loaded_text.update("No dataset was loaded")
    if event=='-STATS-':
        if read_successful:
            show_stats(df)
        else:
            loaded_text.update("No dataset was loaded")
    if event=='colnames':
        if len(values['colnames'])!=0:
            output_var = values['colnames'][0]
            if output_var!='Class variable':
                sg.Popup("Wrong output column selected!", title='Wrong',font="Helvetica 14")
            else:
                prediction_text.update("Fitting model...")
                for i in range(50):
                    event, values = window.read(timeout=10)
                    progress_bar.UpdateBar(i + 1)
                _,score = sklearn_model(output_var)
                prediction_text.update("Accuracy of Random Forest model is: {}".format(score))
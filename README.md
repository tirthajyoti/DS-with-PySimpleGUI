# DS-with-PySimpleGUI
Data science GUI programs with awesome `PySimpleGUI` package.

## What is `PySimpleGUI` and what is this repo?

As per their website, ___"Python GUI For Humans - Transforms tkinter, Qt, Remi, WxPython into portable people-friendly Pythonic interfaces"___. In this repo, I specifically focus on creating simple demo programs related to data science (simple analytics, statistical modeling and visualizations, basic machine learning) using this powerful GUI building tool.

## Requirements

Install `PySimpleGUI` by,
```
pip install pysimplegui
```

You will also need,

- Numpy
- Pandas
- Matplotlib
- Scikit-learn
- Seaborn

etc. to run the demo codes.

## Demo of `SimpleDataFrame.py` (Pandas DataFrame app)

There are both Jupyter notebooks and .PY scripts. The simplest way to run a GUI is to execute the .PY scripts, e.g.
```
python SimpleDataFrame.py
```

### Input file
At the start, it will ask you for a dataset file (a CSV)

![input](https://raw.githubusercontent.com/tirthajyoti/DS-with-PySimpleGUI/main/images/SimpleDataFrame-0.PNG)

### File browser
When you click on the 'Browse' button, it will show a file browser dialog first. Make sure you select the correct dataset for this demo from under the `data` directory.

![browser](https://raw.githubusercontent.com/tirthajyoti/DS-with-PySimpleGUI/main/images/SimpleDataFrame-1.PNG)

### Prompts
After you select the `cars.csv`, you will see other prompts popping up,

![prompts](https://raw.githubusercontent.com/tirthajyoti/DS-with-PySimpleGUI/main/images/SimpleDataFrame-6.png)
### Dataset
If you click 'Yes' on that last prompt, you will see the dataset that was read in a new window,

![data](https://raw.githubusercontent.com/tirthajyoti/DS-with-PySimpleGUI/main/images/SimpleDataFrame-5.PNG)
### Descriptive stats
After you close that window, a new popup will ask if you want to see the descriptive statistics about this dataset. If you click 'Yes', then you will see something like this,

![stat](https://raw.githubusercontent.com/tirthajyoti/DS-with-PySimpleGUI/main/images/SimpleDataFrame-7.PNG)
### A plot
After you close that window, another popup will ask if you want to see a sample plot. If you click 'Yes', then you will see something like this,

![plot](https://raw.githubusercontent.com/tirthajyoti/DS-with-PySimpleGUI/main/images/SimpleDataFrame-8.PNG)
### Play with the notebooks if you like
If you want to experiment with the code, you can look at the Notebooks and play with them.

## Standalone windows app demo (`FontUpdate.py`)

Just run with `python FontUpdate.py` command and you will see this window pop up where you can dynamically update the font of the text. Here is the demo video,

![fontupdate](https://raw.githubusercontent.com/tirthajyoti/DS-with-PySimpleGUI/main/images/FontUpdate.gif)

## PySimpleGUI website

[Read the docs here](https://pysimplegui.readthedocs.io/en/latest/)

[Github repo](https://github.com/PySimpleGUI/PySimpleGUI)

[Cool demos](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms)


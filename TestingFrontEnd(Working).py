# These are the Modules
import re
import csv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
# These are the UI Parts
# The Software
theSoftware = Tk()
theSoftware.title('The Timings of Employee into seperate CSV')
theSoftware.geometry('500x500')

# the Variables
lottaMonthTime = StringVar()
lottaMonthTime.set('Choose your Month')

# The Frames
frameKing = Frame(theSoftware)
frameQueen = Frame(frameKing)
framePrince = Frame(frameQueen)
frameAdvisor = Frame(framePrince)
frameCommander = Frame(frameAdvisor)
frameKing.pack(side = TOP)
frameQueen.pack(side = TOP)
framePrince.pack(side = TOP)
frameAdvisor.pack(side = TOP)
frameCommander.pack(side = TOP)
# The Buttons and Label
# The Label
theCSVFileLabel = Label(frameAdvisor, text = 'Please select your CSV File: ')
theTargetFolderLabel = Label(framePrince, text = 'Please select your Target Folder: ')
theMonthLabel = Label(frameQueen, text = 'Please select the Month: ')
theCSVFileLabel.pack(side = LEFT)
theTargetFolderLabel.pack(side = LEFT)
theMonthLabel.pack(side = LEFT)
# The Button
theCSVFileButton = Button(frameAdvisor, text = 'CSV File')
theTargetFolderButton = Button(framePrince, text = 'Target Folder')
theMonthMenuButton = OptionMenu(frameQueen, lottaMonthTime, 'Choose your Month', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
theStartProcessButton = Button(frameKing, text = 'Start Process')
theCSVFileButton.pack()
theTargetFolderButton.pack()
theMonthMenuButton.pack()
theStartProcessButton.pack()


theSoftware.mainloop()
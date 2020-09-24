# These are the Modules 
import re
import csv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# These are the functions
def findMyCsvFile():
	global csvFileDirectory
	csvFileDirectory = filedialog.askopenfile(initialdir = '/', title = 'Select A CSV file', filetypes = (('CSV Files', '*.csv'), ('All Files', '*.')))
	theCSVFileLabel.configure(text = 'File Selected!')

def findTargetFolder():
	global targetFolderDirectory
	targetFolderDirectory = filedialog.askdirectory(initialdir = '/', title = 'Select A Folder')
	theTargetFolderLabel.configure(text = 'Folder Selected!')

def theCSVProcessor():
	# this is just to grab the string path and turn it into an actual path!
	global lottaMonthTime
	global targetFolderDirectory
	global csvFileDirectory
	theMonthTime = lottaMonthTime.get()
	theTargetFolderDirectory = targetFolderDirectory.replace('/', '\\')
	theCSVFileDirectory = csvFileDirectory.name.replace('/', '\\')
	# Heres the actual code
	# The Opening of Files
	edtechAttendance_data = open(theCSVFileDirectory, encoding = 'utf-8')
	edtechAttendance_csv_data = csv.reader(edtechAttendance_data)
	edtech_dataLines = list(edtechAttendance_csv_data)
	# This is where we store the important regular expressions
	patternTime = r'\d\d:\d\d\sam\s-\s\d\d:\d\d\spm'
	patternDay = r'\d\d:\d\d\sam'
	patternNight = r'\d\d:\d\d\spm'
	patternName = r'[A-Za-z]'
	employTime = 1

	# This is the program
	for l in edtech_dataLines:
		employTime = 1
		NameOfEmployee = theTargetFolderDirectory + '\\' + l[0] + '.csv'
		theCsvFile = open(NameOfEmployee, 'w', newline = '')
		edtechCsv_typist = csv.writer(theCsvFile, delimiter = ',')
		for l_check in l:
			day_and_month = str(employTime) + f' - {theMonthTime}'
			if l_check == '':
				edtechCsv_typist.writerow([l[0], day_and_month,'In Time', 'No time Obtained!'])
				edtechCsv_typist.writerow([l[0], day_and_month,'Out Time', 'No time Obtained!'])
				employTime = employTime + 1
			chIfTime = re.search(patternTime, l_check)
			if type(chIfTime) == re.Match:
				chIfDay = re.search(patternDay, chIfTime.group())
				chIfNight = re.search(patternNight, chIfTime.group())
				if type(chIfDay) and type(chIfNight) == re.Match:
					edtechCsv_typist.writerow([l[0], day_and_month, 'In Time', chIfDay.group()])
					edtechCsv_typist.writerow([l[0], day_and_month, 'Out Time', chIfNight.group()])
					employTime = employTime + 1
			if employTime > 16:
				employTime = 1

	messagebox.showinfo('Process Completed', 'The Process is completed,\n Please check your Target Folder')



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
theCSVFileButton = Button(frameAdvisor, text = 'CSV File', command = findMyCsvFile)
theTargetFolderButton = Button(framePrince, text = 'Target Folder', command = findTargetFolder)
theMonthMenuButton = OptionMenu(frameQueen, lottaMonthTime, 'Choose your Month', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
theStartProcessButton = Button(frameKing, text = 'Start Process', command = theCSVProcessor)
theCSVFileButton.pack()
theTargetFolderButton.pack()
theMonthMenuButton.pack()
theStartProcessButton.pack()

theSoftware.mainloop()

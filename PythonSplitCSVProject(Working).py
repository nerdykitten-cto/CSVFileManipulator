# These are the Modules
import re
import csv

# These are the variables
# this is where we open the file and read its content
edtechAttendance_data = open('Edtech-Attendance.csv', encoding = 'utf-8')
edtechAttendance_csv_data = csv.reader(edtechAttendance_data)
edtech_dataLines = list(edtechAttendance_csv_data)

# This is where we store the important regular expressions
patternTime = r'\d\d:\d\d\sam\s-\s\d\d:\d\d\spm'
patternDay = r'\d\d:\d\d\sam'
patternNight = r'\d\d:\d\d\spm'
patternName = r'[A-Za-z]'

# This is the File directory in which we store the employee info
thefileDirectory = 'C:\\Users\\S.AliAhsan\\Documents\\BilalFiles\\PythonScripts\\CoolPythonProjectsOfAbbu\\EmployeeTimings'

# This is the day counter for every one of the employee
employTime = 1

# This is the program
for l in edtech_dataLines:
    employTime = 1
    NameOfEmpoyee = thefileDirectory + '\\' + l[0] + '.csv'
    theCsvFile = open(NameOfEmpoyee, 'w', newline = '')
    edtechCsv_typist = csv.writer(theCsvFile, delimiter = ',')
    for l_check in l:
        day_and_month = str(employTime) + ' - Aug'
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


# PS, If it is messy, don't blame me!!!

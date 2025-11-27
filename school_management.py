#class for student course details
class Details:
    def __init__(self,CN,Lvl,CWA,Sts,Credit):
        self.CourseName=CN   # course enrolled
        self.Level=Lvl                   # year level
        self.CWA=CWA             # cumulative weight average
        self.Status=Sts              # fulltime or parttime
        self.Credit=Credit         # credits earned

class Student:
    def _init_(self,ID,Fn,Ln):
        self.StudentID=ID   # student id
        self.FirstName=Fn # firstname
        self.LastName=Ln  # student's lastname

import csv      # import the CSV module to handle reading and writing CSV files
#function to add student record to the data.csv
def AddStudent():
    studentId=input("Enter ID :")                                           # get student id
    firstname=input("Enter FirstName :")                         # get the firstname
    FamilyName=input("Enter FamilyName :")                # get the familyname
    CourseEnrolled=input("Enter CourseEnrolled :")   # the course the student is enrolled in
    # validate level 1-4
    while True:
        YearLevel=int(input("Enter YearLevel 1-4:"))
        if YearLevel>=1 and YearLevel<=4:
            break
    # validate CWA btwn 0-100 can be  decimal
    while True:
        
        CWA=int(input("Enter CWA 0-100 :"))
        if  CWA>=0 and CWA<=100:
             break
    # validate status must be FT or PT only
    while True:
        Status=input("Enter Status FT/PT :").upper()
        if Status in ["FT",  "PT"]:
            break
     # validate credits earned must be 0-400   
    while True:
        CreditsEarned=int(input("Enter CreditsEarned 0-400 :"))
        if  CreditsEarned >=0 and CreditsEarned<=400:
            break
    # create a list of each student's data (record)
    newrecord=[studentId, firstname,FamilyName,CourseEnrolled, YearLevel, CWA, Status, CreditsEarned]
    #open the file in append mode & write the newrecord to it 
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)           # creates a csv writer object
        writer.writerow(newrecord) # writes the student record as one row 
        print("record added!")  # for confirmation

    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    print("Current CSV Data: ")
    print(data)
    print("Data type of whole file:", type(data))
    print("Data type in one row:", type(data[0]))


    
# Edit Student

def EditStudent():
    sid = input("Enter ID to edit: ")
    rows = [] #will collect all the rows updated or not
    found = False #to track if sid matches the row were at

    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == sid:   # match by StudentID
                    print("Leave blank to keep old value")
                    #ask user to enter thei new details or keep the old ones
                    row[1] = input("FirstName ({row[1]}): ") or row[1]
                    row[2] = input("LastName ({row[2]}): ") or row[2]
                    row[3] = input("Course ({row[3]}): ") or row[3]
                    row[4] = input("YearLevel ({row[4]}): ") or row[4]
                    row[5] = input("CWA ({row[5]}): ") or row[5]
                    row[6] = input("Status ({row[6]}): ") or row[6]
                    row[7] = input("Credits ({row[7]}): ") or row[7]
                    found = True
                rows.append(row)

        # Write back all rows (including updated one)
        with open("data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        if found:
            print("Record updated!")
        else:
            print("️ Student not found!")
    except FileNotFoundError:
        print(" No records yet.")

def averageCWA():
    DistinctCoarses=[]
    AvgCWAs=[]
    allData=[]
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:   # skip empty rows
                    allData.append(row)
                    cos=row[3]
                    if cos not in DistinctCoarses:
                        DistinctCoarses.append(cos)
            for cos in DistinctCoarses:
                totalperCos=0
                count=0
                for studentData in allData:
                    if cos==studentData[3]:
                        cwa=int(studentData[5])
                        print(cwa)
                        totalperCos =totalperCos+cwa
                        count+=1
                AvgCWAs.append(totalperCos/count)
            for i in range  (len(DistinctCoarses)):
                print(DistinctCoarses[i],AvgCWAs[i])
      
            
                        
    except FileNotFoundError:
        print("️ No records yet.")
    print (DistinctCoarses)
    
#viewall
def ViewAll():
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            print(reader)
            for row in reader:
                if row:   # skip empty rows
                    print(row)
    except FileNotFoundError:
        print("️ No records yet.")
    print()

#filter by course
def FilterByCourse():
    course = input("Enter course to filter: ")
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[3].lower() == course.lower(): #if row skips empty rows 
                    print(row)
    except FileNotFoundError:
        print("No records yet.")
  

##filter by status
def FilterByStatus():
    status = input("Enter status (FT/PT): ").upper()
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[6] == status:
                    print(row)
    except FileNotFoundError:
        print("No records yet.")


## highest CWA
def HighestCWA():
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row]
            if rows:
                top = max(rows, key=lambda row: float(row[5]))
                print(" Highest CWA:", top)
    except FileNotFoundError:
        print(" No records yet.")
 

###AverageCWAperCourse
##def AverageCWAperCourse():


#CreditAnalysis
def CreditAnalysis():
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            graduate = [row for row in reader if row and int(row[7]) >= 400]
            if graduate:
                print("Eligible for graduation:")
                for row in graduate:
                    print(row)
            else:
                print("No students eligible yet.")
    except FileNotFoundError:
        print("No records yet.")



## MAIN MENU

while True: 
    print("=============================================")
    print("   Welcome to Student Central")
    print("=============================================")
    print("1> Add new student.")
    print("2> Edit student.")
    print("3> View all students.")
    print("4> Filter by course.")
    print("5> Filter by status.")
    print("6> Highest CWA.")
    print("7> Average CWA for each course.")
    print("8> Credit Analysis.")
    print("9> Exit.")
        
    choice = input("Enteryour  choice: ")

    if choice == "1":
        AddStudent()
    elif choice == "2":
        EditStudent()
    elif choice == "3":
        ViewAll()
    elif choice == "4":
        FilterByCourse()
    elif choice == "5":
        FilterByStatus()
    elif choice == "6":
        HighestCWA()
    elif choice == "7":
        averageCWA()
    elif choice == "8":
        CreditAnalysis()
    elif choice == "9":
        print(" Exiting program...")
        break
    else:
        print(" Invalid choice, try again!")





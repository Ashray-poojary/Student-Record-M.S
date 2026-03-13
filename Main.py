import os
import getpass as g
#autorization setup part
if not os.path.exists(".data.txt"):
    print("Set up your system access")
    user = input("Enter username:")
    passw = g.getpass("Enter password:")
    cpassw = g.getpass("Confirm password : ")
    if (passw == cpassw):
        f1 = open(".data.txt","w")
        f1.write(user + "\n")
        f1.write(passw)
        f1 = open(".data.txt","r")
        r_user = f1.readline().strip()
        r_passw = f1.readline().strip()
        f1.close()
    else:
        print("put your glasses, then try.")
        exit(0)
else:
    f = open(".data.txt","r")
    r_user = f.readline().strip()
    r_passw = f.readline().strip()
    f.close()

i = 0
#authorization part
while(True):
    print("Authentication.....")
    c_user = input("username : ")
    c_passw = g.getpass("password : ")
    
    if(c_user == r_user and c_passw == r_passw):
        print("granted")
        break
    else:
        print("denied")
        i = i+1
        if(i == 3):
            print("exiting.....!!!!!")
            exit(0)
            
#starting the program with class,list,function

class Student:
    def __init__(self, roll, name, phone):
        self.roll = roll
        self.name = name
        self.phone = phone
        
students = []

def add_student():
    lp = input("Enter how many records to add : ")
    lp = int(lp)
    for i in range(lp):
        #roll uniqueness code has to be added
        
        roll = input("Enter Roll No : ")
        name = input("Enter Name : ")
        phone = input("Enter Phone : ")

        s = Student(roll, name, phone)
        students.append(s)

        print("Student Added Successfully...\n")
    
    
def delete_student():
    if not students:
        print("No records available to delete")
        return
    
    roll = input("Enter Roll No to delete : ")

    for s in students:
        if s.roll == roll:
            students.remove(s)
            print("Student Deleted\n")
            return

    print("Student Not Found\n")
    
def display_students():
    if not students:
        print("No records found\n")
        return

    print("\nStudent List")
    for s in students:
        print(" Roll : ", s.roll, "\t\tName : ", s.name, "\t\tPhone : ", s.phone)
    print()
    
def search_student():
    if not students:
        print("No records available to search")
        return
    
    roll = input("Enter Roll No to search : ")

    for s in students:
        if s.roll == roll:
            print("\nStudent Found")
            print("Roll : ", s.roll)
            print("Name : ", s.name)
            print("Phone : ", s.phone)
            print()
            return

    print("Student Not Found!\n")
    
#menu part for operation 
print("student record management system")
print("----------------------------------------------------------->")
while(1):
    print("1.Add record")
    print("2.Delete record")
    print("3.Display record")
    print("4.search record")
    print("5.Exit")
    print("------------------------------>")
    print("Enter your choice...")
    ch=input()
    if ch.isdigit():
        ch = int(ch)
        print("--------------------->")
        if (ch == 1):
            add_student()
            print("added")
        elif (ch == 2):
            delete_student()
            print("deleted")
        elif (ch == 3):
            display_students()
            print("display")
        elif (ch == 4):
            search_student()
        elif (ch == 5):
            exit(0)
        else:
            print("Invlid option")
    else:
        print("Enter your choice from  (1,2,3,4,5) : ")

#thus program can only store data during its running or execution not permanently 
#hence its fast for add,delete,search,display operations


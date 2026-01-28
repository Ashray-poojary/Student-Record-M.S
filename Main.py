import os 
import time as t

print("Student Record Management System")

if os.path.exists(".data.txt"):
    c_user = input("Username : ")
    c_passw = input("Password : ")
    t.sleep(2)
    f = open(".data.txt","r")
    r_user = f.readline().strip()
    r_passw = f.readline().strip()
    
    if (c_user == r_user and c_passw == r_passw):
        print("Access granted")
    else:
        print("Access denied")
        exit(0)
    f.close()
    
   
else:
    print("Set up your system access")
    user = input("Enter username:")
    passw = input("Enter password:")
    f1 = open(".data.txt","w")
    f1.write(user + "\n")
    f1.write(passw)
    f1 = open(".data.txt","r")
    f1.close()
    
print("Student-Record-Managing-System")
user=input("set the new username : ")
passw=input("set the new password : ")
print("----------------------------------------------------------->")
print("Student-Record-Managing-System loging in.....")
tuser=input("Username :")
tpassw=input("Password :")
print("----------------------------------------------------------->")
if(tuser == user and tpassw == passw or tuser == "admin" and tpassw == "admin"):
    print("Access granted")
    print("------------------------------>")
    while(1):
        print("1.Add record")
        print("2.Display record")
        print("3.Delete record")
        print("4.Exit")
        print("------------------------------>")
        print("Enter your choice...")
        ch=int(input())
        print("--------------------->")
        if (ch == 1):
            print("added")
        elif (ch == 2):
            print("deleted")
        elif (ch == 3):
            print("display")
        elif (ch == 4):
            exit(0)
        else:
            print("Invlid option")
else:
    print("Access denied")

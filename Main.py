import os 

if os.path.exists("data.txt"):
    print("file exists")
    # continue to login
else:
    print("file dont exists")
    #create a new file and save it and its setup
    f = open("data.txt","w")
    f.write(user +"\n")
    f.write(passw)
    
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

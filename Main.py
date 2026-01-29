import os 

if not os.path.exists(".data.txt"):
    print("Set up your system access")
    user = input("Enter username:")
    passw = input("Enter password:")
    f1 = open(".data.txt","w")
    f1.write(user + "\n")
    f1.write(passw)
    f1 = open(".data.txt","r")
    r_user = f1.readline().strip()
    r_passw = f1.readline().strip()
    f1.close()
else:
    f = open(".data.txt","r")
    r_user = f.readline().strip()
    r_passw = f.readline().strip()
    f.close()

i = 0

while(True):
    print("Authentication.....")
    c_user = input("username : ")
    c_passw = input("password : ")
    
    if(c_user == r_user and c_passw == r_passw):
        print("granted")
        break
    else:
        print("denied")
        i = i+1
        if(i == 3):
            print("exiting.....!!!!!")
            exit(0)
            
print("student record management system")
print("----------------------------------------------------------->")
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



username  = input("enter user name : ")
password = input("enter password : ")

if(username == "admin" and password == "1234"):
    print("logged in")
elif(username!="admin"):
    print("wrong username")
else:
    print("wrong password")
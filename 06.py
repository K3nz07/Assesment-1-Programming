password =("12345") 
code   = False
while code == False:
    inputpassword = input("Enter your passowrd:")
    if inputpassword == password:
        print (" Access granted")
        code = True
        

    else:
        print("Incorrect password, Access denied")

#A user enters a password. Check if the password length is at least 8 characters. If yes, print 
#"Strong", otherwise "Weak"
password = input("Enter the password : ")
if len(password)>=8:
    print("strong")
else:
    print("weak")
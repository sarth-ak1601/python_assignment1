# A user enters age. Print "Child" if age < 13, "Teenager" if 13–19, else "Adult".
age = int(input("Enter the age : "))
if age < 13 :
    print("Child")
elif age > 19 :
    print("Adult")
else:
    print("Teenager")
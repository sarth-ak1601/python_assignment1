#Take two strings as input. Check which one is lexicographically larger (dictionary order) using if-else without using built-in functions. 
a = input("Enter first string: ") 
b = input("Enter second string: ") 
if a > b: 
 print(a, "is larger") 
elif a < b: 
 print(b, "is larger") 
else: 
 print("Both are equal") 
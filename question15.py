# Input a string. If its first and last characters are the same, print "Match", otherwise "No Match".
text = input("Enter your string: ")
if text[0]==text[-1] :
    print("Match")
else:
    print("No match")
# Input a word. If the word is a palindrome (same forward and backward), print "Palindrome",otherwise "Not Palindrome".
word = input("Enter the word : ")
if word==word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
    


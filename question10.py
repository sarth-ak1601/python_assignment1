#Take a string input and print the middle character (if length is odd) or middle two characters 
# (if length is even).
text = input("Enter a string: ")
length = len(text)

if length % 2 == 0:
    mid = length // 2
    print("Middle characters:", text[mid - 1:mid + 1])
else:
    mid = length // 2
    print("Middle character:", text[mid])

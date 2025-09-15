# A user enters their name. Print their name in uppercase and lowercase using slicing only.
name = input("Enter your name: ")

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

uppercase_name = ''
for char in name:
    if char in lower:
        index = lower.index(char)
        uppercase_name += upper[index]
    else:
        uppercase_name += char

lowercase_name = ''
for char in name:
    if char in upper:
        index = upper.index(char)
        lowercase_name += lower[index]
    else:
        lowercase_name += char

print("Uppercase:", uppercase_name)
print("Lowercase:", lowercase_name)

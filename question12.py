# A user enters a sentence. Print the first half and second half separately using slicing. 
sentence = input("Enter a sentence: ")

mid = len(sentence) // 2

first_half = sentence[:mid]
second_half = sentence[mid:]

print("First half:", first_half)
print("Second half:", second_half)

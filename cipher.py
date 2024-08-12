# add your code here
alphabet = 'abcdefghijklmnopqrstuvwxyz'

prompt = input("Enter a message: ")
shift = int(+5)
length = len(prompt)

output = ""

for x in range(length):
    letter = prompt[x]
    location = alphabet.find(letter)
    shift_location = (location + shift) % 26
    output += alphabet[shift_location]
    
print(output)
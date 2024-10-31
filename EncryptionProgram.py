import random
import string

char = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(char)

keys = chars.copy()

random.shuffle(keys)

# print(f"chars : {chars}")
# print(f"keys : {keys}")

#ENCRPYT

plain_text = input('Enter a message to Encrpyt : ')
cipher_text = ''

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f'The plain text is : {plain_text}')
print(f'The cypher_text is : {cipher_text}')


#DECRYPT

cipher_text = input('Enter a message to decrypt : ')
plain_text = ''

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f'The cypher_text is : {cipher_text}')
print(f'The plain text is : {plain_text}')

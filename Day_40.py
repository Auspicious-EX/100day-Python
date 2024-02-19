# DAY 40 : Exercise 4: Secret Code Language

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode



import random

def encode_word(word):
    if len(word) >= 3:
        first_letter = word[0]
        modified_word = word[1:] + first_letter
        code = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        return code + modified_word + code
    else:
        return word[::-1]

def decode_word(word):
    if len(word) < 3:
        return word[::-1]
    else:
        word = word[3:-3]
        last_letter = word[-1]
        modified_word = last_letter + word[:-1]
        return modified_word

def encode_message(message):
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)

def decode_message(message):
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

choice = input("Do you want to code or decode? (code/decode): ").lower()

if choice == 'code':
    message = input("Enter the message to encode: ")
    encoded_message = encode_message(message)
    print("Encoded message:", encoded_message)
elif choice == 'decode':
    message = input("Enter the message to decode: ")
    decoded_message = decode_message(message)
    print("Decoded message:", decoded_message)
else:
    print("Invalid choice! Please enter 'code' or 'decode'.")

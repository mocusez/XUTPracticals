"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
print("Password Generator")


LETTERS = "abcdefghijklmnopqrstuvwyz"
LETTERS_UPPER = "ABCDEFGHIJKLMONPQRSTUVWYXZ"
NUMBERS = "1234567890"
LENGTH = 4
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
password = ""

password_length = int(input('How long should the password be? '))

while password_length < LENGTH:
    print("Error, Password must be atleast {} characters long".format(LENGTH))
    password_length = int(input("Please re-enter the length of the password: "))

password = password + (random.choice(LETTERS_UPPER))
password = password + (random.choice(LETTERS))
password = password + (random.choice(NUMBERS))
password = password + (random.choice(SPECIAL_CHARACTERS))
for i in range(4, password_length):
    x = random.randint(1, 4)
    if x == 1:
        password += (random.choice(LETTERS_UPPER))
    elif x == 2:
        password += (random.choice(LETTERS))
    elif x == 3:
        password += (random.choice(NUMBERS))
    else:
        password += (random.choice(SPECIAL_CHARACTERS))

shuffled_password = ''.join(random.sample(password, len(password)))

print(shuffled_password)

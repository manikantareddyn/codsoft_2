# Password Generation

# Importing required libraries
import random
import string

# Defining a function named password_generator
def password_generator(length):
    characters= string.ascii_letters +string.digits + string.punctuation

# It produces lots of passwords upto getting a required password
    while True:
        
# It takes password length of  different characters and store in password
        password=''.join(random.choice(characters) for i in range(length))
# Checking for all the characters are present in password
        if (any(char.isupper() for char in password)   and  any(char.islower() for char in password)   and  any(char.isdigit() for char in password)   and any(char in string.punctuation for char in password)  ):
            return password
#Take length of password from user
length=abs(int(input('Enter length of password for Generating :')))
# Printing generated password
print('Password :',password_generator(length))
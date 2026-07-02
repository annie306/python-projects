import secrets
import string

characters =string.ascii_letters+string.digits + string.punctuation

length = int(input("Enter password length (min 15 recommended): "))

if length<4:
    print("Password too short.")
else:
    password = ''.join(secrets.choice(characters) for i in range(length))
    print("Your generated password is:", password)

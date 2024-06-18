import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = 6  
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)

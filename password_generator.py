# Password Generator
import random, string
def generate_password(length=12):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))
print("Generated password:", generate_password())

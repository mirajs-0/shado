# LESSON 2 - Python Basics
# Shado Project

# ------------------
# VARIABLES
# ------------------

name = "Shado"
version = 1
is_active = "True"

print(name)
print(version)
print(is_active)

# ------------------
# VARIABLES
# ------------------

def greet_user(username):
    print("Welcome back " + username)
    print("Shado is watching.")

greet_user("Miraj")

# ------------------
# CONDITIONS
# ------------------

def check_user(username):
    authorized_user = "Miraj"

    if username == authorized_user:
        print("Access granted. Welcome " + username)
    else:
        print ("Unknown user detected. Access Denied.")

check_user("Miraj")
check_user("John")

# ------------------
# LOOPS
# ------------------

access_attempts = ["Miraj", "John", "Anna", "Miraj"]

for user in access_attempts:
    check_user(user)
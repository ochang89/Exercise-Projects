from pw_gen import *

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def create_password(self):
        self.password = main()
        return self.password

emp1 = User('username', 'password', 'email')

emp1.create_password()
print(f"Your new password is: {emp1.password}")


class UserNotFoundError(Exception):
    pass

class WrongPasswordError(Exception):
    pass

class UserExistsError(Exception):
    pass

class UserAuth:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            raise UserExistsError("Użytkownik już istnieje!")
        self.users[username] = password
        return "Rejestracja udana!"

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError("Użytkownik nie istnieje!")
        if self.users[username] != password:
            raise WrongPasswordError("Błędne hasło!")
        return "Logowanie udane!"

# Przykład użycia
auth = UserAuth()

# Poprawna rejestracja
try:
    print(auth.register("user1", "password123"))
except UserExistsError as e:
    print(e)

# Próba rejestracji istniejącego użytkownika
try:
    print(auth.register("user1", "password123"))
except UserExistsError as e:
    print(e)

# Udane logowanie i błędne hasło
try:
    print(auth.login("user1", "password123"))  # Logowanie udane!
    print(auth.login("user1", "wrongpass"))    # Błąd: WrongPasswordError
except UserNotFoundError as e:
    print(e)
except WrongPasswordError as e:
    print(e)

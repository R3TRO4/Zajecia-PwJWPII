
"""
Zaprojektuj klasę UserAuth, która będzie symulować system logowania użytkownika w
aplikacji mobilnej.
1. Stwórz klasę UserAuth, która:
a. Ma atrybut users, będący słownikiem ({login: hasło})
b. Metodę login(username, password), sprawdzającą poprawność
danych logowania
2. Stwórz własne wyjątki UserNotFoundError i WrongPasswordError
3. Obsłuż wyjątki:
a. UserNotFoundError – jeśli użytkownika nie ma w systemie
b. WrongPasswordError – jeśli hasło jest niepoprawne
auth = UserAuth({"admin": "1234", "user": "abcd"})
try:
auth.login("admin", "1234") # Sukces
auth.login("unknown", "pass") # Powinien rzucić UserNotFoundError
auth.login("user", "wrongpass") # Powinien rzucić WrongPasswordError
except Exception as e:
print(f"Błąd: {e}")
"""

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

import hashlib
import os


class passwordHandling:
    def __init__(self):
        self.password = None
        self.salt = None

    def savedPassword(self, userPassword):
        salt = os.urandom(16)
        salted_password = salt + userPassword.encode()
        hashing = hashlib.sha256(salted_password).hexdigest()
        self.password = hashing
        self.salt = salt

    def verifyPassword(self, attempt):
        if self.password is None:
            return False
        salting = self.salt
        attemptEncode = salting + attempt.encode()
        attemptHash = hashlib.sha256(attemptEncode).hexdigest()
        return self.password == attemptHash

passwordAttempt = passwordHandling()
passwordAttempt.savedPassword(input())
print(passwordAttempt.verifyPassword(input()))


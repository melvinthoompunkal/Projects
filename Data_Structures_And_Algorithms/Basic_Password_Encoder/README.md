# Simple Password Hasher in Python

This is a lightweight example demonstrating how to securely store and verify passwords using **SHA-256** and **salting** in Python. It's meant for learning and small-scale use only — not production-ready security!

---

## Features

- Hashes passwords using SHA-256
- Adds a random 16-byte salt to defend against rainbow table attacks
- Verifies a password against the stored salted hash


---

## How It Works

1. **Save a password:**
   - Generate a random salt
   - Combine it with the user's password
   - Hash the combination using SHA-256
   - Store both the salt and hash

2. **Verify a password:**
   - Combine the stored salt with the input attempt
   - Hash it and compare to the stored hash

Author - Melvin Thoompunkal

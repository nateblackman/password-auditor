import hashlib

BREACH_FILE = "breached_passwords.txt"

def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def check_breach(password_hash):
    """Checks if the hashed password is in the breached passwords file."""
    try:
        with open(BREACH_FILE, "r") as f:
            breached_hashes = f.read().splitlines()
        return password_hash in breached_hashes
    except FileNotFoundError:
        return False
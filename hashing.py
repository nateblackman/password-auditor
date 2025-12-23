import hashlib
import requests

HIBP_API_URL = "https://api.pwnedpasswords.com/range/"

def hash_password_sha1(password):
    return hashlib.sha1(password.encode()).hexdigest().upper()

def check_breach(password):
    sha1_hash = hash_password_sha1(password)
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    response = requests.get(HIBP_API_URL + prefix)

    if response.status_code != 200:
        return False

    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return True

    return False

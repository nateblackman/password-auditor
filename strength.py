import re

COMMON_WORDS = ["password", "admin", "welcome", "qwerty", "letmein"]

def analyze_password(password):
    issues = []

    if len(password) < 12:
        issues.append("Password is too short; it should be at least 12 characters long.")

    if password.islower() or password.isupper():
        issues.append("Password should include both uppercase and lowercase letters.")

    if not re.search(r"[0-9]", password):
        issues.append("Password should include at least one digit.")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("Password should include at least one special character.")

    for word in COMMON_WORDS:
        if word in password.lower():
            issues.append(f"Password should not contain common words like '{word}'.")
            break
    
    rating = "Strong" if not issues else "Weak"

    return {
        "rating": rating,
        "issues": issues
    }

from strength import analyze_password
from hashing import hash_password, check_breach
from report import generate_report

def main():
    password = input("Enter the password to audit: ")
    
    strength = analyze_password(password)
    hashed = hash_password(password)
    breached = check_breach(hashed)
    
    report = generate_report(password, strength, breached)
    print(report)

if __name__ == "__main__":
    main()

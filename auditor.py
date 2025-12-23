from strength import analyze_password
from hashing import check_breach
from report import generate_report

def main():
    password = input("Enter password to audit: ")

    analysis = analyze_password(password)
    breached = check_breach(password)

    report = generate_report(password, analysis, breached)
    print(report)

if __name__ == "__main__":
    main()


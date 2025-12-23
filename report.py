import json

def generate_report(password, analysis, breached):
    report = {
        "strength": analysis["rating"],
        "issues": analysis["issues"],
        "breached": breached
    }

    output = "\nPassword Security Report\n"
    output += "-------------------------\n"
    output += f"Strength: {analysis['rating']}\n"

    if analysis["issues"]:
        output += "Issues:\n"
        for issue in analysis["issues"]:
            output += f"- {issue}\n"
    else:
        output += "No weaknesses detected\n"

    if breached:
        output += "\n❌ Password found in known breach database\n"
    else:
        output += "\n✅ Password not found in breach database\n"

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    return output
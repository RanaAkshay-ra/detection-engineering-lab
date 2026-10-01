alert = {
    "device": "LAB-WINDOWS-01",
    "user": "akshay",
    "process": "powershell.exe",
    "command_line": "powershell.exe -EncodedCommand TEST",
    "severity": "medium"
}

print("=== SOAR TRIAGE PLAYBOOK ===")

print(f"Device: {alert['device']}")
print(f"User: {alert['user']}")
print(f"Process: {alert['process']}")
print(f"Command: {alert['command_line']}")
print(f"Severity: {alert['severity']}")

if "EncodedCommand" in alert["command_line"]:

    print()
    print("[DETECTION] Encoded PowerShell detected")

    print("[ACTION 1] Collect process tree")
    print("[ACTION 2] Collect process hash")
    print("[ACTION 3] Review network connections")
    print("[ACTION 4] Check user activity")
    print("[ACTION 5] Create SOC investigation")
    print("[ACTION 6] Notify analyst")

else:

    print("No suspicious PowerShell behaviour detected")

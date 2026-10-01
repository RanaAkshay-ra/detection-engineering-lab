from pathlib import Path
import sys
import yaml


REQUIRED_FIELDS = [
    "title",
    "logsource",
    "detection"
]


def test_rule(path):
    print(f"Checking: {path}")

    with open(path, "r", encoding="utf-8") as file:
        rule = yaml.safe_load(file)

    for field in REQUIRED_FIELDS:
        if field not in rule:
            raise ValueError(
                f"{path}: missing required field '{field}'"
            )

    if "condition" not in rule["detection"]:
        raise ValueError(
            f"{path}: detection does not contain condition"
        )

    print("PASS")


rule_files = Path("rules").rglob("*.yml")

failed = False

for rule_file in rule_files:
    try:
        test_rule(rule_file)

    except Exception as error:
        failed = True
        print(f"FAIL: {error}")


if failed:
    sys.exit(1)

print("All detection rules passed.")

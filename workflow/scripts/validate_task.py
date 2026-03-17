#!/usr/bin/env python3
"""
validate_task.py — Task file completeness validator.

Checks that a TASK-NNN.md file has all required fields populated with
real values (not template placeholders) and a valid status.

Usage:
    python validate_task.py <path-to-TASK-NNN.md>
    python validate_task.py --all   (validates all tasks in memory-bank/tasks/)

Exit codes:
    0   PASS
    1   FAIL
    2   Usage or file error
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_DIR  = os.path.abspath(os.path.join(SCRIPT_DIR, "../../memory-bank/tasks"))

# Fields expected as bold headers: **Field**: value
HEADER_FIELDS = ["Owner", "Sprint", "Status", "Created"]

# Section headers expected as ## Heading with non-empty content below
SECTION_HEADERS = ["Objective", "Input artifacts", "Output artifacts", "Evidence"]

VALID_STATUSES = {"queued", "in_progress", "blocked", "done"}

# Matches template placeholder comments
PLACEHOLDER_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def load_file(path: str) -> str:
    with open(path) as f:
        return f.read()


def extract_header_field(content: str, field: str) -> str | None:
    pattern = re.compile(rf"^\*\*{re.escape(field)}\*\*:\s*(.+)$", re.MULTILINE)
    match = pattern.search(content)
    return match.group(1).strip() if match else None


def extract_section_content(content: str, heading: str) -> str | None:
    """Return the text between ## heading and the next ## heading (or end of file)."""
    pattern = re.compile(
        rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(content)
    return match.group(1).strip() if match else None


def is_placeholder_or_empty(value: str) -> bool:
    cleaned = PLACEHOLDER_RE.sub("", value).strip()
    return cleaned == "" or cleaned == "-"


def validate_task_file(path: str) -> dict:
    if not os.path.isfile(path):
        return {"path": path, "result": "FAIL", "failures": [f"File not found: {path}"]}

    content  = load_file(path)
    failures = []

    # Skip template file itself
    if "TASK-TEMPLATE" in os.path.basename(path):
        return {"path": path, "result": "SKIP", "failures": []}

    # Check bold header fields
    for field in HEADER_FIELDS:
        value = extract_header_field(content, field)
        if value is None:
            failures.append(f"Missing header field: **{field}**")
        elif is_placeholder_or_empty(value):
            failures.append(f"Header field '{field}' is still a placeholder")

    # Validate status value
    status = extract_header_field(content, "Status")
    if status and status not in VALID_STATUSES:
        failures.append(
            f"Invalid status '{status}'. Must be one of: {', '.join(sorted(VALID_STATUSES))}"
        )

    # Check section headers have content
    for heading in SECTION_HEADERS:
        section_content = extract_section_content(content, heading)
        if section_content is None:
            failures.append(f"Missing section: ## {heading}")
        elif is_placeholder_or_empty(section_content):
            # Evidence section may be blank while task is not yet done — only warn if done
            if heading == "Evidence":
                if status == "done":
                    failures.append("Section 'Evidence' must be filled before marking done")
            else:
                failures.append(f"Section '{heading}' is empty or still a placeholder")

    result = "PASS" if not failures else "FAIL"
    return {"path": path, "result": result, "failures": failures}


def format_result(v: dict) -> str:
    if v["result"] == "SKIP":
        return f"[SKIP] {v['path']} (template)"
    symbol = "PASS" if v["result"] == "PASS" else "FAIL"
    lines  = [f"[{symbol}] {os.path.basename(v['path'])}"]
    for f in v["failures"]:
        lines.append(f"      - {f}")
    return "\n".join(lines)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: validate_task.py <path-to-TASK-NNN.md> | --all", file=sys.stderr)
        sys.exit(2)

    if sys.argv[1] == "--all":
        paths = sorted(
            os.path.join(TASKS_DIR, f)
            for f in os.listdir(TASKS_DIR)
            if f.endswith(".md")
        )
    else:
        paths = [sys.argv[1]]

    any_fail = False
    for path in paths:
        result = validate_task_file(path)
        print(format_result(result))
        if result["result"] == "FAIL":
            any_fail = True

    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()

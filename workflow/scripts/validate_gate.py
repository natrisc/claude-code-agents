#!/usr/bin/env python3
"""
validate_gate.py — Gate enforcement validator.

Reads workflow_state.yaml and gates.yaml and verifies that a named gate's
conditions are satisfied: prerequisite gates open, required files exist and
are non-empty.

Usage:
    python validate_gate.py <gate_name>
    python validate_gate.py --all

Exit codes:
    0   PASS
    1   FAIL (at least one gate failed validation)
    2   Usage or file error

Requires: PyYAML (pip install pyyaml)
"""

import os
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
MEMORY_BANK  = os.path.abspath(os.path.join(SCRIPT_DIR, "../../memory-bank"))
CONTRACTS    = os.path.abspath(os.path.join(SCRIPT_DIR, "../contracts/gates.yaml"))
STATE_FILE   = os.path.join(MEMORY_BANK, "state/workflow_state.yaml")
TASKS_DIR    = os.path.join(MEMORY_BANK, "tasks")


def load_yaml(path: str) -> dict:
    try:
        with open(path) as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        print(f"ERROR: Required file not found: {path}", file=sys.stderr)
        sys.exit(2)


def resolve_paths(paths: list, current_sprint: str) -> list:
    return [p.replace("{current_sprint}", current_sprint) for p in paths]


def file_exists_and_nonempty(relative_path: str) -> bool:
    full_path = os.path.join(MEMORY_BANK, relative_path)
    if not os.path.isfile(full_path):
        return False
    return os.path.getsize(full_path) > 50


def has_active_tasks(state: dict) -> bool:
    tasks = state.get("tasks", []) or []
    return any(
        isinstance(t, dict) and t.get("status") not in ("done",)
        for t in tasks
    ) or len(tasks) > 0


def all_tasks_resolved(state: dict) -> bool:
    tasks = state.get("tasks", []) or []
    if not tasks:
        return True
    return all(
        isinstance(t, dict) and t.get("status") in ("done", "queued")
        for t in tasks
    )


def validate_gate(gate_name: str, gates: dict, state: dict) -> dict:
    """
    Returns {"gate": str, "result": "PASS"|"FAIL", "failures": list[str]}.
    """
    current_sprint = state.get("project", {}).get("current_sprint", "")
    gate_flags     = state.get("gates", {})

    if gate_name not in gates:
        return {
            "gate": gate_name,
            "result": "FAIL",
            "failures": [f"Unknown gate '{gate_name}'. Valid gates: {', '.join(gates.keys())}"],
        }

    contract = gates[gate_name]
    failures = []

    # 1. Prerequisite gates must be open
    for prereq in contract.get("prerequisite_gates", []):
        if not gate_flags.get(prereq, False):
            failures.append(f"Prerequisite gate not open: {prereq}")

    # 2. Required files must exist and be non-empty
    raw_files = contract.get("required_files", [])
    resolved  = resolve_paths(raw_files, current_sprint)
    for rel_path in resolved:
        if not file_exists_and_nonempty(rel_path):
            failures.append(f"Required file missing or empty: memory-bank/{rel_path}")

    # 3. Sprint-specific checks
    if contract.get("task_list_nonempty") and not has_active_tasks(state):
        failures.append("No tasks found in workflow_state.yaml — at least one task must exist")

    if contract.get("all_tasks_resolved") and not all_tasks_resolved(state):
        tasks = state.get("tasks", []) or []
        open_tasks = [
            t.get("id", "?") for t in tasks
            if isinstance(t, dict) and t.get("status") not in ("done", "queued")
        ]
        if open_tasks:
            failures.append(f"Open tasks must be completed or deferred: {', '.join(open_tasks)}")

    result = "PASS" if not failures else "FAIL"
    return {"gate": gate_name, "result": result, "failures": failures}


def format_result(v: dict) -> str:
    symbol = "PASS" if v["result"] == "PASS" else "FAIL"
    lines  = [f"[{symbol}] {v['gate']}"]
    for f in v["failures"]:
        lines.append(f"      - {f}")
    return "\n".join(lines)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: validate_gate.py <gate_name> | --all", file=sys.stderr)
        sys.exit(2)

    contracts_data = load_yaml(CONTRACTS)
    gates          = contracts_data.get("gates", {})
    state          = load_yaml(STATE_FILE)

    gate_names = list(gates.keys()) if sys.argv[1] == "--all" else [sys.argv[1]]

    any_fail = False
    for name in gate_names:
        result = validate_gate(name, gates, state)
        print(format_result(result))
        if result["result"] == "FAIL":
            any_fail = True

    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()

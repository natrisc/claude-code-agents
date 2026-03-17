#!/usr/bin/env python3
"""
regenerate_dashboard.py — Rebuilds memory-bank/state/dashboard.md from state files.

Run after every workflow state change. Produces a deterministic dashboard
so the scrum-master does not need to hand-write it.

Usage:
    python regenerate_dashboard.py

Reads:
    memory-bank/state/workflow_state.yaml
    memory-bank/state/product_progress.yaml
    memory-bank/logs/events.log

Writes:
    memory-bank/state/dashboard.md

Requires: PyYAML (pip install pyyaml)
"""

import os
import sys
from datetime import datetime, timezone

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
MEMORY_BANK = os.path.abspath(os.path.join(SCRIPT_DIR, "../../memory-bank"))


def load_yaml(rel_path: str) -> dict:
    full = os.path.join(MEMORY_BANK, rel_path)
    if not os.path.isfile(full):
        return {}
    with open(full) as f:
        return yaml.safe_load(f) or {}


def load_events(n: int = 5) -> list:
    log_path = os.path.join(MEMORY_BANK, "logs/events.log")
    if not os.path.isfile(log_path):
        return []
    with open(log_path) as f:
        lines = [line.rstrip() for line in f if line.strip() and not line.startswith("#")]
    return lines[-n:]


def gate_icon(flag) -> str:
    return "PASS" if flag else "pending"


def render(state: dict, progress: dict, events: list) -> str:
    project  = state.get("project") or {}
    gates    = state.get("gates") or {}
    roles    = state.get("roles") or {}
    blockers = state.get("blockers") or []
    tasks    = state.get("tasks") or []

    epics   = (progress.get("epics") or {})
    releases = (progress.get("releases") or {})
    history  = (progress.get("sprint_history") or {})

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")

    lines = [
        "# Sprint Dashboard",
        "",
        f"> Last regenerated: {now}  |  Source of truth: `memory-bank/state/`",
        "",
        "---",
        "",
        "## Project",
        "",
        "| Field | Value |",
        "| --- | --- |",
        f"| Name | {project.get('name') or '—'} |",
        f"| Current sprint | {project.get('current_sprint') or '—'} |",
        f"| Context version | {project.get('active_context_version') or '—'} |",
        f"| Status | {project.get('status') or '—'} |",
        "",
        "---",
        "",
        "## Gate status",
        "",
        "| Gate | Status |",
        "| --- | --- |",
    ]

    for gate, flag in gates.items():
        lines.append(f"| {gate} | {gate_icon(flag)} |")

    # Build active-task lookup by owner
    active_task_map: dict = {}
    for task in tasks:
        if isinstance(task, dict) and task.get("status") == "in_progress":
            owner = task.get("owner", "")
            active_task_map[owner] = task.get("id", "")

    lines += [
        "",
        "---",
        "",
        "## Roles",
        "",
        "| Role | Status | Active task |",
        "| --- | --- | --- |",
    ]
    for role, status in roles.items():
        active = active_task_map.get(role, "—")
        lines.append(f"| {role} | {status} | {active} |")

    lines += ["", "---", "", "## Open blockers", ""]
    if blockers:
        for b in blockers:
            lines.append(f"- {b}")
    else:
        lines.append("None.")

    in_progress = [t for t in tasks if isinstance(t, dict) and t.get("status") == "in_progress"]
    lines += ["", "---", "", "## Active tasks", ""]
    if in_progress:
        lines += ["| ID | Title | Owner | Status |", "| --- | --- | --- | --- |"]
        for t in in_progress:
            lines.append(
                f"| {t.get('id','—')} | {t.get('title','—')} | {t.get('owner','—')} | {t.get('status','—')} |"
            )
    else:
        lines.append("None.")

    lines += ["", "---", "", "## Product progress", "", "| Epic | Status |", "| --- | --- |"]
    if epics:
        for eid, epic in epics.items():
            if isinstance(epic, dict):
                lines.append(f"| {eid}: {epic.get('title','—')} | {epic.get('status','—')} |")
    else:
        lines.append("| — | — |")

    lines += ["", "| Release | Target epics | Progress |", "| --- | --- | --- |"]
    if releases:
        for rid, rel in releases.items():
            if isinstance(rel, dict):
                targets = ", ".join(rel.get("target_epics") or []) or "—"
                progress_pct = rel.get("progress", 0)
                lines.append(f"| {rid} | {targets} | {progress_pct}% |")
    else:
        lines.append("| — | — | — |")

    lines += ["", "---", "", "## Sprint history", "", "| Sprint | Outcome | Completed | Carry-over |", "| --- | --- | --- | --- |"]
    if history:
        for sid, sprint in history.items():
            if isinstance(sprint, dict):
                completed = len(sprint.get("completed_items") or [])
                carry     = len(sprint.get("carry_over_items") or [])
                lines.append(f"| {sid} | {sprint.get('outcome','—')} | {completed} | {carry} |")
    else:
        lines.append("| — | — | — | — |")

    lines += ["", "---", "", "## Recent events", ""]
    if events:
        for e in events:
            lines.append(f"- `{e}`")
    else:
        lines.append("No events yet. See `logs/events.log` for full history.")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    state    = load_yaml("state/workflow_state.yaml")
    progress = load_yaml("state/product_progress.yaml")
    events   = load_events(5)
    content  = render(state, progress, events)

    out_path = os.path.join(MEMORY_BANK, "state/dashboard.md")
    with open(out_path, "w") as f:
        f.write(content)

    print(f"Dashboard regenerated → {out_path}")


if __name__ == "__main__":
    main()

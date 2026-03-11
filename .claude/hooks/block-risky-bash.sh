#!/usr/bin/env bash
set -euo pipefail

INPUT="$(cat || true)"

if echo "$INPUT" | grep -Eqi 'terraform destroy|kubectl delete|rm -rf /|git push --force'; then
  echo "Blocked by project hook: risky bash command detected." >&2
  exit 2
fi

exit 0
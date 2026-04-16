#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
VENV_PYTHON="$REPO_ROOT/.venv/bin/python"

if [ -x "$VENV_PYTHON" ]; then
  "$VENV_PYTHON" -m pytest tests/ -q
else
  echo "Warning: virtualenv not found at $VENV_PYTHON" >&2
  echo "Falling back to system Python. Activate the repo venv or install pytest." >&2
  python -m pytest tests/ -q
fi

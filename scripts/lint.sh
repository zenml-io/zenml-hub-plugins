#!/usr/bin/env bash
set -e
set -x
set -o pipefail

SRC=${1:-"src"}

export ZENML_DEBUG=1
export ZENML_ANALYTICS_OPT_IN=false
ruff $SRC

# autoflake replacement: checks for unused imports and variables
ruff $SRC --select F401,F841 --exclude "__init__.py" --isolated

black $SRC  --check

# check type annotations
mypy $SRC

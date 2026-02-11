# create script in pyproject 
# then run with uv run {{scriptName}}
# run script 
rs scriptName: 
  uv run {{scriptName}}

# test list 
tl: 
  uv run pytest --collect-only

# test run 
tr namePattern: 
  uv run pytest -k "{{namePattern}}" -s --verbose

# run binary
rb name:
  python ./src/bin/{{name}}.py

# activate environtment
ae:
  source .venv/bin/activate.fish

de: 
  deactivate

# migrate to head
mth: 
  cd ./src/migrations && alembic upgrade head

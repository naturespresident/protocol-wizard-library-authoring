PYTHON := .venv/bin/python3

.PHONY: setup test validate

# Create .venv and install the dependencies (jsonschema). Safe to rerun.
setup:
	python3 -m venv .venv
	$(PYTHON) -m pip install --quiet -r requirements.txt

# Unit tests for the validator and the translation chunk tool.
test: $(PYTHON)
	$(PYTHON) -B -m unittest discover -p 'test_*.py'

# Check every translation against its English original and the schema.
validate: $(PYTHON)
	$(PYTHON) -B validate_translations.py

$(PYTHON):
	@echo "Run 'make setup' first." >&2 && exit 1

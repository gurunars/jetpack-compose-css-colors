run: venv
	./venv/bin/python colors.py

venv:
	virtualenv ./venv
	./venv/bin/pip install -r requirements.txt

.PHONY: run

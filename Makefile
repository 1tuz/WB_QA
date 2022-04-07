venv:
	python3 -m pip install virtualenv
	python3 -m venv venv
install:
	pip install -r requirements.txt
tests:
	pytest


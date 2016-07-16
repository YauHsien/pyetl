.PHONY: init test

PIP = /usr/bin/pip3
PyTest = py.test

init:
	$(PIP) install -r requirements.txt

test:
	$(PyTest) tests

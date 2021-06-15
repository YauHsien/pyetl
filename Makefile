.PHONY: init test example.oops example.hello

PIP = pip3
PYTHON_USER_BASE = ./.local
PyTest = py.test

init: .load-env
	echo OK
.load-env:
	@touch $(PYTHON_USER_BASE)/.dummy\
	 && (rm -rf $(PYTHON_USER_BASE)/*)\
	 || (mkdir $(PYTHON_USER_BASE))
	PYTHONUSERBASE=$(PYTHON_USER_BASE) $(PIP) install --user pipenv
	touch .load-env
# $(PIP) install -r requirements.txt

test:
	$(PyTest) tests

example.oops:
	./etl world1 hello
	./etl world hello1
	./etl hello world 1
example.hello:
	./etl hello world

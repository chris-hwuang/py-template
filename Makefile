test: init
	nosetests tests

init:
	pip install -r requirements.txt

.PHONY: test

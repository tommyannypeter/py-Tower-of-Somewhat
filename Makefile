.PHONY: clean all install test

all:
	python main.py

install:
	pip install -r mod_requirement.txt

test:
	python test.py

clean:
	rm -f *.log
	rm -rf __pycache__

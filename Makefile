.PHONY: run install test clean

run:
	python src/main.py

install:
	pip install -r mod_requirement.txt

test:
	pytest tests

clean:
	rm -f *.log
	rm -rf __pycache__

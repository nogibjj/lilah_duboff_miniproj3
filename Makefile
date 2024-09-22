install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black ./python_files

lint:
	ruff check ./python_files/*.py  ./python_files/*.ipynb 
	
test:
	python -m pytest -vv --nbval ./python_files/tests/test_*.py ./python_files/*.ipynb

check:
	python ./python_files/desc_stats_main.py
	git config --local user.email "action@github.com"; \
	git config --local user.name "Github Action"; \
	git add .; \
	git commit -m "test"; \
	git push; \

deploy:
	#deploy goes here

all: install lint format test 
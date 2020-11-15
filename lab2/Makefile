all: install test run deploy

install:
	pip install pipenv && pipenv --python 3.7
	pipenv install requests && pipenv install ntplib
	pipenv install pytest

test:
	pipenv run pytest tests/tests.py > results.txt

run:
	pipenv run python app.py append >> results.txt

deploy:
	git add . && git commit -m "added output in results.txt"  && git push

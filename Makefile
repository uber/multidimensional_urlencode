all: develop test

test: develop lint
	py.test

test-all:
	tox

develop:
	python setup.py develop

release: clean
	prerelease && release

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name __pycache__ -delete

lint:
	flake8 multidimensional_urlencode

coverage:
	coverage run --source multidimensional_urlencode setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs: develop
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

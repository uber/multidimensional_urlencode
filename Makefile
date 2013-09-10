all: develop test release

test: develop
	flake8 multidimensional_urlencode
	py.test

develop:
	python setup.py develop

release:
	prerelease && release

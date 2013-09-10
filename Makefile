all: develop test release

test:
	py.test

develop:
	python setup.py develop

release:
	prerelease && release

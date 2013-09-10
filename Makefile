all: develop test prerelease release

test:
	py.test

develop:
	python setup.py develop

prerelease:
	prerelease

release:
	release

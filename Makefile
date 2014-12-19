.PHONY:	test-release release clean

test-release:
	python setup.py register -r testpypi
	python setup.py sdist upload -r testpypi
	python setup.py bdist_wheel upload -r testpypi

release:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi
	python setup.py bdist_wheel upload -r pypi

clean:
	rm -rf build dist MANIFEST install.txt
	rm -rf *.egg-info
	find . -name "__pycache__" -exec rm -r {} +

"""Do setup for uploading to pypi
"""
import setuptools

with open("README.md", "r") as readme:
	long_description = readme.read()

setuptools.setup(
	name="metprint",
	version="2020.3",
	author="FredHappyface",
	description="Pretty print text in a range of builtin formats or make your own",
	long_description=long_description,
    long_description_content_type="text/markdown",
	url="https://github.com/FHPythonUtils/MetPrint",
	packages=setuptools.find_packages(),
	classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
	python_requires='>=3.0',
)

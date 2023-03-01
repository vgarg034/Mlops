from setuptools import setup,find_packages

setup(
	name='my_package',
	version='0.1',
	description='A sample Python package',
	author='Vineet Garg',
	author_email='vineetgarg034@gmail.com',
	packages = find_packages(),
	install_requires=[
		
		'pandas',
	],
)

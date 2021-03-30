import setuptools
from setuptools import setup 




# specify requirements of your package here 
REQUIREMENTS = ['panclus'] 

# some more details 
CLASSIFIERS = [ 
	'Development Status :: 4 - Beta', 
	'Intended Audience :: Developers', 
	'Topic :: Internet', 
	'License :: OSI Approved :: MIT License', 
	'Programming Language :: Python', 
	'Programming Language :: Python :: 3', 
	'Programming Language :: Python :: 3.3', 
	'Programming Language :: Python :: 3.4', 
	'Programming Language :: Python :: 3.5', 
	] 

setuptools.setup(
    name="Example-Test-00", # Replace with your own username
    version="0.0.1",
    author="Ayush Moghe",
    author_email="mogheayushgr8@gmail.com",
    description="example",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,

)

import setuptools

with open('README.md', 'r') as infile:
    long_description = infile.read()

setuptools.setup(
    name='dopyr',
    version='0.0.1',
    author='Timon Schmelzer',
    author_email='timon.schmelzer@tu-dortmund.de',
    description='A small python framework to produce plots and do calculations commonly used in HEP.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Kecksdose/dopyr',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
from setuptools import setup, find_packages

packages = find_packages(
        where='.',
        include=['kkpdf*']
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='kkpdf',
    version='1.0.0',
    description='pdf to image.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kazukingh01/kkpdf",
    author='Kazunoki',
    author_email='kazukingh01@gmail.com',
    license='Public License',
    packages=packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Private License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'PyMuPDF==1.22.5',
        'reportlab==4.0.9',
        'Pillow==10.0.0',
        'wheel>=0.37.0',
    ],
    python_requires='>=3.12.2'
)

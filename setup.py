from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='wikiextractor',
    version='2.70',
    description='A script that extracts and cleans text from a Wikipedia database dump',
    author='appachan',
    author_email='appachan.hotel@gmail.com',
    url='https://github.com/attardi/wikiextractor',
    license="GPL 3.0",
    keywords=['text', 'nlp'],
    packages=['wikiextractor'],
    install_requires=[]
)

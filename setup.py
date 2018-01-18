from setuptools import setup

def readme():
    with open('README') as f:
        return f.read()

setup(
    name='fsutil',
    version='1',
    description='File system utilities',
    long_description=readme(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='file system utilities',
    url='https://github.com/robehickman/fsutil',
    author='Robert Hickman',
    author_email='robehickman@gmail.com',
    license='MIT',
    packages=['fsutil'],
    test_suite='nose.collector',
    tests_require=['nose'])


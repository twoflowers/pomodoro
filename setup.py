__author__ = 'Tom'

from distutils.core import setup

setup(
    name='pomodoro',
    version='0.1',
    author='Tom Martin',
    author_email='thomas.r.martin@gmail.com',
    packages=['pomodoro', 'pomodoro.test'],
    scripts=['bin/stowe-towels.py',],
    url='http://pypi.python.org/pypi/pomodoro/',
    license='LICENSE.txt',
    description='Command line pomodoro',
    long_description=open('README.txt').read(),
    install_requires=[
        # "Django >= 1.1.1",
        # "caldav == 0.1.4",
    ],
)

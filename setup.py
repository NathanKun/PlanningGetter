'''
Created on 4 août 2017

@author: Junyang HE
'''

import setuptools

install_requires = [
    'numpy',
    'python-dateutil',
    #'pytz',
    'icalendar',
    'selenium',
    'BeautifulSoup4',
    'lxml'
]

setuptools.setup(
    name='PlanningGetter',
    version='1.3',
    packages=['PlanningGetter','PlanningGetter.util'],
    description='Crawl ESIGELEC Planning and generate ics file ',
    long_description=open('README.md').read(),
    author='Junyang HE',
    author_email='nathanhejunyang@gmail.com',
    license='GNU General Public License v3.0',
    url='https://github.com/NathanKun/PlanningGetter',
    install_requires=install_requires
)
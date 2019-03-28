import os
from setuptools import find_packages, setup

setup(
    name='django-fm-minio',
    version='0.1.4',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app.',
    url='https://github.com/skob/django-fm-minio',
    py_modules=['fixtures_minio'],
    author='skob',
    author_email='skobolo@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[ 'Minio' ]
)


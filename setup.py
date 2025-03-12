from setuptools import setup, find_packages

setup(
    name='proproducts',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'proproducts': ['templates/modules/*.html',],
        'users': ['fixtures/*.json'],
    },
    install_requires=[
        'django==5.1.7',
        'django-formtools==2.5.1',
        'django-environ==0.12.0',
    ],
    author='Heribertus Rustyawan',
    author_email='herbew@gmail.com',
    description='Django Project Management Products',
    url='https://github.com/herbew/proproducts.git',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
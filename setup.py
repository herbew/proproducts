from setuptools import setup, find_packages
import os

def post_install():
    """
    This function will be executed after the installation is complete.
    """
    import django
    from django.core.management import call_command

    # Set up Django environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proproducts.settings')
    django.setup()

    # Add records to the modules.models.Module model
    from modules.models import Module

    # Check if the record already exists
    if not Module.objects.filter(name='proproducts').exists():
        Module.objects.create(
            name='proproducts',
            version='0.1',
            status='installed',
            repository='https://github.com/herbew/proproducts.git',
            description='Django Project Management Products'
        )
        print("Record 'proproducts' successfully added to modules_module.")
    else:
        print("Record 'proproducts' already exists in modules_module.")

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
        'django',
        'django-formtools',
        'django-environ',
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
    entry_points={
        'distutils.commands': [
            'post_install = proproducts.setup:post_install',
        ],
    },
)

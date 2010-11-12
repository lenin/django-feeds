from setuptools import setup, find_packages

version = '0.1'

LONG_DESCRIPTION = """
Feeds
--------------------------
"""

setup(
    name='django-feeds',
    version=version,
    description="django-feeds",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='news,django',
    author='Lenin Yee',
    author_email='lenin.ayr@gmail.com',
    url='http://github.com/lenin/django-feeds',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)

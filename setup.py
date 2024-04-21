from setuptools import setup, find_packages

version = '1.0'

setup(
    name='plone_work_orders',
    version=version,
    description="Plone add-on for managing work orders with SMS and Email notifications",
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Plone Python',
    author='Your Name',
    author_email='your.email@example.com',
    url='http://www.example.com',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone_work_orders'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.api>=1.8.4',
        'Twilio',  # Ensure you have this added for SMS functionalities
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)

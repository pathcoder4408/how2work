from setuptools import setup, find_packages

setup(
    name='plone_work_orders',
    version='1.0',
    description="Manage work orders in Plone with notifications and calendar views",
    long_description=(open("README.md").read() + "\n" +
                      open("CHANGES.md").read()),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='Plone Python Work Orders Management',
    author='Your Name',
    author_email='your.email@example.com',
    url='http://www.yourwebsite.com',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone_work_orders'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.api>=1.8.4',
        'twilio',
        'plone.app.dexterity',
        'plone.app.relationfield',
        'plone.app.event'
    ],
    entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
    """,
)

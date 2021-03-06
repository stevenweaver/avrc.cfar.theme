from setuptools import setup, find_packages
import os

version = '0.5.0'

setup(
    name='avrc.cfar.theme',
    version=version,
    description='Center For AIDS Research (CFAR) Plone Theme',
    classifiers=[
    'Framework :: Plone',
    'Programming Language :: Python',
    ],
    keywords='',
    author='BEAST Core Development Team',
    author_email='beast@ucsd.edu',
    url='https://github.com/beastcore/avrc.cfar.theme',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'':'src'},
    namespace_packages=['avrc', 'avrc.cfar'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.theming',
        'webcouturier.dropdownmenu'
        ],
    extras_require=dict(
        test=['plone.app.testing'],
        ),
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )

from setuptools import setup, find_packages

setup(
    name='fhtw',
    version='0.0.1',
    description='Custom FHTW Pygments Style',
    license='GPL-v3',
    keywords='pygments style extras fhtw',
    author='Alija Sabic',
    author_email='sabic.alija@gmail.com',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    entry_points="""
        [pygments.styles]
        fhtw = styles.fhtw:FhtwStyle
    """,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

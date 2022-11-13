from setuptools import setup, find_packages

setup(
    name='fhtw',
    packages=find_packages(),
    entry_points="""
    [pygments.styles]
    fhtw = fhtw:FhtwStyle
    """,
)

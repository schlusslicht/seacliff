from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    legal = f.read()

setup(
    author='Philip Schildkamp',
    author_email='philip.schildkamp@uni-koeln.de',
    description='seak life within the field of digital humanities',
    entry_points={'console_scripts': ['seacliff = seacliff.seacliff:main']},
    license=legal,
    long_description=readme,
    name='seacliff',
    packages=find_packages(exclude=['docs']),
    url='https://github.com/schlusslicht/seacliff',
    version='0.0.1'
)

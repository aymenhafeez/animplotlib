from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='animplotlib',
    version='0.2.4',
    author='Aymen Hafeez',
    author_email='aymennh@gmail.com',
    packages = find_packages(),
    url='https://github.com/aymenhafeez/animplotlib/',
    license='MIT',
    description='A thin wrapper around the matplotlib FuncAnimation class',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    install_requires=["matplotlib >= 1.1"],
)

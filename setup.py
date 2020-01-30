from setuptools import setup 

with open('README.md') as f:
    long_description = f.read()

setup(
    name='animplotlib',
    version='0.1.4',
    author='Aymen Hafeez',
    author_email='aymennh@gmail.com',
    packages=['animplotlib',],
    url='https://github.com/aymenhafeez/animplotlib/',
    license='MIT',
    description='A thin wrapper around the matplotlib FuncAnimation class',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.5',
    install_requires=["matplotlib >= 1.1"],
)

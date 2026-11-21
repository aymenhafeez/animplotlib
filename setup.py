from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="animplotlib",
    version="0.3.0",
    author="Aymen Hafeez",
    author_email="aymennh@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/aymenhafeez/animplotlib/",
    license="MIT",
    description="A thin wrapper around the matplotlib FuncAnimation class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    install_requires=["matplotlib>=3.8", "numpy"],
)

from setuptools import setup, find_packages

setup(
    name="jotform",
    url="https://github.com/Quandri/jotform-api-python/",
    version="1.1",
    description="JotForm API - Python Client",
    author="JotForm",
    author_email="api@jotform.com",
    
    packages=find_packages(),
    package_data={"": ["*.png"]},
    install_requires=[
        "pytest==7.1.2",
    ],
)

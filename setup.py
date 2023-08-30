from setuptools import setup, find_packages

setup(
    name="sds011",
    version="1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": ["sds011 = sds011:main"]
        },
    install_requires=[
        'Flask>=0.12.2',
        'pyserial>=3.5'
        ]
    )

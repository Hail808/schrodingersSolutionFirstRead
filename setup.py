from setuptools import setup, find_packages

setup(
    name='schrodingerssolution',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your project',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'my-python-project=main:main',  # Adjust this if your main function is named differently
        ],
    },
)
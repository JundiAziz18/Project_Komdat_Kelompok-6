from setuptools import find_packages, setup

setup(
    name='NRZL_LIB',
    version='0.1.0',
    description='Library NRZL Kelompok 6',
    author='Kelompok 6',
    author_email='-',  # Isi dengan email kamu
    url='https://github.com/JundiAziz18/Project_Komdat_Kelompok-6.git',  # URL repo kalau ada
    package_dir={'': 'lib'},
    packages=find_packages(where='lib'),
    install_requires=[
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

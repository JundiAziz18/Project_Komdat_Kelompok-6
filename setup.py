from setuptools import find_packages, setup

setup(
    name='Kelompok6_Komdat',
    version='0.1.4',
    description='Library Enkoder dan Dekoder NRZL & Manchester Kelompok 6' \
                ' untuk mata kuliah Komunikasi Data',
    long_description='Library ini menyediakan fungsi untuk enkoding dan dekoding sinyal NRZ-L dan Manchester. ' \
                     'Dapat digunakan untuk keperluan pembelajaran mata kuliah Komunikasi Data.',
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

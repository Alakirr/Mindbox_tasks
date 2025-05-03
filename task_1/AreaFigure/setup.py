from setuptools import setup, find_packages

setup(
    # name='calculate_areas',
    name='AreaFigure',
    version='1.0.0',
    description='Library for calculating areas of geometric figures',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Алексей',
    author_email='alakir11@mail.ru',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='area calculations mathematics',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    extras_require={
        'dev': ['pytest', 'flake8', 'black'],
    },
    python_requires='>=3.7',
)
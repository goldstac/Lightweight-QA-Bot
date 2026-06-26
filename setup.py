from setuptools import setup, Extension, find_packages

csearch_ext = Extension(
    'src.csearch',
    sources=['csrc/csearch.cpp'],
)

setup(
    name='qabot',
    version='2.0.0',
    packages=find_packages(),
    ext_modules=[csearch_ext],
    python_requires='>=3.8',
)

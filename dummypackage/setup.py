import os

import numpy as np

from os.path import join
from setuptools import setup, Extension
from Cython.Build import cythonize


directory_path = os.path.dirname(
    os.path.abspath(__file__)
    )


ext_data = {
    'cythonpac1.somapac': {
        'sources': [join(directory_path, 'cythonpac1', 'somapac.pyx')]},
    'cythonpac2.multpac': {
        'sources': [join(directory_path, 'cythonpac2', 'multpac.pyx')]},
    'numpypac.normalizepac': {
        'sources': [join(directory_path, 'numpypac', 'normalizepac.pyx')],
        'include': [np.get_include()]},
    'cpppac.wrap_fib': {
        'sources': [
            join(directory_path, 'cpppac', 'wrap_fib.pyx'),
            join(directory_path, 'cpppac', 'cfib.c')]
    }
}


extensions = []

for name, data in ext_data.items():

    sources = data['sources']
    include = data.get('include', [])

    obj = Extension(
        name,
        sources=sources,
        include_dirs=include
    )
    
    extensions.append(obj)


# Use cythonize on the extension object.
setup(
    package_dir={'dummypackage': ''},
    ext_modules=cythonize(extensions))
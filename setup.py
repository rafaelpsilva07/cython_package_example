import os

import numpy as np

from os.path import join
from setuptools import setup, Extension
from Cython.Build import cythonize


directory_path = os.path.dirname(
    os.path.abspath(__file__)
    )


ext_data = {
    'dummypackage.cythonpac1.addpac': {
        'sources': [join(directory_path, 'dummypackage', 'cythonpac1', 'addpac.pyx')]},
    'dummypackage.cythonpac2.multpac': {
        'sources': [join(directory_path, 'dummypackage', 'cythonpac2', 'multpac.pyx')]},
    'dummypackage.numpypac.normalizepac': {
        'sources': [join(directory_path, 'dummypackage', 'numpypac', 'normalizepac.pyx')],
        'include': [np.get_include()]},
    'dummypackage.cpac.wrap_fib': {
        'sources': [
            join(directory_path, 'dummypackage', 'cpac', 'wrap_fib.pyx'),
            join(directory_path, 'dummypackage', 'cpac', 'cfib.c')]
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
    name='dummypackage',
    author='Rafael Pereira',
    #package_dir={'dummypackage': ''},
    ext_modules=cythonize(extensions))
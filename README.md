# About this package
This package is an example of how to organize and compile a cython package. It contains pure cython examples, a C wraped function and a numpy example.

## Build
To build the package use the following command line:

```python setup.py build_ext --inplace```

To install the package use:

```python setup.py install```

Another option is to distribute this package into a wheel file.

```python setup.py sdist bdist_wheel```


## How to use

Once the package is installed, you can test te functions!


```python
>>> from dummypackage.cythonpac1 import add
>>> from dummypackage.cythonpac2 import mult
>>> from dummypackage.numpypac import normalize
>>> from dummypackage.cpac import fib
```

## See an overview of this package on Youtube
 https://www.youtube.com/watch?v=53l4HApVUKU&ab_channel=EngenhariaRefinada
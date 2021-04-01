# from distutils.core import setup
from Cython.Build import cythonize
from setuptools import setup,Extension
extensions = [
    Extension(
        'cython_tools.queue',
        ['cython_tools/queue.pyx'],
    )
]
setup(
    # name = 'cython_tools',
    ext_modules = cythonize(extensions)
)
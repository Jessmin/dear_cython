from os import path
import sys
from setuptools import setup, Extension
from Cython.Build import cythonize

cython_src_dir = 'components/'
c_src_dir = 'components/src_c/'
package_name = 'components'
package_prefix = package_name+'.'

extensions = [
    Extension(
        package_prefix+'binocular_calculator',
        [
            cython_src_dir+'binocular_calculator.pyx',
            c_src_dir+'BinocularCalculation.cpp',
            c_src_dir+'CalculateStereoFrame.c',
            c_src_dir+'MappingCoef.c'
        ],
        include_dirs = [ c_src_dir, path.join(sys.prefix, 'include') ],
        extra_compile_args = [
            "-mavx",
            "-mavx2",
            "-mfma"
        ],
    ),
    Extension(
        package_prefix+'calcStFrame',
        [
            cython_src_dir+'calcStFrame.pyx',
        ],
        include_dirs = [ c_src_dir, path.join(sys.prefix, 'include') ],
    )
]

setup(
    name='components',
    ext_modules=cythonize(extensions)
)
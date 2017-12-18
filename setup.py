from setuptools import setup
from distutils.extension import Extension
from setuptools import Command
import os.path


try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False
ext = '.pyx' if USE_CYTHON else '.cpp'

cwd = os.path.abspath(os.path.dirname(__file__))
extensions =\
    [Extension(name='kaldi_edit_distance._edit_distance',
               sources=['kaldi_edit_distance/_edit_distance' + ext],
               include_dirs=[],
               extra_compile_args=['-O3'])]

if USE_CYTHON:
    extensions = cythonize(extensions)

setup(name='kaldi_edit_distance', ext_modules=extensions)

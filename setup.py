from setuptools import setup
from distutils.extension import Extension
from setuptools import Command
import os.path

cwd = os.path.abspath(os.path.dirname(__file__))
pythondir = 'kaldi_edit_distance'


try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False
ext = '.pyx' if USE_CYTHON else '.c'

extensions =\
    [Extension(name=os.path.join(pythondir, 'edit_distance'),
               sources=[os.path.join(pythondir, 'edit_distance' + ext)],
               include_dirs=[os.path.join(cwd, 'kaldi_src')],
               extra_compile_args=['-O3'])]

if USE_CYTHON:
    extensions = cythonize(extensions)

setup(name='kaldi_edit_distance',
      ext_modules=extensions)

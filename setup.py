from distutils.core import setup
from distutils.extension import Extension
import os.path

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False
ext = '.pyx' if USE_CYTHON else '.cpp'

include_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'kaldi_src')
extensions =\
    [Extension(name='kaldi_edit_distance/edit_distance',
               sources=['kaldi_edit_distance/edit_distance' + ext],
               include_dirs=[include_path],
               extra_compile_args=['-O3'])]

if USE_CYTHON:
    extensions = cythonize(extensions)

setup(name='kaldi_edit_distance',
      ext_modules=extensions)

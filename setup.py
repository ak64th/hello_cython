import fnmatch

from Cython.Build import cythonize
from setuptools import setup, find_packages, Extension
from setuptools.command.build_py import build_py

extensions = [
    # Extension('hello_cython.utils', ['src/hello_cython/utils.py']),
    # Extension('hello_cython.core', ['src/hello_cython/core.pyx']),
    Extension('hello_cython.*', ['src/hello_cython/*.pyx']),
    Extension('hello_cython.*', ['src/hello_cython/*.py']),
]
cython_excludes = ['**/__init__.py']


def not_cythonized(tup):
    (package, module, filepath) = tup
    return any(
        fnmatch.fnmatchcase(filepath, pat=pattern)
        for pattern in cython_excludes
    ) or not any(
        fnmatch.fnmatchcase(filepath, pat=pattern)
        for ext in extensions
        for pattern in ext.sources
    )


class build_py_(build_py):
    def find_modules(self):
        modules = super().find_modules()
        return list(filter(not_cythonized, modules))

    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        return list(filter(not_cythonized, modules))


setup(
    author="Elmer Yu",
    author_email='yujun@kingobots.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    license="MIT license",
    name='hello_cython',
    include_package_data=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'hello_cython': ['*.pxd']},
    ext_modules=cythonize(extensions, exclude=cython_excludes),
    cmdclass={'build_py': build_py_},
    url='https://github.com/ak64th/hello_cython',
    version='0.0.1',
    zip_safe=False,
)

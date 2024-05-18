"""
   pyRCSwitch
   Python module to wrap the RCSwitch Common Library

   See: https://github.com/latchdevel/pyRCSwitch

   Copyright (c) 2024 Jorge Rivera. All right reserved.
   License GNU Lesser General Public License v3.0.
"""

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import os

# Add cmake_lists_dir to Extension
class CMakeExtension(Extension):
    def __init__(self, name, cmake_lists_dir='.', **kwa):
        Extension.__init__(self, name, sources=[], **kwa)
        self.cmake_lists_dir = os.path.abspath(cmake_lists_dir)

# CMake Extension Build
class cmake_build_ext(build_ext):

    def build_extensions(self):

        import subprocess

        # Ensure that CMake is present and working
        try:
            out = subprocess.check_output(['cmake', '--version'])
            #print (out.decode())
        except OSError:
            raise RuntimeError('Cannot find CMake executable')

        for ext in self.extensions:

            # Set library output dir
            lib_temp = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

            # Set build type
            build_type = 'Debug' if os.environ.get('DISPTOOLS_DEBUG','OFF') == 'ON' else 'Release'

            print("\nCMake building extension:  {}".format(ext.name))
            print(  "CMake build type:          {}".format(build_type))
            print(  "CMake module output dir:   {}".format(lib_temp))
            print(  "CMake temporary build dir: {}".format(self.build_temp))

            cmake_args = [
                '-DCMAKE_BUILD_TYPE=%s' % build_type,
                # Ask CMake to place the resulting library in the directory containing the extension
                '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(build_type.upper(), lib_temp),
                # Other intermediate static libraries are placed in a temporary build directory instead
                '-DCMAKE_ARCHIVE_OUTPUT_DIRECTORY_{}={}'.format(build_type.upper(), self.build_temp),
                # VERSION_INFO is defined in setup() and passed into the C++ here
                '-DVERSION_INFO={}'.format(self.distribution.get_version())
            ]

            # Make build directory if not exists
            if not os.path.exists(self.build_temp): os.makedirs(self.build_temp)

            # Call CMake configure
            print ("\nCMake configure:")
            subprocess.check_call(['cmake', ext.cmake_lists_dir] + cmake_args, cwd=self.build_temp )

            # Call CMake configure build
            print ("\nCMake build:")
            subprocess.check_call(['cmake', '--build', '.', '--config', build_type], cwd=self.build_temp )
            print ("CMake build done!\n")

setup(
    name="pyRCSwitch",
    version="0.1.0",
    author="Jorge Rivera",
    author_email="latchdevel@users.noreply.github.com",
    description="Python module to wrap the RCSwitch Common Library",
    url="https://github.com/latchdevel/pyRCSwitch",
    long_description="Adaptation of RCSwitch Arduino library to be used on any system to encode and decode RC codes of supported protocols",
    ext_modules=[CMakeExtension(name='pyRCSwitch')],
    cmdclass={'build_ext':cmake_build_ext},
    keywords="rcswitch, rc-switch, rc-switch-lib, rcswitch-library, ask, ook, ask-ook, 315mhz, 433mhz",
    license='LGPL-3.0',
    license_files=["LICENSE.txt"],
    classifiers=[ # https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: C++",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        "Operating System :: OS Independent"
    ],
    platforms=["any"],
    python_requires=">=3.6",
    test_suite = 'test_pyRCSwitch'
)
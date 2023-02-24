"""The setup script for the ``pynrand`` library.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# To get version of Python, to extract command line arguments, and to exit
# script abruptly if necessary.
import sys

# For directory operations, e.g. to check if a directory exists.
import os

# To run git commands and retrieve corresponding output.
import subprocess

# For determining the machine architecture.
import platform

# For enforcing character limits for lines of texts.
import textwrap



# To check whether a package has been installed already.
from pkg_resources import DistributionNotFound, get_distribution

# For setting up target package.
from setuptools import setup, find_packages, Command



############################
## Authorship information ##
############################

__author__     = "Matthew Fitzpatrick"
__copyright__  = "Copyright 2023"
__credits__    = ["Matthew Fitzpatrick"]
__maintainer__ = "Matthew Fitzpatrick"
__email__      = "mrfitzpa@uvic.ca"
__status__     = "Development"



####################################
## Define functions and constants ##
####################################

target_pkg_name = "pynrand"

major_python_revision = 3
minimum_minor_python_revision = 0
minimum_python_version = (major_python_revision, minimum_minor_python_revision)

if not sys.version_info >= minimum_python_version:
    print("ERROR: ``{}`` requires Python version >= ".format(target_pkg_name),
          major_python_revision, ".", minimum_minor_python_revision,
          ", the script got called by:\n", sys.version, ".", sep="")
    sys.exit(1)



# Hard-codd version for people without git. Current non-production version.
MAJOR = 0
MINOR = 1
MICRO = 0
RELEASED = False
VERSION = '{0:d}.{1:d}.{2:d}'.format(MAJOR, MINOR, MICRO)



def get_git_revision():
    """Get revision hash of ``pynrand`` from git.

    Parameters
    ----------

    Returns
    -------
    revision : `str`
        Git revision hash of ``pynrand``.

    """
    if not os.path.exists('.git'):
        revision = "unknown"
    else:
        try:
            parsed_cmd = ['git', 'rev-parse', 'HEAD']
            cwd = os.path.dirname(os.path.abspath(__file__))
            stderr = subprocess.STDOUT

            cmd_output = subprocess.check_output(parsed_cmd,
                                                 cwd=cwd,
                                                 stderr=stderr)
            revision = cmd_output.decode().strip()

        except:
            revision = "unknown"

    return revision



def get_version_info():
    """Get version of ``pynrand`` from git.

    Parameters
    ----------

    Returns
    -------
    full_version : `str`
        Full version of ``pynrand``.

    """
    full_version = VERSION
    git_revision = get_git_revision()

    if not RELEASED:
        full_version += '.dev0+' + git_revision[:7]
    return full_version, git_revision



def write__version_py(full_version,
                      git_revision,
                      filename=target_pkg_name+"/_version.py"):
    """Write the version during compilation to file.

    Parameters
    ----------
    full_version : `str`
        Full of version of ``pynrand``.
    git_revision : `str`
        Git revision hash of ``pynrand``.
    filename : `str`, optional
        Filename of file containing information about the version currently
        being compiled.

    Returns
    -------

    """
    line = ("This file was generated from setup.py. It contains information "
            "about the version of ``{}`` currently installed on "
            "machine.".format(target_pkg_name))
    lines = textwrap.wrap(line, width=78, break_long_words=False)
    for line_idx, line in enumerate(lines):
        lines[line_idx] = "# " + line

    lines += ["",
              "",
              "",
              "############################",
              "## Authorship information ##",
              "############################",
              "",
              "__author__     = \"Matthew Fitzpatrick\"",
              "__copyright__  = \"Copyright 2023\"",
              "__credits__    = [\"Matthew Fitzpatrick\"]",
              "__maintainer__ = \"Matthew Fitzpatrick\"",
              "__email__      = \"mrfitzpa@uvic.ca\"",
              "__status__     = \"Development\"",
              "",
              "",
              "",
              "#########################",
              "## Version information ##",
              "#########################",
              "",
              "version = '{version!s}'",
              "short_version = 'v' + version",
              "released = {released!s}",
              "full_version = '{full_version!s}'",
              "git_revision = '{git_revision!s}'"]

    content = "\n".join(lines)
    content = content.format(version=VERSION,
                             full_version=full_version,
                             released=RELEASED,
                             git_revision=git_revision)

    with open(filename, 'w') as file_obj:
        print(filename)
        file_obj.write(content)

    return None



def read_requirements_file(filename):
    """Read requirements file and extract a set of library requirements.

    Parameters
    ----------
    filename : `str`
        Filename of requirements file.

    Returns
    -------
    requirements : array_like(`str`, ndim=1)
        Extracted set of library requirements.
    """
    with open(filename, 'r') as file_obj:
        requirements = file_obj.readlines()

    requirements = [line.strip() for line in requirements if line.strip()]

    return requirements


def read_extra_requirements():
    """Extract set of extra library requirements from the requirement files.

    Parameters
    ----------

    Returns
    -------
    extra_requirements : `dict` [`str`, array_like(`str`, ndim=1)]
        Extracted set of library requirements.
    """
    extra_requirements = \
        {'doc': read_requirements_file('requirements-doc.txt'),
         'examples': read_requirements_file('requirements-examples.txt')}

    extra_requirements['all'] = [requirement for requirement_subset
                                 in extra_requirements.values()
                                 for requirement in requirement_subset]

    return extra_requirements



def not_installed(pkg_name):
    r"""Check whether package has been installed.

    Parameters
    ----------
    pkg_name : `str`
        The name of the package.

    Returns
    -------
    result : `bool`
        Set to ``False`` if the package has already been installed. Otherwise,
        it is set to ``True``.
    """
    try:
        get_distribution(pkg_name)
        result = False
    except DistributionNotFound:
        result = True

    return result



def gen_minimal_requirements():
    r"""Generate the minimal list of required packages.

    Parameters
    ----------

    Returns
    -------
    minimal_requirements : `array_like` ('str`, ndim=1)
        The minimal list of required packages.
    """
    pkg_names = read_requirements_file('requirements.txt')

    minimal_requirements = []
    for pkg_name in pkg_names:
        try:
            get_distribution(pkg_name)
        except DistributionNotFound:
            minimal_requirements.append(pkg_name)

    return minimal_requirements



def clean():
    if sys.platform.startswith("win"):
        os.system("rmdir /s /q ./build")
        os.system("rmdir /s /q ./dist")
        os.system("rmdir /s /q ./embeam.egg-info")
        os.system("del /q ./*.pyc")
        os.system("del /q ./*.tgz")
        os.system("del /q ./embeam/_version.py")
    else:
        os.system("rm -vrf ./build ./dist ./*.pyc "
                  "./*.tgz ./*.egg-info ./embeam/_version.py")

    return None



class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        clean()



def setup_package():
    """Setup ``pynrand`` package.

    Parameters
    ----------

    Returns
    -------
    """
    # Change directory to root path of the repository.
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(src_path)

    full_version, git_revision = get_version_info()
    write__version_py(full_version, git_revision)

    setup_requires = ['setuptools']
    install_requires = gen_minimal_requirements()
    extras_require = read_extra_requirements()

    description = ("Contains serializable classes representing random number "
                   "generators.")

    setup(name=target_pkg_name,
          description=description,
          author="Matthew Fitzpatrick",
          author_email="mrfitzpa@uvic.ca",
          packages=find_packages(),
          version=full_version,
          setup_requires=setup_requires,
          install_requires=install_requires,
          extras_require=extras_require,
          cmdclass={'clean': CleanCommand})



if __name__ == "__main__":
    setup_package()
    clean()
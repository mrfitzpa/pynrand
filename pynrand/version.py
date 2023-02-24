"""A module for retrieving the version of this library.

The version is provided in the standard python format ``major.minor.revision``
as a string. Use ``pkg_resources.parse_version`` to compare different versions.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# To get version of Python being used in the current (virtual) environment.
import sys

# To run git commands and retrieve corresponding output.
import subprocess

# For getting the absolute file path of this file.
import os



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

# List of public objects in module.
__all__ = ["version",
           "released",
           "short_version",
           "git_revision",
           "full_version",
           "version_summary"]



# Name of package.
pkg_name = "pynrand"

# Hard-coded version for people without git. Current non-production version.
version = '0.1.0'

# Whether this is a released version or modified.
released = False

# Short version.
short_version = 'v' + version



def _get_git_revision():
    """Get revision hash of ``pynrand`` from git.

    Parameters
    ----------

    Returns
    -------
    revision : `str`
        Git revision hash of ``pynrand``.

    """
    try:
        parsed_cmd = ['git', 'rev-parse', 'HEAD']
        cwd = os.path.dirname(os.path.abspath(__file__))
        stderr = subprocess.STDOUT

        cmd_output = subprocess.check_output(parsed_cmd, cwd=cwd, stderr=stderr)
        revision = cmd_output.decode().strip()

    except:
        revision = "unknown"

    return revision

# The current git revision (if available).
git_revision = _get_git_revision()



def _get_full_version():
    """Get version of ``pynrand`` from git.

    Parameters
    ----------

    Returns
    -------
    full_version : `str`
        Full version of ``pynrand``.

    """
    full_version = version

    if not released:
        full_version += '.dev0+' + git_revision[:7]

    return full_version

# Full version string including a prefix containing the beginning of the git
# revision hash.
full_version = _get_full_version()



def _get_version_summary():
    """Get version summary of ``pynrand``.

    Parameters
    ----------

    Returns
    -------
    summary : `str`
        Version summary of ``pynrand``.

    """
    # Check versions of ``pynrand``.
    from . import _version
    if _version.version != version:
        raise ValueError(_get_version_summary_err_msg_1)



    # Generate summary.
    summary = "pynrand "
    summary += ("{lib_ver!s};\n"
                "git revision {git_rev!s} using\n"
                "python {python_ver!s}")

    summary = summary.format(lib_ver=full_version,
                             git_rev=git_revision,
                             python_ver=sys.version)
    return summary

# Summary of the versions as a string.
version_summary = _get_version_summary()



###########################
## Define error messages ##
###########################

_get_version_summary_err_msg_1 = \
    ("``{}`` version has changed since "
     "installation/compilation.".format(pkg_name))
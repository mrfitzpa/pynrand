"""Insert here a brief description of the library.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# Import child modules and packages of current package.
import pynrand.discrete
import pynrand.continuous
import pynrand.version



############################
## Authorship information ##
############################

__author__       = "Matthew Fitzpatrick"
__copyright__    = "Copyright 2023"
__credits__      = ["Matthew Fitzpatrick"]
__version__      = version.version
__full_version__ = version.full_version
__maintainer__   = "Matthew Fitzpatrick"
__email__        = "mrfitzpa@uvic.ca"
__status__       = "Development"



##################################
## Define classes and functions ##
##################################

# List of public objects in package.
__all__ = ["show_config"]



def show_config():
    """Print information about the version of ``pynrand`` and libraries it uses.

    """
    print(version.version_summary)

    return None



###########################
## Define error messages ##
###########################

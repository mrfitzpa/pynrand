"""A one-line description of the subpackage.

A more detailed description of the subpackage. The more detailed description can
span multiple lines.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For converting objects.
import czekitout.convert



# For defining classes derived from the classes
# :class:`pynrand._discrete.base.UniformSampler` and
# :class:`pynrand._discrete.base.CustomSampler`.
import pynrand._discrete.base

# Import submodules of subpackage.
import pynrand.discrete.nonnegative.integer
import pynrand.discrete.nonnegative.boolean



############################
## Authorship information ##
############################

__author__     = "Matthew Fitzpatrick"
__copyright__  = "Copyright 2023"
__credits__    = ["Matthew Fitzpatrick"]
__maintainer__ = "Matthew Fitzpatrick"
__email__      = "mrfitzpa@uvic.ca"
__status__     = "Development"



##################################
## Define classes and functions ##
##################################

# List of public objects in subpackage.
__all__ = ["UniformSampler",
           "CustomSampler"]



def _check_and_convert_sample_space(ctor_params):
    obj_name = "sample_space"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    sample_space = czekitout.convert.to_tuple_of_nonnegative_floats(**kwargs)

    return sample_space



class UniformSampler(pynrand._discrete.base.UniformSampler):
    r"""Insert description here.

    Parameters
    ----------
    sample_space : `array_like` (`float`, ndim=1), optional
        Insert description here.

    Attributes
    ----------
    core_attrs : `dict`, read-only
        A `dict` representation of the core attributes: each `dict` key is a
        `str` representing the name of a core attribute, and the corresponding
        `dict` value is the object to which said core attribute is set. The core
        attributes are the same as the construction parameters, except that 
        their values might have been updated since construction.

    """
    _validation_and_conversion_funcs = \
        {"sample_space": _check_and_convert_sample_space}

    def __init__(self, sample_space=(0, 1)):
        ctor_params = {"sample_space": sample_space}
        pynrand._discrete.base.UniformSampler.__init__(self, **ctor_params)

        return None



def _check_and_convert_weights(ctor_params):
    weights = pynrand._discrete.base._check_and_convert_weights(ctor_params)

    return weights



class CustomSampler(pynrand._discrete.base.CustomSampler):
    r"""Insert description here.

    Parameters
    ----------
    sample_space : `array_like` (`float`, ndim=1), optional
        Insert description here.
    weights : `array_like` (`float`, ndim=1) | `None`, optional
        Insert description here.

    Attributes
    ----------
    core_attrs : `dict`, read-only
        A `dict` representation of the core attributes: each `dict` key is a
        `str` representing the name of a core attribute, and the corresponding
        `dict` value is the object to which said core attribute is set. The core
        attributes are the same as the construction parameters, except that 
        their values might have been updated since construction.

    """
    _validation_and_conversion_funcs = \
        {"sample_space": _check_and_convert_sample_space,
         "weights": _check_and_convert_weights}

    def __init__(self, sample_space=(0, 1), weights=None):
        ctor_params = {"sample_space": sample_space, "weights": weights}
        pynrand._discrete.base.CustomSampler.__init__(self, **ctor_params)

        return None



###########################
## Define error messages ##
###########################

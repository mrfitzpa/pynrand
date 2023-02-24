"""Insert a one-line description of module.

A more detailed description of the module. The more detailed description can
span multiple lines.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For generating random numbers.
import numpy as np

# For converting objects.
import czekitout.convert



# For defining classes derived from the class :class:`pynrand._base.Sampler`.
import pynrand._base

# For defining classes derived from the class
# :class:`pynrand._continuous.base.UniformSampler`.
import pynrand._continuous.base



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

# List of public objects in module.
__all__ = ["UniformSampler",
           "GammaSampler"]



def _check_and_convert_lower_limit(ctor_params):
    obj_name = "lower_limit"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    lower_limit = czekitout.convert.to_nonnegative_float(**kwargs)

    return lower_limit



def _check_and_convert_upper_limit(ctor_params):
    upper_limit = \
        pynrand._continuous.base._check_and_convert_upper_limit(ctor_params)

    return upper_limit



class UniformSampler(pynrand._continuous.base.UniformSampler):
    r"""Insert description here.

    Parameters
    ----------
    lower_limit : `float`, optional
        Insert description here.
    upper_limit : `float`, optional
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
        {"lower_limit": _check_and_convert_lower_limit,
         "upper_limit": _check_and_convert_upper_limit}

    def __init__(self, lower_limit=0, upper_limit=1):
        ctor_params = {"lower_limit": lower_limit, "upper_limit": upper_limit}
        pynrand._continuous.base.UniformSampler.__init__(self, **ctor_params)

        return None



def _check_and_convert_shape(ctor_params):
    obj_name = "shape"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    shape = czekitout.convert.to_nonnegative_float(**kwargs)

    return shape



def _pre_serialize_shape(shape):
    serializable_rep = shape
    
    return serializable_rep



def _de_pre_serialize_shape(serializable_rep):
    shape = serializable_rep

    return shape



def _check_and_convert_scale(ctor_params):
    obj_name = "scale"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    scale = czekitout.convert.to_nonnegative_float(**kwargs)

    return scale



def _pre_serialize_scale(scale):
    serializable_rep = scale
    
    return serializable_rep



def _de_pre_serialize_scale(serializable_rep):
    scale = serializable_rep

    return scale



class GammaSampler(pynrand._base.Sampler):
    r"""Insert description here.

    Parameters
    ----------
    shape : `float`, optional
        Insert description here.
    scale : `float`, optional
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
    _validation_and_conversion_funcs = {"shape": _check_and_convert_shape,
                                        "scale": _check_and_convert_scale}

    _pre_serialization_funcs = {"shape": _pre_serialize_shape,
                                "scale": _pre_serialize_scale}

    _de_pre_serialization_funcs = {"shape": _de_pre_serialize_shape,
                                   "scale": _de_pre_serialize_scale}

    def __init__(self, shape=1, scale=1):
        ctor_params = {"shape": shape, "scale": scale}
        pynrand._base.Sampler.__init__(self, ctor_params)

        self._post_base_update()

        return None



    def _post_base_update(self):
        self._shape = self.core_attrs["shape"]
        self._scale = self.core_attrs["scale"]
        self._rng = np.random.default_rng()

        return None



    def update(self, core_attr_subset):
        super().update(core_attr_subset)
        self._post_base_update()

        return None



    def _draw(self, output_shape):
        sample = self._rng.gamma(shape=self._shape,
                                 scale=self._scale,
                                 size=output_shape)

        return sample



###########################
## Define error messages ##
###########################

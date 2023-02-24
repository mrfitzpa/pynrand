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
__all__ = ["UniformSampler"]



def _check_and_convert_lower_limit(ctor_params):
    obj_name = "lower_limit"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    lower_limit = czekitout.convert.to_float(**kwargs)

    return lower_limit



def _pre_serialize_lower_limit(lower_limit):
    serializable_rep = lower_limit
    
    return serializable_rep



def _de_pre_serialize_lower_limit(serializable_rep):
    lower_limit = serializable_rep

    return lower_limit



def _check_and_convert_upper_limit(ctor_params):
    obj_name = "upper_limit"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    upper_limit = czekitout.convert.to_float(**kwargs)

    lower_limit = _check_and_convert_lower_limit(ctor_params)
    if lower_limit >= upper_limit:
        raise ValueError(_check_and_convert_upper_limit_err_msg_1)

    return upper_limit



def _pre_serialize_upper_limit(upper_limit):
    serializable_rep = upper_limit
    
    return serializable_rep



def _de_pre_serialize_upper_limit(serializable_rep):
    upper_limit = serializable_rep

    return upper_limit



class UniformSampler(pynrand._base.Sampler):
    _validation_and_conversion_funcs = \
        {"lower_limit": _check_and_convert_lower_limit,
         "upper_limit": _check_and_convert_upper_limit}

    _pre_serialization_funcs = \
        {"lower_limit": _pre_serialize_lower_limit,
         "upper_limit": _pre_serialize_upper_limit}

    _de_pre_serialization_funcs = \
        {"lower_limit": _de_pre_serialize_lower_limit,
         "upper_limit": _de_pre_serialize_upper_limit}

    def __init__(self, lower_limit=0, upper_limit=1):
        ctor_params = {"lower_limit": lower_limit, "upper_limit": upper_limit}
        pynrand._base.Sampler.__init__(self, ctor_params)

        self._post_base_update()

        return None



    def _post_base_update(self):
        self._lower_limit = self.core_attrs["lower_limit"]
        self._upper_limit = self.core_attrs["upper_limit"]
        self._rng = np.random.default_rng()

        return None



    def update(self, core_attr_subset):
        super().update(core_attr_subset)
        self._post_base_update()

        return None



    def _draw(self, output_shape):
        sample = self._rng.uniform(low=self._lower_limit,
                                   high=self._upper_limit,
                                   size=output_shape)

        return sample



###########################
## Define error messages ##
###########################

_check_and_convert_upper_limit_err_msg_1 = \
    ("The object ``upper_limit`` must be a real number satisfying "
     "``lower_limit < upper_limit``.")

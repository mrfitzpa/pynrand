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
__all__ = ["BernoulliSampler"]



def _check_and_convert_probability_of_yes(ctor_params):
    obj_name = "probability_of_yes"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    probability_of_yes = czekitout.convert.to_nonnegative_float(**kwargs)

    if probability_of_yes > 1:
        raise ValueError(_check_and_convert_probability_of_yes_err_msg_1)

    return probability_of_yes



def _pre_serialize_probability_of_yes(probability_of_yes):
    serializable_rep = probability_of_yes
    
    return serializable_rep



def _de_pre_serialize_probability_of_yes(serializable_rep):
    probability_of_yes = serializable_rep

    return probability_of_yes



class BernoulliSampler(pynrand._base.Sampler):
    r"""Insert description here.

    Parameters
    ----------
    probability_of_yes : `float`, optional
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
        {"probability_of_yes": _check_and_convert_probability_of_yes}
    
    _pre_serialization_funcs = \
        {"probability_of_yes": _pre_serialize_probability_of_yes}

    _de_pre_serialization_funcs = \
        {"probability_of_yes": _de_pre_serialize_probability_of_yes}

    def __init__(self, probability_of_yes=0.5):
        ctor_params = {"probability_of_yes": probability_of_yes}
        pynrand._base.Sampler.__init__(self, ctor_params)

        self._post_base_update()

        return None



    def _post_base_update(self):
        self._p = self.core_attrs["probability_of_yes"]
        self._rng = np.random.default_rng()

        return None



    def update(self, core_attr_subset):
        super().update(core_attr_subset)
        self._post_base_update()

        return None



    def _draw(self, output_shape):
        sample = self._rng.binomial(n=1, p=self._p, size=output_shape)

        return sample



###########################
## Define error messages ##
###########################

_check_and_convert_probability_of_yes_err_msg_1 = \
    ("The object ``probability_of_yes`` must be a nonnegative number less than "
     "or equal to unity.")

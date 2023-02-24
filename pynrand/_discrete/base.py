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
__all__ = ["UniformSampler",
           "CustomSampler"]



def _check_and_convert_sample_space(ctor_params):
    obj_name = "sample_space"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    sample_space = czekitout.convert.to_tuple_of_floats(**kwargs)

    return sample_space



def _pre_serialize_sample_space(sample_space):
    serializable_rep = sample_space
    
    return serializable_rep



def _de_pre_serialize_sample_space(serializable_rep):
    sample_space = serializable_rep

    return sample_space



class UniformSampler(pynrand._base.Sampler):
    _validation_and_conversion_funcs = \
        {"sample_space": _check_and_convert_sample_space}

    _pre_serialization_funcs = \
        {"sample_space": _pre_serialize_sample_space}

    _de_pre_serialization_funcs = \
        {"sample_space": _de_pre_serialize_sample_space}

    def __init__(self, sample_space=(0, 1)):
        ctor_params = {"sample_space": sample_space}
        pynrand._base.Sampler.__init__(self, ctor_params)

        self._post_base_update()

        return None



    def _post_base_update(self):
        self._sample_space = np.array(self.core_attrs["sample_space"])
        self._num_elems_in_sample_space = len(self._sample_space)
        self._rng = np.random.default_rng()

        return None



    def update(self, core_attr_subset):
        super().update(core_attr_subset)
        self._post_base_update()

        return None



    def _draw(self, output_shape):
        num_elems_in_sample_space = self._num_elems_in_sample_space
        sample_space_indices = self._rng.integers(num_elems_in_sample_space,
                                                  size=output_shape)
        sample = self._sample_space[sample_space_indices]

        return sample



def _check_and_convert_weights(ctor_params):
    sample_space = _check_and_convert_sample_space(ctor_params)

    obj_name = "weights"
    if ctor_params[obj_name] is None:
        weights = tuple(1/len(sample_space) for _ in sample_space)
    else:
        kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
        try:
            weights = czekitout.convert.to_tuple_of_nonnegative_floats(**kwargs)
        except:
            raise TypeError(_check_and_convert_weights_err_msg_1)

    if len(weights) != len(sample_space):
        raise IndexError(_check_and_convert_weights_err_msg_1)

    return weights



def _pre_serialize_weights(weights):
    serializable_rep = weights
    
    return serializable_rep



def _de_pre_serialize_weights(serializable_rep):
    weights = serializable_rep

    return weights



class CustomSampler(pynrand._base.Sampler):
    _validation_and_conversion_funcs = \
        {"sample_space": _check_and_convert_sample_space,
         "weights": _check_and_convert_weights}

    _pre_serialization_funcs = \
        {"sample_space": _pre_serialize_sample_space,
         "weights": _pre_serialize_weights}

    _de_pre_serialization_funcs = \
        {"sample_space": _de_pre_serialize_sample_space,
         "weights": _de_pre_serialize_weights}

    def __init__(self, sample_space=(0, 1), weights=None):
        ctor_params = {"sample_space": sample_space, "weights": weights}
        pynrand._base.Sampler.__init__(self, ctor_params)

        self._post_base_update()

        return None



    def _post_base_update(self):
        self._sample_space = np.array(self.core_attrs["sample_space"])

        weights = np.array(self.core_attrs["weights"])
        self._normalized_weights = weights / np.sum(weights)

        self._rng = np.random.default_rng()

        return None



    def update(self, core_attr_subset):
        super().update(core_attr_subset)
        self._post_base_update()

        return None



    def _draw(self, output_shape):
        sample = self._rng.choice(self._sample_space,
                                  size=output_shape,
                                  p=self._normalized_weights)

        return sample



###########################
## Define error messages ##
###########################

_check_and_convert_weights_err_msg_1 = \
    ("The object ``weights`` must be of the type `NoneType`, or it must be a "
     "sequence of nonnegative numbers equal in length to the sequence "
     "specified by ``sample_space``.")

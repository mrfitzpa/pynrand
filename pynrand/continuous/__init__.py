"""A one-line description of the subpackage.

A more detailed description of the subpackage. The more detailed description can
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

# Import submodules of subpackage.
import pynrand.continuous.nonnegative



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
           "NormalSampler",
           "CircularNormalSampler"]



def _check_and_convert_lower_limit(ctor_params):
    obj_name = "lower_limit"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    lower_limit = czekitout.convert.to_float(**kwargs)

    return lower_limit



def _check_and_convert_upper_limit(ctor_params):
    upper_limit = \
        pynrand._continuous.base._check_and_convert_upper_limit(ctor_params)

    return upper_limit



class UniformSampler(pynrand._continuous.base.UniformSampler):
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
        {"lower_limit": _check_and_convert_lower_limit,
         "upper_limit": _check_and_convert_upper_limit}

    def __init__(self, lower_limit=0, upper_limit=1):
        ctor_params = {"lower_limit": lower_limit, "upper_limit": upper_limit}
        pynrand._continuous.base.UniformSampler.__init__(self, **ctor_params)

        return None



def _check_and_convert_mean(ctor_params):
    obj_name = "mean"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    mean = czekitout.convert.to_float(**kwargs)

    return mean



def _pre_serialize_mean(mean):
    serializable_rep = mean
    
    return serializable_rep



def _de_pre_serialize_mean(serializable_rep):
    mean = serializable_rep

    return mean



def _check_and_convert_std_dev(ctor_params):
    obj_name = "std_dev"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    std_dev = czekitout.convert.to_nonnegative_float(**kwargs)

    return std_dev



def _pre_serialize_std_dev(std_dev):
    serializable_rep = std_dev
    
    return serializable_rep



def _de_pre_serialize_std_dev(serializable_rep):
    std_dev = serializable_rep

    return std_dev



class NormalSampler(pynrand._base.Sampler):
    r"""Insert description here.

    Parameters
    ----------
    mean : `float`, optional
        Insert description here.
    std_dev : `float`, optional
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
    _validation_and_conversion_funcs = {"mean": _check_and_convert_mean,
                                        "std_dev": _check_and_convert_std_dev}

    _pre_serialization_funcs = {"mean": _pre_serialize_mean,
                                "std_dev": _pre_serialize_std_dev}

    _de_pre_serialization_funcs = {"mean": _de_pre_serialize_mean,
                                   "std_dev": _de_pre_serialize_std_dev}

    def __init__(self, mean=0, std_dev=1):
        ctor_params = {"mean": mean, "std_dev": std_dev}
        pynrand._base.Sampler.__init__(self, ctor_params)

        self._post_base_update()

        return None



    def _post_base_update(self):
        self._mean = self.core_attrs["mean"]
        self._std_dev = self.core_attrs["std_dev"]
        self._rng = np.random.default_rng()

        return None



    def update(self, core_attr_subset):
        super().update(core_attr_subset)
        self._post_base_update()

        return None



    def _draw(self, output_shape):
        sample = self._rng.normal(loc=self._mean,
                                  scale=self._std_dev,
                                  size=output_shape)

        return sample



def _check_and_convert_mu(ctor_params):
    obj_name = "mu"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    mu = czekitout.convert.to_float(**kwargs)

    return mu



def _pre_serialize_mu(mu):
    serializable_rep = mu
    
    return serializable_rep



def _de_pre_serialize_mu(serializable_rep):
    mu = serializable_rep

    return mu



def _check_and_convert_kappa(ctor_params):
    obj_name = "kappa"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    kappa = czekitout.convert.to_nonnegative_float(**kwargs)

    return kappa



def _pre_serialize_kappa(kappa):
    serializable_rep = kappa
    
    return serializable_rep



def _de_pre_serialize_kappa(serializable_rep):
    kappa = serializable_rep

    return kappa



class CircularNormalSampler(pynrand._base.Sampler):
    r"""Insert description here.

    Parameters
    ----------
    mu : `float`, optional
        Insert description here.
    kappa : `float`, optional
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
    _validation_and_conversion_funcs = {"mu": _check_and_convert_mu,
                                        "kappa": _check_and_convert_kappa}

    _pre_serialization_funcs = {"mu": _pre_serialize_mu,
                                "kappa": _pre_serialize_kappa}

    _de_pre_serialization_funcs = {"mu": _de_pre_serialize_mu,
                                   "kappa": _de_pre_serialize_kappa}

    def __init__(self, mu=0, kappa=1):
        ctor_params = {"mu": mu, "kappa": kappa}
        pynrand._base.Sampler.__init__(self, ctor_params)

        self._post_base_update()

        return None



    def _post_base_update(self):
        self._mu = self.core_attrs["mu"]
        self._kappa = self.core_attrs["kappa"]
        self._rng = np.random.default_rng()

        return None



    def update(self, core_attr_subset):
        super().update(core_attr_subset)
        self._post_base_update()

        return None



    def _draw(self, output_shape):
        sample = self._rng.vonmises(mu=self._mu,
                                    kappa=self._kappa,
                                    size=output_shape)

        return sample



###########################
## Define error messages ##
###########################

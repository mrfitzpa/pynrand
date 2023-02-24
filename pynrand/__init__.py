"""Insert here a brief description of the library.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For validating and converting objects, and for resolving the fully qualified
# names of classes.
import czekitout.check
import czekitout.convert
import czekitout.name



# For defining classes derived from the class :class:`pynrand._base.Sampler`.
import pynrand._base

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
__all__ = ["show_config",
           "Sampler"]



def show_config():
    """Print information about the version of ``pynrand`` and libraries it uses.

    """
    print(version.version_summary)

    return None



_sampler_classes = (pynrand.discrete.UniformSampler,
                    pynrand.discrete.CustomSampler,
                    pynrand.discrete.nonnegative.UniformSampler,
                    pynrand.discrete.nonnegative.CustomSampler,
                    pynrand.discrete.nonnegative.integer.UniformSampler,
                    pynrand.discrete.nonnegative.integer.CustomSampler,
                    pynrand.discrete.nonnegative.boolean.BernoulliSampler,
                    pynrand.continuous.UniformSampler,
                    pynrand.continuous.NormalSampler,
                    pynrand.continuous.CircularNormalSampler,
                    pynrand.continuous.nonnegative.UniformSampler,
                    pynrand.continuous.nonnegative.GammaSampler)



def _check_and_convert_name(ctor_params):
    obj_name = "name"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    name = czekitout.convert.to_str_from_str_like(**kwargs)

    get_class_name = czekitout.name.fully_qualified_class_name
    accepted_strings = tuple(get_class_name(cls) for cls in _sampler_classes)
    
    kwargs["obj"] = name
    kwargs["accepted_strings"] = accepted_strings
    czekitout.check.if_one_of_any_accepted_strings(**kwargs)

    return name



def _pre_serialize_name(name):
    serializable_rep = name
    
    return serializable_rep



def _de_pre_serialize_name(serializable_rep):
    name = serializable_rep

    return name



def _check_and_convert_params(ctor_params):
    obj_name = "params"
    kwargs = {"obj": ctor_params[obj_name], "obj_name": obj_name}
    params = czekitout.convert.to_dict(**kwargs)

    name = _check_and_convert_name(ctor_params)
    get_class_name = czekitout.name.fully_qualified_class_name
    
    for sampler_cls in _sampler_classes:
        if name == get_class_name(sampler_cls):
            try:
                sampler_cls(**params)
                break
            except:
                err_msg = _check_and_convert_params_err_msg_1.format(name)
                raise ValueError(err_msg)

    return params



def _pre_serialize_params(params):
    serializable_rep = params
    
    return serializable_rep



def _de_pre_serialize_params(serializable_rep):
    params = serializable_rep

    return params



class Sampler(pynrand._base.Sampler):
    r"""Insert description here.

    Parameters
    ----------
    name : `str`, optional
        Insert description here.
    params : `dict`, optional
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
    _validation_and_conversion_funcs = {"name": _check_and_convert_name,
                                        "params": _check_and_convert_params}

    _pre_serialization_funcs = {"name": _pre_serialize_name,
                                "params": _pre_serialize_params}

    _de_pre_serialization_funcs = {"name": _de_pre_serialize_name,
                                   "params": _de_pre_serialize_params}

    def __init__(self, name="pynrand.discrete.CustomSampler", params=dict()):
        ctor_params = {"name": name, "params": params}
        pynrand._base.Sampler.__init__(self, ctor_params)

        self._post_base_update()

        return None



    def _post_base_update(self):
        name = self.core_attrs["name"]
        params = self.core_attrs["params"]
        get_class_name = czekitout.name.fully_qualified_class_name
    
        for sampler_cls in _sampler_classes:
            if name == get_class_name(sampler_cls):
                self._sampler = sampler_cls(**params)

        return None



    def update(self, core_attr_subset):
        super().update(core_attr_subset)
        self._post_base_update()

        return None



    def _draw(self, output_shape):
        sample = self._sampler._draw(output_shape)

        return sample



###########################
## Define error messages ##
###########################

_check_and_convert_params_err_msg_1 = \
    ("The object ``params`` specifies a set of construction parameters that "
     "are incompatible with the sampler class `{}`, specified by the object "
     "``name``. See the documentation for the aforementioned class for details "
     "on its constructions parameters, and see the traceback above for "
     "further details on the source of the error.")

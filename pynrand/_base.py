"""Insert a one-line description of module.

A more detailed description of the module. The more detailed description can
span multiple lines.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For defining abstract base classes.
import abc



# For converting objects.
import czekitout.convert

# For defining classes that support enforced validation, updatability,
# pre-serialization, and de-serialization.
import fancytypes



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
__all__ = ["Sampler"]



class Sampler(fancytypes.PreSerializableAndUpdatable, abc.ABC):
    _validation_and_conversion_funcs = dict()

    _pre_serialization_funcs = dict()

    _de_pre_serialization_funcs = dict()

    def __init__(self, ctor_params):
        fancytypes.PreSerializableAndUpdatable.__init__(self, ctor_params)

        return None



    def draw(self, output_shape=None):
        r"""Insert description here.

        Parameters
        ----------
        output_shape : `array_like` (`int`, ndim=1) | `None`, optional
            Insert description here.

        Returns
        -------
        sample : `int` | `float` | `array_like` (`int`) | `array_like` (`float`)
            Insert description here.

        """
        if output_shape is not None:
            try:
                czekitout.convert.to_tuple_of_nonnegative_ints(output_shape,
                                                               "output_shape")
            except:
                raise TypeError(_sampler_err_msg_1)
            
        sample = self._draw(output_shape)
        
        return sample



    @abc.abstractmethod
    def _draw(self, output_shape):
        pass



###########################
## Define error messages ##
###########################

_sampler_err_msg_1 = \
    ("The object ``output_shape`` must be of the type `NoneType`, or it must "
     "be a sequence of nonnegative integers.")

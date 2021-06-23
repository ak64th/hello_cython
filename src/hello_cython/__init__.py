from hello_cython.core import square

from hello_cython.utils import echo


def biquadrate(x):
    return square(square(x))

# First level modeling
# Classes for building a logical base for working with digital data
# First level modeling: combined and memory inputs
# made class with type 
# Basic switchable inputs

from bitarray import bitarray

# numericl type for numeric computation
# dynamic type for other computation


#Numerical computation:
#================================================================

def input_init(self, n: int=64, fill: bool=False, *args) -> None:
    """ Any data with a specific length is modeled here.

        *Args: this is the n bits inputed
        fill: if True then fill the data with the specified
    """
    if n < 2 : raise ValueError("Invalid length")

    index = 0
    self._input = bitarray(n)
    if fill:
        for arg in args:
            self._input[index] = arg
            index += 1
        del index


def input_set_item(self, key) -> None:
    """Append the given key and cerculate Right"""

    self._input.append(key)
    self._input.remove(self._input[0])

def input_get_item(self, key) -> bitarray:
    return self._input[key]

def input_len_item(self):
    return self._input.count()

def input_del_item(self, index: int=0, del_world: bool=False) -> None:
    """Deletes an element or deletes the whole"""
    if del_world:
        del self._input
        return None
    self._input[index] = 0

def input_str(self) -> str:
    return f"this bits in divice is:{self._input.count()} \n {50*"="}\n numerical is True"

# class with slots inputs
Input_Numerical_Data = type('',(), {

    '__slots__': ("_input"),

    '__init__': input_init,

    '__setitem__': input_set_item,
    '__getitem__': input_get_item,
    '__len__': input_len_item,
    '__delitem__': input_del_item,
    
    '__str__': input_str

})

#============================================================================


"""An example of a function definition"""

from re import A


def my_max(a: int b: int) -> int:   # signature line (contract)
    """return the greatest argument"""  # docstring
    if a >= b:   # the body block
        return a 
    else:
        return b

print(my_max(10+1, 10))
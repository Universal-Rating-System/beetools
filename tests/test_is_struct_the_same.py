
'''Testing is_struct_the_same()'''

from pathlib import Path
from beetools import Archiver, is_struct_the_same

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))
def test_is_struct_the_same_list_eq():
    '''Testing is_struct_the_same_list_eq()'''
    x = [1, 2]
    y = [1, 2]
    assert is_struct_the_same(x, y)


def test_is_struct_the_same_dict_eq():
    '''Testing is_struct_the_same_dict_eq()'''
    x = {1: "One", 2: "Two"}
    y = {2: "Two", 1: "One"}
    assert is_struct_the_same(x, y)

def test_is_struct_the_same_dict_diff_keys():
    '''Testing is_struct_the_same_dict_diff_keys()'''
    x = {1: "One", 3: "Two"}
    y = {1: "One", 2: "Two"}
    assert not is_struct_the_same(x, y)

def test_is_struct_the_same_dict_neq():
    '''Testing is_struct_the_same_dict_neq()'''
    y = {2: "Two", 1: "One"}
    z = {2: "Two", 1: "Three"}
    assert not is_struct_the_same(y, z, "ref str")

def test_is_struct_the_same_len():
    '''Testing is_struct_the_same_len()'''
    x = [1, 2]
    y = [1, 2, 3]
    assert not is_struct_the_same(x, y)

# test_is_struct_the_same_list_eq()
# test_is_struct_the_same_dict_eq()
# test_is_struct_the_same_dict_diff_keys()
# test_is_struct_the_same_dict_neq()
# test_is_struct_the_same_len()
del b_tls

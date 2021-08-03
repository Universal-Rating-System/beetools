
'''Testing example_virtual_environment()'''

from pathlib import Path
from beetools import Archiver, example_virtual_environment

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_example_virtual_environment_simple():
    '''Testing example_virtual_environment()'''
    assert example_virtual_environment()

# test_msg_ok_simple()
del b_tls

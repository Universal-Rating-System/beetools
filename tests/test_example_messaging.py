
'''Testing example_messaging()'''

from pathlib import Path
from beetools import Archiver, example_messaging

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_example_messaging():
    '''Testing example_messaging()'''
    assert example_messaging()

# test_msg_ok_simple()
del b_tls

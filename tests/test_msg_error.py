
'''Testing msg_error()'''

from pathlib import Path
from beetools import Archiver, msg_error

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_msg_error_simple():
    '''Testing msg_error_simple()'''
    assert msg_error("Error message") == "\x1b[31mError message\x1b[0m"

# test_msg_error_simple()
del b_tls

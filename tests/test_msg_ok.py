
'''Testing msg_ok()'''

from pathlib import Path
from beetools import Archiver, msg_ok

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_msg_ok_simple():
    '''Testing msg_ok_simple()'''
    assert msg_ok("OK message") == "\x1b[32mOK message\x1b[0m"

# test_msg_ok_simple()
del b_tls

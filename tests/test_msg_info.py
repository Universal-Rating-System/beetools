'''Testing msg_info()'''

from pathlib import Path
from beetools import Archiver, msg_info

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_msg_info_simple():
    '''Testing msg_info_simple()'''
    assert msg_info("Info message") == "\x1b[33mInfo message\x1b[0m"

# test_msg_info_simple()
del b_tls

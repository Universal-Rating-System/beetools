'''Testing msg_header()'''

from pathlib import Path
from beetools import Archiver, msg_header

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_msg_header_simple():
    '''Testing msg_header_simple()'''
    assert msg_header("Header message") == "\x1b[36mHeader message\x1b[0m"

# test_msg_header_simple()
del b_tls


'''Testing msg_display()'''

from pathlib import Path
from beetools import Archiver, msg_display

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_msg_display_simple():
    '''Testing msg_display()'''
    assert msg_display("Display message") == "\x1b[37mDisplay message                               "

# test_msg_display_simple()
del b_tls

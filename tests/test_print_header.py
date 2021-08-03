
'''Testing print_header'''

from pathlib import Path
from beetools import Archiver

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'


def test_print_header_simple():
    '''Testing print_header_simple()'''
    b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))
    assert b_tls.print_header()

# test_print_header_simple()

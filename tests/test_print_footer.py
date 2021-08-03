'''Testing print_footer()'''

from pathlib import Path
from beetools import Archiver

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'


def test_print_footer_simple():
    '''Testing print_footer_simple()'''
    b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))
    assert b_tls.print_footer()

# test_print_footer_simple()

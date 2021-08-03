
'''Testing example_scripting()'''

from pathlib import Path
from beetools import Archiver, example_scripting

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_example_scripting_simple():
    '''Testing example_scripting()'''
    assert example_scripting()

# test_msg_ok_simple()
del b_tls

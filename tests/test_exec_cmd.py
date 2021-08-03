
'''Testing exec_cmd()'''

from pathlib import Path
from beetools import Archiver, exec_cmd

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_exec_cmd_simple():
    '''Testing exec_cmd()'''
    assert exec_cmd(["echo", "Hello"])

# test_exec_cmd_simple()
del b_tls

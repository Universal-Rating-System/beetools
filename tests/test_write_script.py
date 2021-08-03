
'''Testing exec_batch()'''

from pathlib import Path
from beetools import Archiver, write_script, get_tmp_fldr

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_write_script_simple():
    '''Testing exec_batch_in_session()'''
    script_pth = get_tmp_fldr() / _name
    cmds = [
        ['echo', 'Hello'],
        ['echo', 'Goodbye'],
    ]
    assert write_script(script_pth,cmds) == 'echo Hello\necho Goodbye\n'

test_write_script_simple()
del b_tls

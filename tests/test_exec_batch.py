
'''Testing exec_batch()'''

from pathlib import Path
from beetools import Archiver, exec_batch, get_tmp_fldr, get_os, rm_tree, WINDOWS, LINUX, MACOS

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_exec_batch_simple():
    '''Testing exec_batch_in_session()'''
    tmp_test = get_tmp_fldr() / "test"
    tmp_t1 = tmp_test / "T1"
    if tmp_test.exists():
        rm_tree(tmp_test)
    if get_os() in [LINUX, MACOS]:
        cmds = [
            ['mkdir', '-p', '{}'.format(tmp_t1)],
            ['ls', '-l', '{}'.format(tmp_test)],
        ]
    elif get_os() == WINDOWS:
        cmds = [
            ['md','{}'.format(tmp_t1)],
            ['dir', '/B', '{}'.format(tmp_test)],
        ]
    assert exec_batch(cmds, p_verbose=False)

test_exec_batch_simple()
del b_tls

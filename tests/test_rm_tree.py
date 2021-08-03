
'''Testing do_bash_script()'''

from pathlib import Path
from beetools import Archiver, exec_batch_in_session, get_os, get_tmp_fldr, rm_tree, WINDOWS, LINUX, MACOS

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_rm_tree():
    '''Testing rm_tree()'''
    tmp_test = get_tmp_fldr() / 'test'
    tmp_t1 = tmp_test / 'T1'
    if get_os() == WINDOWS:
        cmd = ['md {}'.format(tmp_t1)]
    elif get_os() in [LINUX, MACOS]:
        cmd = ['mkdir -p {}'.format(tmp_t1)]
    exec_batch_in_session(cmd, p_verbose=False)
    t_file = tmp_test / Path( 't.tmp')
    t_file.touch(mode=0o666, exist_ok=True)
    t_file = tmp_t1 / Path( 't.tmp')
    t_file.touch(mode=0o666, exist_ok=True)
    assert rm_tree(tmp_test, p_crash = True)

# test_rm_tree()
del b_tls

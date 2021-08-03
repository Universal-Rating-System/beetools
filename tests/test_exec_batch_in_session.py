
'''Testing exec_batch_in_session()'''

from pathlib import Path
from beetools import Archiver, exec_batch_in_session, get_tmp_fldr, get_os, WINDOWS, LINUX, MACOS

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'


def test_exec_batch_in_session_simple():
    '''Testing exec_batch_in_session()'''
    b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))
    tmp_test = get_tmp_fldr() / "test"
    tmp_t1 = tmp_test / "T1"
    if get_os() in [LINUX, MACOS]:
        batch = [
            "mkdir -p {}".format(tmp_t1),
            "ls -l {}".format(tmp_test),
            "rm -R {}".format(tmp_test),
        ]
    elif get_os() == WINDOWS:
        batch = [
            "md {}".format(tmp_t1),
            "dir /B {}".format(tmp_test),
            "rd /Q /S {}".format(tmp_test),
        ]
    assert exec_batch_in_session(batch, p_verbose=False)
    del b_tls

# test_exec_batch_in_session_simple()

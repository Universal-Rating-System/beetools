
'''Testing rm_locked_file()'''

from pathlib import Path
from beetools import Archiver, get_os, get_tmp_fldr, rm_locked_file,  WINDOWS, LINUX, MACOS

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_rm_locked_file_simple():
    '''Testing rm_locked_file_simple()'''
    tmp_test = get_tmp_fldr() / "test"
    if get_os() in [LINUX, MACOS]:
        cmd = [
            "mkdir -p {}".format(tmp_test)
        ]
    elif get_os() == WINDOWS:
        cmd = [
            "md {}".format(tmp_test)
        ]
    assert rm_locked_file(tmp_test)

# test_rm_locked_file_simple()

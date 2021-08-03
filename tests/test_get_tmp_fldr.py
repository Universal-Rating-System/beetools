
'''Testing get_tmp_fldr()'''

import os
from pathlib import Path
from beetools import Archiver,get_os, get_tmp_fldr, WINDOWS, LINUX, MACOS

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_get_tmp_fldr_simple():
    '''Testing et_tmp_fldr()'''
    if get_os() == LINUX:
        tmp_fldr = Path("/tmp")
    elif get_os() == WINDOWS:
        tmp_fldr = Path(os.environ["TEMP"])
    elif get_os() == MACOS:
        tmp_fldr = Path(os.environ["TMPDIR"])
    assert get_tmp_fldr() == tmp_fldr

# test_get_tmp_fldr_simple()
del b_tls
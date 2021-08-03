
'''Testing get_venv_fldr()'''

import os
from pathlib import Path
from beetools import Archiver, get_os, get_tmp_fldr, get_venv_fldr, WINDOWS, LINUX, MACOS

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_get_venv_fldr_simple():
    '''Testing get_venv_fldr()'''
    if get_os() in [LINUX, MACOS]:
        tmp_fldr = "/tmp"
    elif get_os() == WINDOWS:
        tmp_fldr = os.environ["TEMP"]
    assert str(get_venv_fldr(get_tmp_fldr(), "bee-project")) == str(
        Path(tmp_fldr, "bee-project_env")
    )

# test_get_venv_fldr_simple()
del b_tls
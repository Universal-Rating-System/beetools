
'''Testing activate_venv_cmd()'''

from pathlib import Path
import sys
from beetools import Archiver, get_os, WINDOWS, LINUX, MACOS

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_get_os_simple():
    '''Testing get_os()'''
    if sys.platform.startswith("win32"):
        curr_os = WINDOWS
    elif sys.platform.startswith("linux"):
        curr_os = LINUX
    elif sys.platform.startswith("darwin"):
        curr_os = MACOS
    assert get_os() == curr_os

# test_get_os_simple()
del b_tls

'''Testing set_up_venv()'''

from pathlib import Path
from beetools import Archiver, get_os, exec_cmd, get_venv_fldr, get_tmp_fldr, set_up_venv, LINUX, WINDOWS, MACOS

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_set_up_venv_simple():
    '''Testing set_up_venv()'''
    project_name = "new-project"
    if get_os() in [LINUX, MACOS]:
        exec_cmd(
            ["sudo", "rm", "-R", "-f", str(get_venv_fldr(get_tmp_fldr(), project_name))], p_crash=False
        )
    elif get_os() == WINDOWS:
        exec_cmd(["rd", "/S", "/Q", str(get_venv_fldr(get_tmp_fldr(), project_name))], p_crash=False)
    assert set_up_venv(get_tmp_fldr(), "new-project", ["pip", "wheel"], p_verbose=False)

# test_set_up_venv_simple()
del b_tls

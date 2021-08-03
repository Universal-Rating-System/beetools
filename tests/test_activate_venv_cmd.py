
'''Testing activate_venv_cmd()'''

from pathlib import Path
from beetools import Archiver, activate_venv_cmd, get_os, get_tmp_fldr, WINDOWS, LINUX, MACOS

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

def test_activate_venv_cmd_simple():
    '''Testing activate_venv()'''
    b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))
    if get_os() == WINDOWS:
        cmd = "CALL " + str(
            get_tmp_fldr() / Path("bee-project_env", "Scripts", "activate")
        )
    elif get_os() == [LINUX, MACOS]:
        cmd = "source " + str(
            get_tmp_fldr() / Path("bee-project_env", "bin", "activate")
        )
    assert activate_venv_cmd(get_tmp_fldr(), "bee-project") == cmd
    del b_tls

# test_activate_venv_cmd_simple()

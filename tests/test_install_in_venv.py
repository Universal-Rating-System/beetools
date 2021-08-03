
'''Testing install_in_venv()'''

import os
from pathlib import Path
from beetools import Archiver, exec_cmd, get_os, get_tmp_fldr, get_venv_fldr, install_in_venv, set_up_venv, WINDOWS, LINUX, MACOS

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_install_in_venv_simple():
    '''Testing install_in_venv()'''
    project_name = "new-project"
    if get_os() in [LINUX, MACOS]:
        exec_cmd(
            ["sudo", "rm", "-R", "-f", str(get_venv_fldr(get_tmp_fldr(), project_name))]
        )
    elif get_os() == WINDOWS:
        exec_cmd(["rd", "/S", "/Q", str(get_venv_fldr(get_tmp_fldr(), project_name))], p_crash = False)
    set_up_venv(get_tmp_fldr(), project_name, ["pip"], p_verbose=True)
    assert install_in_venv(
        get_tmp_fldr(),
        project_name,
        ["echo Installing in VEnv", "pip install wheel", "echo Done!"],
    )

# test_install_in_venv_simple()
del b_tls
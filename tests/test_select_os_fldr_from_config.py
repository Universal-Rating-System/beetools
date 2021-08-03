
'''Testing select_os_fldr_from_config()'''

import configparser
from pathlib import Path
from beetools import Archiver, get_os, select_os_fldr_from_config, LINUX, WINDOWS, MACOS

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_select_os_fldr_from_config_simple():
    '''Testing select_os_fldr_from_config_simple()'''
    cnf = configparser.ConfigParser()
    cnf.read_dict(
        {
            "Folders": {
                "windows1_MyFolderOnSystem": "c:\\Program Files",
                "windows2_MyFolderOnSystem": "c:\\Program Files (x86)",
                "linux1_MyFolderOnSystem": "/usr/local/bin",
                "linux2_MyFolderOnSystem": "/bin",
                "macos1_MyFolderOnSystem": "/System",
                "macos2_MyFolderOnSystem": "/Application",
            }
        }
    )
    if get_os() == LINUX:
        fldr = "/usr/local/bin"
    elif get_os() == WINDOWS:
        fldr = "c:\\Program Files"
    elif get_os() == MACOS:
        fldr = "/System"
    assert str(select_os_fldr_from_config(cnf, "Folders", "MyFolderOnSystem")) == fldr

# test_select_os_fldr_from_config_simple()
del b_tls

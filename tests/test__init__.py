
'''Testing __init__()'''

from pathlib import Path
from beetools import Archiver, DEF_LOG_LEV, DEF_LOG_LEV_FILE, DEF_LOG_LEV_CON, \
                     LOG_FILE_FORMAT, LOG_CONSOLE_FORMAT, LOG_DATE_FORMAT, \
                     LONG_DATE_FORMAT, TIME_FORMAT, BAR_LEN, MSG_LEN, CRASH_RETRY, \
                     WINDOWS, LINUX, MACOS, AIX


_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

def test__init__simple():
    '''Testing __init__()'''
    b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))
    assert b_tls.success

def test__init__attributes():
    '''Assert class attributes'''
    b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))
    assert b_tls.log_name == 'test__init__.beetools.beetools'
    assert b_tls.app_desc == 'Testing __init__()'
    assert b_tls.app_ini_file_name is None
    assert b_tls.app_name == 'test__init__'
    assert b_tls.app_ver == _VERSION
    assert b_tls.archive_sub_fldr == 'VersionArchive'
    assert b_tls.cls
    assert b_tls.dur_hours == 0
    assert b_tls.dur_min == 0
    assert b_tls.dur_sec == 0
    assert b_tls.elapsed_time == 0
    assert b_tls.end_time == 0
    assert b_tls.start_date_str == b_tls.start_time.strftime('%y%m%d%H%M%S')

def test__init__constants():
    '''Assert class constants'''
    assert DEF_LOG_LEV == 10
    assert DEF_LOG_LEV_FILE == 10
    assert DEF_LOG_LEV_CON == 30
    assert LOG_FILE_FORMAT == '%(asctime)s%(msecs)d;%(levelname)s;%(name)s;%(funcName)s;%(message)s'
    assert LOG_CONSOLE_FORMAT == '\x1b[0;31;40m\n%(levelname)s - %(name)s - %(funcName)s - %(message)s\x1b[0m'

    # Defb_tlslt date format strings
    assert LOG_DATE_FORMAT == '%Y%m%d%H%M%S'
    assert LONG_DATE_FORMAT == '%Y%m%d'
    assert TIME_FORMAT == '%H%M%S'

    # Message defb_tlslts
    assert BAR_LEN == 50
    assert MSG_LEN == 50
    assert CRASH_RETRY == 2

    # Operating system name defb_tlslts
    assert WINDOWS == 'windows'
    assert LINUX == 'linux'
    assert MACOS == 'macos'
    assert AIX == 'aix'

# test__init__simple()
# test__init__attributes()
# test__init__constants()

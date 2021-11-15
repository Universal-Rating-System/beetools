'''Testing script__init__()'''

import configparser
from pathlib import Path
import os
import sys
import beetools


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = '0.0.5'


btls = beetools.Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)


class TestUtils:
    def test_tools_constants(self):
        '''Assert class constants'''
        assert beetools.DEF_LOG_LEV == 10
        assert beetools.DEF_LOG_LEV_FILE == 10
        assert beetools.DEF_LOG_LEV_CON == 30
        assert (
            beetools.LOG_FILE_FORMAT
            == '%(asctime)s%(msecs)d;%(levelname)s;%(name)s;%(funcName)s;%(message)s'
        )
        assert (
            beetools.LOG_CONSOLE_FORMAT
            == '\x1b[0;31;40m\n%(levelname)s - %(name)s - %(funcName)s - %(message)s\x1b[0m'
        )

        # Def date format strings
        assert beetools.LOG_DATE_FORMAT == '%Y%m%d%H%M%S'
        assert beetools.LONG_DATE_FORMAT == '%Y%m%d'
        assert beetools.TIME_FORMAT == '%H%M%S'

        # Def message constants
        assert beetools.BAR_LEN == 50
        assert beetools.MSG_LEN == 50
        assert beetools.CRASH_RETRY == 2

        # Operating system name defaults
        assert beetools.WINDOWS == 'windows'
        assert beetools.LINUX == 'linux'
        assert beetools.MACOS == 'macos'
        assert beetools.AIX == 'aix'

    def test_tools_do_examples(self):
        '''Testing msg_do_examples()'''
        assert beetools.do_examples(_PROJ_PATH)

    def test_get_os(self):
        '''Testing get_os()'''
        if sys.platform.startswith("win32"):
            curr_os = 'windows'
        elif sys.platform.startswith("linux"):
            curr_os = 'linux'
        elif sys.platform.startswith("darwin"):
            curr_os = 'macos'
        assert beetools.get_os() == curr_os

    def test_get_tmp_dir(self):
        '''Testing get_tmp_dir()'''
        if beetools.get_os() == beetools.LINUX:
            tmp_dir = Path("/tmp")
        elif beetools.get_os() == beetools.WINDOWS:
            tmp_dir = Path(os.environ["TEMP"])
        elif beetools.get_os() == beetools.MACOS:
            tmp_dir = Path(os.environ["TMPDIR"])
        assert beetools.get_tmp_dir() == tmp_dir

    def test_tools_is_struct_the_same_list_eq(self):
        '''Testing is_struct_the_same_list_eq()'''
        x = [1, 2]
        y = [1, 2]
        assert beetools.is_struct_the_same(x, y)

    def test_tools_is_struct_the_same_dict_eq(self):
        '''Testing is_struct_the_same_dict_eq()'''
        x = {1: "One", 2: "Two"}
        y = {2: "Two", 1: "One"}
        assert beetools.is_struct_the_same(x, y)

    def test_tools_is_struct_the_same_dict_diff_keys(self):
        '''Testing is_struct_the_same_dict_diff_keys()'''
        x = {1: "One", 3: "Two"}
        y = {1: "One", 2: "Two"}
        assert not beetools.is_struct_the_same(x, y)

    def test_tools_is_struct_the_same_dict_neq(self):
        '''Testing is_struct_the_same_dict_neq()'''
        y = {2: "Two", 1: "One"}
        z = {2: "Two", 1: "Three"}
        assert not beetools.is_struct_the_same(y, z, "ref str")

    def test_tools_is_struct_the_same_len(self):
        '''Testing is_struct_the_same_len()'''
        x = [1, 2]
        y = [1, 2, 3]
        assert not beetools.is_struct_the_same(x, y)

    def test_tools_result_rep_true(self):
        '''Testing tools_result_rep_true()'''
        assert (
            beetools.result_rep(True)
            == "test_tools_result_rep_true - \x1b[32mSuccess\x1b[0m (No Comment)"
        )

    def test_tools_result_rep_false(self):
        '''Testing tools_result_rep_false()'''
        assert (
            beetools.result_rep(False)
            == "test_tools_result_rep_false - \x1b[31mFailed\x1b[0m (No Comment)"
        )

    def test_tools_rm_temp_locked_file(self):
        '''Testing tools_rm_temp_locked_file()'''
        tmp_test = beetools.get_tmp_dir() / "test"
        # if beetools.get_os() in [beetools.LINUX, beetools.MACOS]:
        #     cmd = ["mkdir -p {}".format(tmp_test)]
        # elif beetools.get_os() == beetools.WINDOWS:
        #     cmd = ["md {}".format(tmp_test)]
        assert beetools.rm_temp_locked_file(tmp_test)

    def test_tools_rm_tree(self, make_self_destruct_working_dir):
        '''Testing tools_rm_tree()'''
        working_dir = make_self_destruct_working_dir.bee_dir
        tmp_t1 = Path(working_dir, 'T1')
        if beetools.get_os() == beetools.WINDOWS:
            cmd = ['md {}'.format(tmp_t1)]
        elif beetools.get_os() in [beetools.LINUX, beetools.MACOS]:
            cmd = ['mkdir -p {}'.format(tmp_t1)]
        beetools.exec_batch_in_session(cmd, p_verbose=False)
        t_file = working_dir / Path('t.tmp')
        t_file.touch(mode=0o666, exist_ok=True)
        t_file = tmp_t1 / Path('t.tmp')
        t_file.touch(mode=0o666, exist_ok=True)
        assert beetools.rm_tree(working_dir, p_crash=True)
        pass

    def test_select_os_dir_from_config_simple(self):
        '''Testing select_os_dir_from_config_simple()'''
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
        if beetools.get_os() == beetools.LINUX:
            bee_dir = "/usr/local/bin"
        elif beetools.get_os() == beetools.WINDOWS:
            bee_dir = "c:\\Program Files"
        elif beetools.get_os() == beetools.MACOS:
            bee_dir = "/System"
        assert (
            str(beetools.select_os_dir_from_config(cnf, "Folders", "MyFolderOnSystem"))
            == bee_dir
        )


del btls

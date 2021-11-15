'''Testing script__init__()'''

from pathlib import Path
import beetools


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = '0.0.5'


btls = beetools.Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)


class TestScript:
    def test__do_example(self):
        '''Testing script_do_example()'''
        assert beetools.do_examples()

    def test__exec_batch(self):
        '''Testing script_exec_batch()'''
        tmp_test = beetools.get_tmp_dir() / "test"
        tmp_t1 = tmp_test / "T1"
        if tmp_test.exists():
            beetools.rm_tree(tmp_test)
        if beetools.get_os() in [beetools.LINUX, beetools.MACOS]:
            cmds = [
                ['mkdir', '-p', '{}'.format(tmp_t1)],
                ['ls', '-l', '{}'.format(tmp_test)],
            ]
        elif beetools.get_os() == beetools.WINDOWS:
            cmds = [
                ['md', '{}'.format(tmp_t1)],
                ['dir', '/B', '{}'.format(tmp_test)],
            ]
        assert beetools.exec_batch(cmds, p_verbose=False)

    def test__exec_batch_in_session(self):
        '''Testing script_exec_batch_in_session()'''
        tmp_test = beetools.get_tmp_dir() / "test"
        tmp_t1 = tmp_test / "T1"
        if tmp_test.exists():
            beetools.rm_tree(tmp_test)
        if beetools.get_os() in [beetools.LINUX, beetools.MACOS]:
            batch = [
                "mkdir -p {}".format(tmp_t1),
                "ls -l {}".format(tmp_test),
                "rm -R {}".format(tmp_test),
            ]
        elif beetools.get_os() == beetools.WINDOWS:
            batch = [
                "md {}".format(tmp_t1),
                "dir /B {}".format(tmp_test),
                "rd /Q /S {}".format(tmp_test),
            ]
        assert beetools.exec_batch_in_session(batch, p_verbose=False)

    def test__exec_cmd(self):
        '''Testing script_exec_cmd()'''
        assert beetools.exec_cmd(["echo", "Hello"])

    def test__write_script(self):
        '''Testing script_exec_batch()'''
        script_pth = beetools.get_tmp_dir() / _PROJ_NAME
        cmds = [
            ['echo', 'Hello'],
            ['echo', 'Goodbye'],
        ]
        assert beetools.write_script(script_pth, cmds) == 'echo Hello\necho Goodbye\n'


del btls

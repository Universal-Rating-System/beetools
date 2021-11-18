'''Testing script__init__()'''

from pathlib import Path
from beetools import beescript, beearchiver, beeutils


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = '0.0.5'


btls = beearchiver.Archiver(_PROJ_NAME, _PROJ_DESC, _PROJ_PATH)


class TestScript:
    def test__do_example(self):
        '''Testing script_do_example()'''
        assert beescript.do_examples()
        pass

    def test__exec_batch(self, make_self_destruct_working_dir):
        '''Testing script_exec_batch()'''

        tmp_test = make_self_destruct_working_dir.dir / "test"
        tmp_t1 = tmp_test / "T1"
        if beeutils.get_os() in [beeutils.LINUX, beeutils.MACOS]:
            cmds = [
                ['mkdir', '-p', '{}'.format(tmp_t1)],
                ['ls', '-l', '{}'.format(tmp_test)],
            ]
        elif beeutils.get_os() == beeutils.WINDOWS:
            cmds = [
                ['md', '{}'.format(tmp_t1)],
                ['dir', '/B', '{}'.format(tmp_test)],
            ]
        assert beescript.exec_batch(cmds, p_verbose=False)
        pass

    def test__exec_batch_in_session(self, make_self_destruct_working_dir):
        '''Testing script_exec_batch_in_session()'''
        tmp_test = make_self_destruct_working_dir.dir / "test"
        tmp_t1 = tmp_test / "T1"
        if beeutils.get_os() in [beeutils.LINUX, beeutils.MACOS]:
            batch = [
                "mkdir -p {}".format(tmp_t1),
                "ls -l {}".format(tmp_test),
                "rm -R {}".format(tmp_test),
            ]
        elif beeutils.get_os() == beeutils.WINDOWS:
            batch = [
                "md {}".format(tmp_t1),
                "dir /B {}".format(tmp_test),
                "rd /Q /S {}".format(tmp_test),
            ]
        assert beescript.exec_batch_in_session(batch, p_verbose=False)
        pass

    def test__exec_cmd(self):
        '''Testing script_exec_cmd()'''
        assert beescript.exec_cmd(["echo", "Hello"])
        pass

    def test__write_script(self, make_self_destruct_working_dir):
        '''Testing script_exec_batch()'''
        script_pth = make_self_destruct_working_dir.dir / _PROJ_NAME
        cmds = [
            ['echo', 'Hello'],
            ['echo', 'Goodbye'],
        ]
        assert beescript.write_script(script_pth, cmds) == 'echo Hello\necho Goodbye\n'
        pass


del btls

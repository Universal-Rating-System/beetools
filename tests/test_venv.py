'''Testing script__init__()'''

# import configparser
from pathlib import Path
from beetools import beearchiver, beeutils, beevenv


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = '0.0.5'


btls = beearchiver.Archiver(_PROJ_NAME, _PROJ_DESC, _PROJ_PATH)


class TestVenv:
    def test_venv_activate(self, make_self_destruct_working_dir) -> object:
        '''Testing venv_activate()'''
        if beeutils.get_os() == beeutils.WINDOWS:
            cmd = "CALL " + str(
                make_self_destruct_working_dir.dir
                / Path("bee-project_env", "Scripts", "activate")
            )
        else:
            cmd = "source " + str(
                make_self_destruct_working_dir.dir
                / Path("bee-project_env", "bin", "activate")
            )
        assert (
            beevenv.activate(make_self_destruct_working_dir.dir, "bee-project") == cmd
        )

    def test_venv_do_example(self):
        '''Testing venv_do_example()'''
        assert beevenv.do_examples()

    def test_venv_get_dir(self, make_self_destruct_working_dir):
        '''Testing venv_get_dir()'''
        assert str(
            beevenv.get_dir(make_self_destruct_working_dir.dir, "bee-project")
        ) == str(Path(make_self_destruct_working_dir.dir, "bee-project_env"))

    def test_venv_install_in(self, make_self_destruct_working_dir):
        '''Testing install_in_venv()'''
        project_name = "new-project"
        beevenv.set_up(beeutils.get_tmp_dir(), project_name, ["pip"], p_verbose=True)
        assert beevenv.install_in(
            make_self_destruct_working_dir.dir,
            project_name,
            ["echo Installing in VEnv", "pip install wheel", "echo Done!"],
        )

    def test_venv_set_up(self, make_self_destruct_working_dir):
        '''Testing venv_set_up()'''
        project_name = "new-project"
        assert beevenv.set_up(
            make_self_destruct_working_dir.dir,
            project_name,
            ["pip", "wheel"],
            p_verbose=False,
        )


del btls

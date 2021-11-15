'''Testing script__init__()'''

# import configparser
from pathlib import Path
import os
import beetools


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = '0.0.5'


btls = beetools.Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)


class TestVenv:
    def test_venv_activate(self) -> object:
        '''Testing venv_activate()'''
        if beetools.get_os() == beetools.WINDOWS:
            cmd = "CALL " + str(
                beetools.get_tmp_dir() / Path("bee-project_env", "Scripts", "activate")
            )
        else:
            cmd = "source " + str(
                beetools.get_tmp_dir() / Path("bee-project_env", "bin", "activate")
            )
        assert beetools.activate(beetools.get_tmp_dir(), "bee-project") == cmd

    def test_venv_do_example(self):
        '''Testing venv_do_example()'''
        assert beetools.do_examples()

    def test_venv_get_dir(self):
        '''Testing venv_get_dir()'''
        if beetools.get_os() in [beetools.LINUX, beetools.MACOS]:
            tmp_dir = "/tmp"
        elif beetools.get_os() == beetools.WINDOWS:
            tmp_dir = os.environ["TEMP"]
        assert str(beetools.get_dir(beetools.get_tmp_dir(), "bee-project")) == str(
            Path(tmp_dir, "bee-project_env")
        )

    def test_venv_install_in(self):
        '''Testing install_in_venv()'''
        project_name = "new-project"
        if beetools.get_os() in [beetools.LINUX, beetools.MACOS]:
            beetools.exec_cmd(
                [
                    "sudo",
                    "rm",
                    "-R",
                    "-f",
                    str(beetools.get_dir(beetools.get_tmp_dir(), project_name)),
                ]
            )
        elif beetools.get_os() == beetools.WINDOWS:
            beetools.exec_cmd(
                [
                    "rd",
                    "/S",
                    "/Q",
                    str(beetools.get_dir(beetools.get_tmp_dir(), project_name)),
                ],
                p_crash=False,
            )
        beetools.set_up(beetools.get_tmp_dir(), project_name, ["pip"], p_verbose=True)
        assert beetools.install_in(
            beetools.get_tmp_dir(),
            project_name,
            ["echo Installing in VEnv", "pip install wheel", "echo Done!"],
        )

    def test_venv_set_up(self):
        '''Testing venv_set_up()'''
        project_name = "new-project"
        if beetools.get_os() in [beetools.LINUX, beetools.MACOS]:
            beetools.exec_cmd(
                [
                    "sudo",
                    "rm",
                    "-R",
                    "-f",
                    # str(get_venv_dir(get_tmp_dir(), project_name)),
                    str(beetools.get_dir(beetools.get_tmp_dir(), project_name)),
                ],
                p_crash=False,
            )
        elif beetools.get_os() == beetools.WINDOWS:
            beetools.exec_cmd(
                [
                    "rd",
                    "/S",
                    "/Q",
                    str(beetools.get_dir(beetools.get_tmp_dir(), project_name)),
                ],
                p_crash=False,
            )
        assert beetools.set_up(
            beetools.get_tmp_dir(), "new-project", ["pip", "wheel"], p_verbose=False
        )


del btls

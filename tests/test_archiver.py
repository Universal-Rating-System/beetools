'''Testing archiver__init__()'''

from pathlib import Path
from beetools import beearchiver


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem


btls = beearchiver.Archiver(_PROJ_DESC, _PROJ_PATH)


class TestArchiver:
    def test__init__module_logger_false(self, setup_env_module):
        '''Assert class __init__'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
        )

        assert t_archiver.app_desc == 'Test application description'
        assert t_archiver.app_ini_file_name is None
        assert t_archiver.app_name == 'testapp'
        assert t_archiver.app_pth == module_setup.app_dir / 'testapp' / 'testapp.py'
        assert t_archiver.app_root_dir == module_setup.app_dir.parents[1]
        assert t_archiver.app_ver == module_setup.app_ver
        assert t_archiver.arc_dir == module_setup.app_dir.parents[1] / 'VersionArchive'
        assert t_archiver.arc_excl_dir == ['Archive', 'VersionArchive', 'build']
        assert t_archiver.arc_extern_dir is None
        assert t_archiver.arc_incl_ext == ['ini', 'py']
        assert t_archiver.arc_pth == module_setup.app_dir.parents[
            1
        ] / 'VersionArchive' / 'testapp {} ({} Beta).zip'.format(
            t_archiver.start_date_str, module_setup.app_ver
        )
        assert t_archiver.log_name is None
        assert t_archiver.logger is None
        assert t_archiver.cls
        assert t_archiver.dur_hours == 0
        assert t_archiver.dur_min == 0
        assert t_archiver.dur_sec == 0
        assert t_archiver.elapsed_time == 0
        assert t_archiver.end_time == 0
        assert t_archiver.start_date_str == t_archiver.start_time.strftime(
            '%y%m%d%H%M%S'
        )
        assert t_archiver.success
        assert t_archiver.version_archive == 'VersionArchive'

    def test__init__logger_true(self, setup_env_module):
        '''Assert class __init__'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
            p_parent_log_name=module_setup.app_name,
            p_arc_incl_ext=['ini', 'txt'],
        )

        assert t_archiver.app_desc == 'Test application description'
        assert t_archiver.app_ini_file_name is None
        assert t_archiver.app_name == 'testapp'
        assert t_archiver.app_pth == module_setup.app_dir / 'testapp' / 'testapp.py'
        assert t_archiver.app_root_dir == module_setup.app_dir.parents[1]
        assert t_archiver.app_ver == module_setup.app_ver
        assert t_archiver.arc_dir == module_setup.app_dir.parents[1] / 'VersionArchive'
        assert t_archiver.arc_excl_dir == ['Archive', 'VersionArchive', 'build']
        assert t_archiver.arc_incl_ext == ['ini', 'py', 'txt']
        assert t_archiver.arc_pth == module_setup.app_dir.parents[
            1
        ] / 'VersionArchive' / 'testapp {} ({} Beta).zip'.format(
            t_archiver.start_date_str, module_setup.app_ver
        )
        assert t_archiver.cls
        assert t_archiver.dur_hours == 0
        assert t_archiver.dur_min == 0
        assert t_archiver.dur_sec == 0
        assert t_archiver.elapsed_time == 0
        assert t_archiver.end_time == 0
        assert t_archiver.log_name == '{}.beearchiver'.format(module_setup.app_name)
        assert t_archiver.logger is not None
        assert t_archiver.start_date_str == t_archiver.start_time.strftime(
            '%y%m%d%H%M%S'
        )
        assert t_archiver.success
        assert t_archiver.version_archive == 'VersionArchive'

    def test__init__app_path_str(self, setup_env_module):
        '''Assert class __init__'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
        )
        assert t_archiver.app_desc == 'Test application description'
        assert t_archiver.app_ini_file_name is None
        assert t_archiver.app_name == 'testapp'
        assert t_archiver.app_pth == module_setup.app_dir / 'testapp' / 'testapp.py'
        assert t_archiver.app_root_dir == module_setup.app_dir.parents[1]
        assert t_archiver.app_ver == module_setup.app_ver
        assert t_archiver.arc_dir == module_setup.app_dir.parents[1] / 'VersionArchive'
        assert t_archiver.arc_extern_dir is None
        assert t_archiver.arc_excl_dir == ['Archive', 'VersionArchive', 'build']
        assert t_archiver.arc_incl_ext == ['ini', 'py']
        assert t_archiver.arc_pth == module_setup.app_dir.parents[
            1
        ] / 'VersionArchive' / 'testapp {} ({} Beta).zip'.format(
            t_archiver.start_date_str, module_setup.app_ver
        )
        assert t_archiver.cls
        assert t_archiver.dur_hours == 0
        assert t_archiver.dur_min == 0
        assert t_archiver.dur_sec == 0
        assert t_archiver.elapsed_time == 0
        assert t_archiver.end_time == 0
        assert t_archiver.log_name is None
        assert t_archiver.logger is None
        assert t_archiver.start_date_str == t_archiver.start_time.strftime(
            '%y%m%d%H%M%S'
        )
        assert t_archiver.success
        assert t_archiver.version_archive == 'VersionArchive'

    def test__init__add_excl_dir(self, setup_env_module):
        '''Assert class __init__'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
            p_arc_excl_dir='Cov',
        )

        assert t_archiver.app_desc == 'Test application description'
        assert t_archiver.app_ini_file_name is None
        assert t_archiver.app_name == 'testapp'
        assert t_archiver.app_pth == module_setup.app_dir / 'testapp' / 'testapp.py'
        assert t_archiver.app_root_dir == module_setup.app_dir.parents[1]
        assert t_archiver.app_ver == module_setup.app_ver
        assert t_archiver.arc_dir == module_setup.app_dir.parents[1] / 'VersionArchive'
        assert t_archiver.arc_excl_dir == ['Archive', 'VersionArchive', 'build', 'Cov']
        assert t_archiver.arc_extern_dir is None
        assert t_archiver.arc_incl_ext == ['ini', 'py']
        assert t_archiver.arc_pth == module_setup.app_dir.parents[
            1
        ] / 'VersionArchive' / 'testapp {} ({} Beta).zip'.format(
            t_archiver.start_date_str, module_setup.app_ver
        )
        assert t_archiver.log_name is None
        assert t_archiver.logger is None
        assert t_archiver.cls
        assert t_archiver.dur_hours == 0
        assert t_archiver.dur_min == 0
        assert t_archiver.dur_sec == 0
        assert t_archiver.elapsed_time == 0
        assert t_archiver.end_time == 0
        assert t_archiver.start_date_str == t_archiver.start_time.strftime(
            '%y%m%d%H%M%S'
        )
        assert t_archiver.success
        assert t_archiver.version_archive == 'VersionArchive'

    def test__init__add_extern_dir(self, setup_env_module):
        '''Assert class __init__'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
            p_arc_extern_dir=module_setup.dir,
        )

        assert t_archiver.app_desc == 'Test application description'
        assert t_archiver.app_ini_file_name is None
        assert t_archiver.app_name == 'testapp'
        assert t_archiver.app_pth == module_setup.app_dir / 'testapp' / 'testapp.py'
        assert t_archiver.app_root_dir == module_setup.app_dir.parents[1]
        assert t_archiver.app_ver == module_setup.app_ver
        assert t_archiver.arc_dir == module_setup.app_dir.parents[1] / 'VersionArchive'
        assert t_archiver.arc_excl_dir == ['Archive', 'VersionArchive', 'build']
        assert t_archiver.arc_extern_dir == module_setup.dir
        assert t_archiver.arc_incl_ext == ['ini', 'py']
        assert t_archiver.arc_pth == module_setup.app_dir.parents[
            1
        ] / 'VersionArchive' / 'testapp {} ({} Beta).zip'.format(
            t_archiver.start_date_str, module_setup.app_ver
        )
        assert t_archiver.log_name is None
        assert t_archiver.logger is None
        assert t_archiver.cls
        assert t_archiver.dur_hours == 0
        assert t_archiver.dur_min == 0
        assert t_archiver.dur_sec == 0
        assert t_archiver.elapsed_time == 0
        assert t_archiver.end_time == 0
        assert t_archiver.start_date_str == t_archiver.start_time.strftime(
            '%y%m%d%H%M%S'
        )
        assert t_archiver.success
        assert t_archiver.version_archive == 'VersionArchive'

    def test__init__module_with_setup_cfg(self, setup_env_module):
        '''Assert class __init__'''
        module_setup = setup_env_module
        (module_setup.app_dir.parents[1] / 'setup.cfg').write_text(
            '[metadata]\nversion = 0.0.1\n'
        )
        app_pth = module_setup.app_dir / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
        )

        assert t_archiver.app_desc == 'Test application description'
        assert t_archiver.app_ini_file_name is None
        assert t_archiver.app_name == 'testapp'
        assert t_archiver.app_pth == module_setup.app_dir / 'testapp.py'
        assert t_archiver.app_root_dir == module_setup.app_dir.parents[1]
        assert t_archiver.app_ver == '0.0.1'
        assert t_archiver.arc_dir == module_setup.app_dir.parents[1] / 'VersionArchive'
        assert t_archiver.arc_excl_dir == ['Archive', 'VersionArchive', 'build']
        assert t_archiver.arc_extern_dir is None
        assert t_archiver.arc_incl_ext == ['ini', 'py']
        assert t_archiver.arc_pth == module_setup.app_dir.parents[
            1
        ] / 'VersionArchive' / 'testapp {} (0.0.1 Beta).zip'.format(
            t_archiver.start_date_str
        )
        assert t_archiver.log_name is None
        assert t_archiver.logger is None
        assert t_archiver.cls
        assert t_archiver.dur_hours == 0
        assert t_archiver.dur_min == 0
        assert t_archiver.dur_sec == 0
        assert t_archiver.elapsed_time == 0
        assert t_archiver.end_time == 0
        assert t_archiver.start_date_str == t_archiver.start_time.strftime(
            '%y%m%d%H%M%S'
        )
        assert t_archiver.success
        assert t_archiver.version_archive == 'VersionArchive'

    def test__init__module_without_setup_cfg(self, setup_env_module):
        '''Assert class __init__'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
        )

        assert t_archiver.app_desc == 'Test application description'
        assert t_archiver.app_ini_file_name is None
        assert t_archiver.app_name == 'testapp'
        assert t_archiver.app_pth == module_setup.app_dir / 'testapp.py'
        assert t_archiver.app_root_dir == module_setup.app_dir.parents[1]
        assert t_archiver.app_ver == '0.0.0'
        assert t_archiver.arc_dir == module_setup.app_dir.parents[1] / 'VersionArchive'
        assert t_archiver.arc_excl_dir == ['Archive', 'VersionArchive', 'build']
        assert t_archiver.arc_extern_dir is None
        assert t_archiver.arc_incl_ext == ['ini', 'py']
        assert t_archiver.arc_pth == module_setup.app_dir.parents[
            1
        ] / 'VersionArchive' / 'testapp {} ({} Beta).zip'.format(
            t_archiver.start_date_str, module_setup.app_ver
        )
        assert t_archiver.log_name is None
        assert t_archiver.logger is None
        assert t_archiver.cls
        assert t_archiver.dur_hours == 0
        assert t_archiver.dur_min == 0
        assert t_archiver.dur_sec == 0
        assert t_archiver.elapsed_time == 0
        assert t_archiver.end_time == 0
        assert t_archiver.start_date_str == t_archiver.start_time.strftime(
            '%y%m%d%H%M%S'
        )
        assert t_archiver.success
        assert t_archiver.version_archive == 'VersionArchive'

    def test__init__module_version_def(self, setup_env_module):
        '''Assert class __init__'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
        )

        assert t_archiver.app_desc == 'Test application description'
        assert t_archiver.app_ini_file_name is None
        assert t_archiver.app_name == 'testapp'
        assert t_archiver.app_pth == module_setup.app_dir / 'testapp.py'
        assert t_archiver.app_root_dir == module_setup.app_dir.parents[1]
        assert t_archiver.app_ver == '0.0.0'
        assert t_archiver.arc_dir == module_setup.app_dir.parents[1] / 'VersionArchive'
        assert t_archiver.arc_excl_dir == ['Archive', 'VersionArchive', 'build']
        assert t_archiver.arc_extern_dir is None
        assert t_archiver.arc_incl_ext == ['ini', 'py']
        assert t_archiver.arc_pth == module_setup.app_dir.parents[
            1
        ] / 'VersionArchive' / 'testapp {} (0.0.0 Beta).zip'.format(
            t_archiver.start_date_str
        )
        assert t_archiver.log_name is None
        assert t_archiver.logger is None
        assert t_archiver.cls
        assert t_archiver.dur_hours == 0
        assert t_archiver.dur_min == 0
        assert t_archiver.dur_sec == 0
        assert t_archiver.elapsed_time == 0
        assert t_archiver.end_time == 0
        assert t_archiver.start_date_str == t_archiver.start_time.strftime(
            '%y%m%d%H%M%S'
        )
        assert t_archiver.success
        assert t_archiver.version_archive == 'VersionArchive'

    def test__init__module_version_by_parm(self, setup_env_module):
        '''Assert class __init__'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc, app_pth, p_app_ver='1.1.1'
        )

        assert t_archiver.app_desc == 'Test application description'
        assert t_archiver.app_ini_file_name is None
        assert t_archiver.app_name == 'testapp'
        assert t_archiver.app_pth == module_setup.app_dir / 'testapp.py'
        assert t_archiver.app_root_dir == module_setup.app_dir.parents[1]
        assert t_archiver.app_ver == '1.1.1'
        assert t_archiver.arc_dir == module_setup.app_dir.parents[1] / 'VersionArchive'
        assert t_archiver.arc_excl_dir == ['Archive', 'VersionArchive', 'build']
        assert t_archiver.arc_extern_dir is None
        assert t_archiver.arc_incl_ext == ['ini', 'py']
        assert t_archiver.arc_pth == module_setup.app_dir.parents[
            1
        ] / 'VersionArchive' / 'testapp {} (1.1.1 Beta).zip'.format(
            t_archiver.start_date_str
        )
        assert t_archiver.log_name is None
        assert t_archiver.logger is None
        assert t_archiver.cls
        assert t_archiver.dur_hours == 0
        assert t_archiver.dur_min == 0
        assert t_archiver.dur_sec == 0
        assert t_archiver.elapsed_time == 0
        assert t_archiver.end_time == 0
        assert t_archiver.start_date_str == t_archiver.start_time.strftime(
            '%y%m%d%H%M%S'
        )
        assert t_archiver.success
        assert t_archiver.version_archive == 'VersionArchive'

    def test__init__module_version_by_setup_cfg(self, setup_env_module):
        '''Assert class __init__'''
        module_setup = setup_env_module
        (module_setup.app_dir.parents[1] / 'setup.cfg').write_text(
            '[metadata]\nversion = 2.2.2\n'
        )
        app_pth = module_setup.app_dir / 'testapp.py'
        t_archiver = beearchiver.Archiver(module_setup.app_desc, app_pth)

        assert t_archiver.app_desc == 'Test application description'
        assert t_archiver.app_ini_file_name is None
        assert t_archiver.app_name == 'testapp'
        assert t_archiver.app_pth == module_setup.app_dir / 'testapp.py'
        assert t_archiver.app_root_dir == module_setup.app_dir.parents[1]
        assert t_archiver.app_ver == '2.2.2'
        assert t_archiver.arc_dir == module_setup.app_dir.parents[1] / 'VersionArchive'
        assert t_archiver.arc_excl_dir == ['Archive', 'VersionArchive', 'build']
        assert t_archiver.arc_extern_dir is None
        assert t_archiver.arc_incl_ext == ['ini', 'py']
        assert t_archiver.arc_pth == module_setup.app_dir.parents[
            1
        ] / 'VersionArchive' / 'testapp {} (2.2.2 Beta).zip'.format(
            t_archiver.start_date_str
        )
        assert t_archiver.log_name is None
        assert t_archiver.logger is None
        assert t_archiver.cls
        assert t_archiver.dur_hours == 0
        assert t_archiver.dur_min == 0
        assert t_archiver.dur_sec == 0
        assert t_archiver.elapsed_time == 0
        assert t_archiver.end_time == 0
        assert t_archiver.start_date_str == t_archiver.start_time.strftime(
            '%y%m%d%H%M%S'
        )
        assert t_archiver.success
        assert t_archiver.version_archive == 'VersionArchive'

    def test_do_examples(self):
        '''Testing archiver_do_examples()'''
        assert beearchiver.do_examples()

    def test_find_app_root_dir_module(self, setup_env_module):
        '''Testing archiver__init__()'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
        )
        assert t_archiver.find_app_root_dir() == module_setup.app_dir.parents[1]
        pass

    def test_find_app_root_dir_package(self, setup_env_package):
        '''Testing archiver__init__()'''
        module_setup = setup_env_package
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
        )
        assert t_archiver.find_app_root_dir() == module_setup.app_dir.parents[0]
        pass

    def test_find_app_root_dir_sitepackage(self, setup_env_sitepackage):
        '''Testing archiver__init__()'''
        module_setup = setup_env_sitepackage
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
        )
        assert t_archiver.find_app_root_dir() == module_setup.app_dir
        pass

    def test_find_app_root_dir_tests(self, setup_env_tests):
        '''Testing archiver__init__()'''
        module_setup = setup_env_tests
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
        )
        assert t_archiver.find_app_root_dir() == module_setup.app_dir.parents[0]
        pass

    def test_find_app_root_dir_root(self, setup_env_module):
        '''Testing archiver__init__()'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir.parents[1]
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
        )
        assert t_archiver.find_app_root_dir() == module_setup.app_dir.parents[1]
        pass

    def test_is_app_in_dev_module_true(self, setup_env_module):
        '''Testing archiver__init__()'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
        )
        assert t_archiver.is_dev_mode()

    def test_make_archive(self, setup_env_module):
        '''Testing archiver_make_archive'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
            # p_arc_extern_dir=module_setup.arc_extern_dir
        )
        assert t_archiver.arc_pth.exists()
        # rm_tree(anchor_dir)
        pass

    def test_make_archive_external(self, setup_env_module):
        '''Testing archiver_make_archive'''
        module_setup = setup_env_module
        app_pth = module_setup.app_dir / 'testapp' / 'testapp.py'
        arc_extern_dir = module_setup.dir / 'extarchive'
        t_archiver = beearchiver.Archiver(
            module_setup.app_desc,
            app_pth,
            p_arc_extern_dir=arc_extern_dir,
        )
        assert (t_archiver.arc_extern_dir / t_archiver.arc_pth.name).exists()

    def test_msg_display_simple(self):
        '''Testing msgdisplay()'''
        assert (
            beearchiver.msg_display("Display message")
            == "\x1b[37mDisplay message                               "
        )

    def test_msg_error(self):
        '''Testing msg_error()'''
        assert beearchiver.msg_error("Error message") == "\x1b[31mError message\x1b[0m"

    def test_msg_header(self):
        '''Testing msg_header()'''
        assert (
            beearchiver.msg_header("Header message") == "\x1b[36mHeader message\x1b[0m"
        )

    def test_msg_info(self):
        '''Testing msg_info()'''
        assert beearchiver.msg_info("Info message") == "\x1b[33mInfo message\x1b[0m"

    def test_msg_milestone(self):
        '''Testing msg_milestone()'''
        assert (
            beearchiver.msg_milestone("Milestone message")
            == "\x1b[35mMilestone message\x1b[0m"
        )

    def test_msg_ok(self):
        '''Testing msg_ok()'''
        assert beearchiver.msg_ok("OK message") == "\x1b[32mOK message\x1b[0m"

    def test_print_footer(self):
        '''Testing archiver_print_footer()'''
        t_archiver = beearchiver.Archiver(_PROJ_DESC, _PROJ_PATH)
        assert t_archiver.print_footer()

    def test_print_header_simple(self):
        '''Testing print_header_simple()'''
        t_archiver = beearchiver.Archiver(_PROJ_DESC, _PROJ_PATH)
        assert t_archiver.print_header()


del btls

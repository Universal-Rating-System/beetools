"""Tools for Bright Edge eServices developments & projects

Designed for the use in the Bright Edge eServices echo system. It defines
methods and functions for general use purposes.

Archiver creates an archive of the key project files, print coloured messages
to console with default parameters.

ToDo
=====
1. Better example on the logging integration.
2. Complete doctests for all methods & functions.

"""
# import configparser
# import datetime
# import logging
# import os
# import shutil
# import sys
# import tempfile
# import zipfile
# from pathlib import Path
from termcolor import colored

# _PROJ_DESC = __doc__.split('\n')[0]
# _PROJ_PATH = Path(__file__)
# _PROJ_NAME = _PROJ_PATH.stem
# _PROJ_VERSION = '3.3.0'

# Message defaults
BAR_LEN = 50
MSG_LEN = 50
CRASH_RETRY = 2


# def _add_parm(def_parm, new_parm):
#     if isinstance(new_parm, list):
#         def_parm += [x for x in new_parm if x not in def_parm]
#     elif isinstance(new_parm, str) and new_parm not in def_parm:
#         def_parm.append(new_parm)
#     return def_parm


def msg_display(p_msg, p_len=MSG_LEN, p_color='white') -> str:
    """Return a text message in white on black.

    Parameters
    ----------
    p_msg
        The message
    p_len
        The fixed length of the message. Default is beetools.MSG_LEN
    p_color
        Color of text, always on black.
            [ grey, red, green, yellow, blue, magenta, cyan, white ]

    Returns
    -------
    str
        Text in the specified color.

    Examples
    --------
    >>> from beetools.beearchiver import msg_display
    >>> msg_display( 'Display message' )
    '\\x1b[37mDisplay message                               '

    """
    msg = colored('{: <{len}}'.format(p_msg, len=p_len), p_color)
    return msg[:p_len] + ' '


def msg_error(p_msg) -> str:
    """Return an "error" text message in red on black

    Parameters
    ----------
    p_msg
        The message

    Returns
    -------
    str
        Text in red on black.

    Examples
    --------
    >>> from beetools.beearchiver import msg_error
    >>> msg_error( 'Error message' )
    '\\x1b[31mError message\\x1b[0m'

    """
    return colored(f'{p_msg}', 'red')


def msg_header(p_msg) -> str:
    """Return a "header" text message in cyan on black

    Parameters
    ----------
    p_msg
        The message

    Returns
    -------
    str
        Text in red on black.

    Examples
    --------
    >>> from beetools.beearchiver import msg_header
    >>> msg_header( 'Header message' )
    '\\x1b[36mHeader message\\x1b[0m'

    """
    return colored(f'{p_msg}', 'cyan')


def msg_info(p_msg) -> str:
    """Return an "information" text message in yellow on black

    Parameters
    ----------
    p_msg
        The message

    Returns
    -------
    str
        Text in red on black.

    Examples
    --------
    >>> from beetools.beearchiver import msg_info
    >>> msg_info( 'Info message' )
    '\\x1b[33mInfo message\\x1b[0m'

    """
    return colored(f'{p_msg}', 'yellow')


def msg_milestone(p_msg) -> str:
    """Return a "milestone" text message in magenta on black

    Parameters
    ----------
    p_msg
        The message

    Returns
    -------
    str
        Text in red on black.

    Examples
    --------
    >>> from beetools.beearchiver import msg_milestone
    >>> msg_milestone( 'Milestone message' )
    '\\x1b[35mMilestone message\\x1b[0m'

    """
    return colored(f'{p_msg}', 'magenta')


def msg_ok(p_msg) -> str:
    """Return an "OK" text message in green on black

    Parameters
    ----------
    p_msg
        The message

    Returns
    -------
    str
        Text in red on black.

    Examples
    --------
    >>> from beetools.beearchiver import msg_ok
    >>> msg_ok( 'OK message' )
    '\\x1b[32mOK message\\x1b[0m'

    """
    return colored(f'{p_msg}', 'green')


# def example_archiver(p_cls=True):
#     """Example to illustrate usage
#
#     Parameters
#     ----------
#     p_cls
#         Clear the screen before start
#         Default is True
#
#     Returns
#     -------
#     bool
#         Successful execution [ b_tls.arc_pth | False ]
#
#     Examples
#     --------
#
#     """
#     success = True
#     app_name = 'TestApp'
#     app_desc = 'Test application description'
#     with tempfile.TemporaryDirectory() as temp_dir:
#         app_dir = Path(temp_dir, app_name, 'src', app_name.lower())
#         app_dir.mkdir(parents=True)
#         app_pth = app_dir / Path(app_name.lower()).with_suffix('.py')
#         app_pth.touch()
#         arc_extern_dir = Path(temp_dir, 'external')
#         # arc_extern_dir.mkdir(parents = True)
#         t_archiver = Archiver(app_desc, app_pth, p_arc_extern_dir=arc_extern_dir)
#     t_archiver.print_header(p_cls=p_cls)
#     t_archiver.print_footer()
#     # working_dir.rmdir()
#     return success


def example_messaging():
    """Standard example to illustrate standard use.

    Parameters
    ----------

    Returns
    -------
    bool
        Successful execution [ b_tls.archive_path | False ]

    Examples
    --------

    """
    success = True
    print(
        msg_display(
            f'This message print in blue and cut at {MSG_LEN} character because it is too long!',
            p_color='blue',
        )
    )
    print(msg_ok('This message is an OK message'))
    print(msg_info('This is an info message'))
    print(msg_milestone('This is a milestone message'))
    print(msg_error('This is a warning message'))
    return success


def do_examples(p_cls=True):
    success = True
    # success = example_archiver(p_cls=p_cls) and success
    success = example_messaging() and success
    return success


if __name__ == '__main__':
    do_examples()

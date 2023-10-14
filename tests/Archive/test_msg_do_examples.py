'''Testing msg_do_examples()'''
from pathlib import Path

from beetools import Archiver
from beetools import beemsg


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)
_PROJ_NAME = _PROJ_PATH.stem
_PROJ_VERSION = '0.0.2'

b_tls = Archiver(_PROJ_NAME, _PROJ_VERSION, _PROJ_DESC, _PROJ_PATH)


def test_msg_do_examples():
    '''Testing msg_do_examples()'''
    assert beemsg.do_examples(_PROJ_PATH)


# test_msg_do_examples()
del b_tls

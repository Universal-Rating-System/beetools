'''Testing result_rep()'''

from pathlib import Path
from beetools import Archiver, result_rep

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_result_rep_true():
    '''Testing result_rep_true()'''
    assert (
        result_rep(True) == "test_result_rep_true - \x1b[32mSuccess\x1b[0m (No Comment)"
    )


def test_result_rep_false():
    '''Testing result_rep_false()'''
    assert (
        result_rep(False) == "test_result_rep_false - \x1b[31mFailed\x1b[0m (No Comment)"
    )

# test_result_rep_true()
# test_result_rep_false()
del b_tls

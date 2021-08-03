
'''Testing do_bash_script()'''

from pathlib import Path
from beetools import Archiver, do_examples

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'


b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_do_examples():
    '''Testing do_examples()'''
    assert do_examples(p_app_path=_path)

# test_do_examples()
del b_tls


'''Testing msg_milestone()'''

from pathlib import Path
from beetools import Archiver, msg_milestone

_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = Archiver( _name, _VERSION, __doc__, Path( _path))

def test_msg_milestone_simple():
    '''Testing msg_milestone_simple()'''
    assert msg_milestone("Milestone message") == "\x1b[35mMilestone message\x1b[0m"

# test_msg_milestone_simple()
del b_tls

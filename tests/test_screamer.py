import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from dopyr.screamer import maybe_scream

def test_screamer_silent():
    assert maybe_scream('hello world') == 'hello world'

def test_screamer_loud():
    assert maybe_scream('hello world', do_scream=True) == 'HELLO WORLD'

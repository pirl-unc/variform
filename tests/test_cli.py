from .common import eq_ 
from variform.cli import main
import pytest

def test_version():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
         main("--version")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0
   
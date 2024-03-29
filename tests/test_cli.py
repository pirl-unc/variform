from .common import eq_ 
from variform.cli import main

def test_version():
    main("--version")
    
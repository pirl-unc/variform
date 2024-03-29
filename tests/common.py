

def ok_(b):
    assert b


def eq_(x, y, msg=None):
    if msg is None:
        assert x == y
    else:
        assert x == y, msg


def neq_(x, y, msg=None):
    if msg is None:
        assert x != y
    else:
        assert x != y, msg


def gt_(x, y, msg=None):
    if msg is None:
        assert x > y
    else:
        assert x > y, msg


def gte_(x, y, msg=None):
    if msg is None:
        assert x >= y
    else:
        assert x >= y, msg


def lt_(x, y, msg=None):
    if msg is None:
        assert x < y
    else:
        assert x < y, msg


def lte_(x, y, msg=None):
    if msg is None:
        assert x <= y
    else:
        assert x <= y, msg


def almost_eq_(a, b, tol=1e-6, s=None):
    if s is None:
        assert abs(a - b) < tol
    else:
        assert abs(a - b) < tol, s

# TemporaryDirectory only got added to Python in version 3.2
try:
    # pylint: disable=no-name-in-module
    from tempfile import TemporaryDirectory

except ImportError:
    # only added in Python 3.2
    from tempfile import mkdtemp
    from shutil import rmtree

    class TemporaryDirectory(object):
        def __init__(self):
            self.name = mkdtemp()

        def __enter__(self, *args, **kwargs):
            return self.name

        def __exit__(self, type, value, traceback):
            rmtree(self.name)
            # don't suppress exceptions
            return False


class assert_raises:
    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        pass

    def to_string(self):
        return " or ".join(["%s" % e for e in self.exception_types])

    def __exit__(self, type, value, traceback):
        if type is None:
            raise AssertionError("Expected exception %s not raised" % self.to_string())
        if type not in self.exception_types:
            raise AssertionError("Expected exception %s, got %s" % (self.to_string(), type))
        return True

def raises(*exception_types):
    from functools import wraps
    
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            with assert_raises(*exception_types):
                f(*args, **kwargs)
        return wrapper
    return decorator
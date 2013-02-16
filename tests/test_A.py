from a import A
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises

class TestA(object):
    def setup_class(A):
        pass
    def teardown_class(A):
        pass
    def setUp(self):
        pass
    def teardown(self):
        pass
    def test_init(self):
        a = A()
        assert_equal(a.value, "some value")
        assert_not_equal(a.value, "incorrect value")
    def test_return_true(self):
        a=A()
        assert_equal(a.return_true(),True)
        assert_not_equal(a.return_true(), False)


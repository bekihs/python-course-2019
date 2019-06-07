from math1 import Foo
def pytest_assertrepr_compare(op, left, right):
    pass
    if isinstance(left, int) and isinstance(right, Foo):# and op == "==":
        return ["not both are FOo types"]
    if isinstance(left, Foo) and isinstance(right, Foo):# and op == "==":
        return ["Comparing Foo instances:", "   vals: {} != {}".format(left.val, right.val)]



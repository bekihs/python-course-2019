def inc(x):
    assert type(x) is int 
    return x+1
def dec(x):
    assert type(x) is int
    return x-1 


class Foo():
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val



class Document():
    def __init__(self, employeeName):
        assert type(employeeName)  is str
        self.employeeName = employeeName
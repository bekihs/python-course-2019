from document import Document
import pytest

class TestDocuments():
    def testInit(self):
        doc = Document("hadas")
        assert doc.employeeName == "hadas"
    def testInitEmptyString(self):
        doc = Document("")
        assert doc.employeeName == ""
    def testInitNumber(self):
        with pytest.raises(AssertionError):
            doc = Document(6)

    [print(p.text) for p in hadas.posts]
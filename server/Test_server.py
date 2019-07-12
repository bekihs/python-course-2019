import requests
import json
 
class TestUserApi(): 
    def test_postDocument(self):
        res = requests.post("http://localhost:5000/document" , data={
            'text':'if statments',
            'employeeId': 1
        } )
        data = res.json()
        assert(data["isOK"])

        res = requests.get("http://localhost:5000/documents")
        data = res.json()
        assert(data[len(data)-1][0] == 'if statments')
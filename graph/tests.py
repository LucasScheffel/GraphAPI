import unittest
import requests
################
from configs import URL

class GraphTests(unittest.TestCase):

    def setUp(self):
        test_data = {
            "description": "Unittest",
            "data": [
                {
                    "source": "A", 
                    "target": "B", 
                    "distance": 6
                },
                {
                    "source": "A", 
                    "target": "E", 
                    "distance": 4
                },
                {
                    "source": "B", 
                    "target": "A", 
                    "distance": 6
                },
                {
                    "source": "B", 
                    "target": "C", 
                    "distance": 2
                },
                {
                    "source": "B", 
                    "target": "D", 
                    "distance": 4
                },
                {
                    "source": "C", 
                    "target": "B", 
                    "distance": 3
                },
                {
                    "source": "C", 
                    "target": "D",
                    "distance": 1
                },
                {
                    "source": "C", 
                    "target": "E", 
                    "distance": 7
                },
                {
                    "source": "D", 
                    "target": "B", 
                    "distance": 8
                },
                {
                    "source": "E", 
                    "target": "B", 
                    "distance": 5
                },
                {
                    "source": "E", 
                    "target": "D", 
                    "distance": 7
                }
            ]
        }

        response = requests.post(URL + "graph/", json=test_data)
        assert response.status_code == 201
        self.graph_id = response.json()["id"]
    

    def test_get(self):
        response = requests.get(URL + f"graph/{self.graph_id}/")
        assert response.status_code == 200
        assert response.json()["id"] == self.graph_id


    def test_list(self):
        response = requests.get(URL + "graph/", params={'description': "Unittest"})
        assert response.status_code == 200
        assert response.json()["count"] == 1


    def test_update(self):
        response = requests.put(URL + f"graph/{self.graph_id}/", json={"description": "Unittest update"})
        assert response.status_code == 200
        assert response.json()["id"] == self.graph_id


    def tearDown(self):
        response = requests.delete(URL + f"graph/{self.graph_id}/")
        assert response.status_code == 200

    def runTests():
        print("/*----------- INITIALIZING GRAPH TESTS -----------*/")
        unittest.main()

if __name__ == '__main__':
    GraphTests.runTests()
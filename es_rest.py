import requests
import json


class ES_rest:
    def __init__(self):
        pass

    def index(self, uri, doc_data={}):
        """Create new document."""
        query = json.dumps(doc_data)
        response = requests.post(uri, data=query)
        print(response)

    def search(self, uri, term):
        """Simple Elasticsearch Query"""
        query = json.dumps({
            "query": {
                "match": {
                    "content": term
                }
            }
        })

        response = requests.get(uri, data=query)
        results = json.loads(response.text)
        return results

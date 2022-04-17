import json
import requests
from elasticsearch import Elasticsearch

class Elastic:
    def __init__(self) -> None:
        self.es = None
        self.connect()

    def connect(self):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200,'scheme': 'http'}])

    def indexing(self):
        r = requests.get('http://localhost:9200')
        i = 18
        while r.status_code == 200:
            r = requests.get('https://swapi.dev/api/people/'+ str(i))
            self.es.index(index='sw', id=i, body=json.loads(r.content))
            i=i+1

        print(i)

# es = Elastic()
# # es.indexing()
# a = es.es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})

# data = []

# es = Elasticsearch([{'host': 'localhost', 'port': 9200,'scheme': 'http'}])

# with open('/Users/vinbrain/Desktop/searching_tutorial/data/symptom.txt','r') as f:
#     for line in f:
#         data.append(line.replace('\n',''))

# with open('/Users/vinbrain/Desktop/searching_tutorial/data/symptoms_aivicare.txt','r') as f:
#     for line in f:
#         data.append(line.replace('\n',''))

# data = list(set(data))
# print(len(data))

# for i, item in enumerate(data):
#     obj = {
#         'name' : item
#     }
#     es.index(index="symptom", id=i, body=obj)

es = Elasticsearch([{'host': 'localhost', 'port': 9200,'scheme': 'http'}])
a = es.search(index="symptom", body={"query": {"match": {'name':'đau đầu'}}})
print(a)
from elasticsearch import Elasticsearch, helpers
import requests
import json

es = Elasticsearch(
    hosts=[{
        'host': 'localhost',
        'port': 9200,
        'scheme': 'http'  # 기본적으로 http 사용
    }]
)

def index_documents(documents):
    """Elasticsearch에 문서 색인"""
    actions = ""
    for doc in documents:
        action = {"index": {"_index": "documents"}, "subject" : doc['filename']}
        actions += json.dumps(action) + "\n" + json.dumps(doc) + "\n"
    
    #headers = {'Content-Type': 'application/json'; compatible-with=8'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://localhost:9200/_bulk', headers=headers, data=actions)
    if response.status_code != 200:
        raise Exception(f"Failed to index documents: {response.text}")

def search_documents(query, top_k=3):
    """Elasticsearch를 통해 관련 문서 검색"""
    headers = {"Content-Type": "application/json"}
    url = "http://localhost:9200/documents/_search"

    query_body = {
        "query": {
            "match": {
                "text": query
            }
        },
        "size": top_k
    }

    response = requests.get(url, headers=headers, data=json.dumps(query_body))
    
    if response.status_code == 200:
        hits = response.json()["hits"]["hits"]
        return [hit["_source"]["text"] for hit in hits]
    else:
        print(f"An error occurred: {response.status_code}, {response.text}")
        return []


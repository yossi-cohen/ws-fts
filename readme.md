# ws-fts

Full Text Search playground using elasticsearch

## install virtualenv python3

virtualenv -p python3 env

## packages

env/bin/pip install [package-name]

flask
requests

## index a document

curl -XPOST http://localhost:9200/test/docs/1 -d '{
    "content": "The quick brown fox"
}'

## simple search

curl -XPOST http://localhost:9200/test/docs/_search?pretty=true -d '{
    "query": {
        "match": {
            "content": "fox"
        }
    }
}'

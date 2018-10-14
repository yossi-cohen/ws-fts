# ws-fts

Full Text Search playground using elasticsearch

## install virtualenv python3

virtualenv -p python3 env

## packages

env/bin/pip install [package-name]

flask
requests
elasticsearch

## delete index

curl -XDELETE http://localhost:9200/test

## index a document

curl -XPOST http://localhost:9200/test/docs/1 -d '{
    "content": "The quick brown fox"
}'
curl -XPOST http://localhost:9200/test/docs/2 -d '{
    "content": "What does the fox say?"
}'
curl -XPOST http://localhost:9200/test/docs/3 -d '{
    "content": "The quick brown fox jumped over the lazy dog"
}'
curl -XPOST http://localhost:9200/test/docs/4 -d '{
    "content": "The quick lazy brown fox did not jump."
}'


## simple search

curl -XPOST http://localhost:9200/test/docs/_search?pretty=true -d '{
    "query": {
        "match": {
            "content": "fox"
        }
    }
}'
